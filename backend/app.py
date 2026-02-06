from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import sys

# Add parent directory to path to import services and database
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.gpt_service import GPTService
from database.db_manager import DatabaseManager

app = Flask(__name__, static_folder='../frontend')
CORS(app)

# Initialize services
gpt_service = GPTService()
db_manager = DatabaseManager()


@app.route('/')
def index():
    """Serve the main chat interface."""
    return send_from_directory('../frontend', 'index.html')


@app.route('/api/conversation', methods=['POST'])
def create_conversation():
    """Create a new conversation."""
    try:
        conversation_id = db_manager.create_conversation()
        return jsonify({
            'success': True,
            'conversation_id': conversation_id
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Handle chat messages - user sends message, GPT responds immediately.
    """
    try:
        data = request.json
        user_message = data.get('message')
        conversation_id = data.get('conversation_id')
        
        if not user_message:
            return jsonify({
                'success': False,
                'error': 'Message is required'
            }), 400
        
        if not conversation_id:
            return jsonify({
                'success': False,
                'error': 'Conversation ID is required'
            }), 400
        
        # Save user message to database
        db_manager.save_message(conversation_id, 'user', user_message)
        
        # Get conversation history for context (excluding the just-added user message)
        history_rows = db_manager.get_conversation_messages(conversation_id)
        # Build conversation history from all messages except the last one (the current user message)
        conversation_history = [
            {"role": role, "content": content}
            for role, content, timestamp in history_rows[:-1]
        ]
        
        # Get GPT response immediately
        assistant_response = gpt_service.get_response(user_message, conversation_history)
        
        # Save assistant response to database
        db_manager.save_message(conversation_id, 'assistant', assistant_response)
        
        return jsonify({
            'success': True,
            'response': assistant_response
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/conversations', methods=['GET'])
def get_conversations():
    """Get all conversations."""
    try:
        conversations = db_manager.get_all_conversations()
        return jsonify({
            'success': True,
            'conversations': [
                {
                    'id': conv[0],
                    'created_at': conv[1],
                    'message_count': conv[2]
                }
                for conv in conversations
            ]
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/conversation/<int:conversation_id>/messages', methods=['GET'])
def get_messages(conversation_id):
    """Get all messages for a conversation."""
    try:
        messages = db_manager.get_conversation_messages(conversation_id)
        return jsonify({
            'success': True,
            'messages': [
                {
                    'role': msg[0],
                    'content': msg[1],
                    'timestamp': msg[2]
                }
                for msg in messages
            ]
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
