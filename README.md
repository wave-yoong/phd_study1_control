# phd_study1_control
Control group chatbot for my phd study 1

## Description
A simple Flask-based chatbot with direct GPT response functionality. This is the control group implementation where users send messages and receive immediate responses from GPT without any confirmation steps.

## Features
- Direct messaging with immediate GPT responses
- SQLite database to store all conversations and messages with timestamps
- Clean web-based chat interface
- All interactions saved for analysis

## Project Structure
```
.
├── backend/
│   └── app.py              # Main Flask application
├── services/
│   └── gpt_service.py      # OpenAI GPT integration
├── database/
│   └── db_manager.py       # SQLite database manager
├── frontend/
│   └── index.html          # Chat UI
├── requirements.txt        # Python dependencies
├── .env.example           # Example environment variables
└── README.md
```

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/wave-yoong/phd_study1_control.git
cd phd_study1_control
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment variables
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

### 4. Run the application
```bash
cd backend
python app.py
```

The application will be available at http://localhost:5000

## Database Schema

### conversations table
- `id` (INTEGER PRIMARY KEY): Unique conversation ID
- `created_at` (TIMESTAMP): When the conversation was created

### messages table
- `id` (INTEGER PRIMARY KEY): Unique message ID
- `conversation_id` (INTEGER): Foreign key to conversations table
- `role` (TEXT): Either 'user' or 'assistant'
- `content` (TEXT): Message content
- `timestamp` (TIMESTAMP): When the message was created

## API Endpoints

- `POST /api/conversation` - Create a new conversation
- `POST /api/chat` - Send a message and get immediate GPT response
- `GET /api/conversations` - Get all conversations
- `GET /api/conversation/<id>/messages` - Get messages for a specific conversation

## Usage
1. Open http://localhost:5000 in your browser
2. Type a message in the input field
3. Press Send or hit Enter
4. Receive immediate response from GPT
5. All messages are automatically saved to the database

## Notes
- This is the control group implementation with direct response functionality
- No confirmation or intermediate steps - messages get immediate responses
- All conversations and messages are stored in SQLite database for analysis
