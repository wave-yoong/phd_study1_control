# Quick Start Guide - Control Group Chatbot

## Overview
This is a simple Flask-based chatbot for PhD Study 1 (Control Group). Users send messages and receive immediate responses from GPT-3.5, with all interactions saved to a SQLite database.

## Quick Setup (5 minutes)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Configure OpenAI API Key
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your OpenAI API key
# Replace 'your_openai_api_key_here' with your actual API key
```

### Step 3: Run the Application
```bash
# Option 1: Use the startup script (Linux/Mac)
./start.sh

# Option 2: Run manually
cd backend
python app.py
```

### Step 4: Open in Browser
Navigate to: http://localhost:5000

## How It Works

1. **User sends a message** → Typed in the chat interface
2. **Immediate GPT response** → No confirmation steps, direct response
3. **All messages saved** → Stored in SQLite database with timestamps
4. **Conversation history** → Each conversation maintains context

## Features

- ✅ Clean, user-friendly chat interface
- ✅ Immediate GPT-3.5 responses (no delays or confirmations)
- ✅ All conversations and messages saved with timestamps
- ✅ Database ready for analysis
- ✅ RESTful API endpoints for integration

## Database Location

The SQLite database file (`chatbot.db`) is created automatically in the project root directory when you first run the application.

## Viewing Database Contents

```bash
# Open SQLite CLI
sqlite3 chatbot.db

# View all conversations
SELECT * FROM conversations;

# View all messages
SELECT * FROM messages;

# Exit SQLite
.exit
```

## API Endpoints

- `POST /api/conversation` - Create new conversation
- `POST /api/chat` - Send message and get response
- `GET /api/conversations` - List all conversations
- `GET /api/conversation/<id>/messages` - Get conversation messages

## Troubleshooting

### "OPENAI_API_KEY not found"
- Make sure you created a `.env` file (not `.env.example`)
- Verify your API key is correctly set in the `.env` file

### "ModuleNotFoundError"
- Run `pip install -r requirements.txt` to install dependencies

### Port 5000 already in use
- Edit `backend/app.py` and change the port number in the last line
- Or stop the process using port 5000

## Study Notes

This is the **control group** version with:
- Direct, immediate responses
- No intermediate confirmation steps
- Standard chatbot interaction pattern
- All data logged for analysis

For research questions, contact the study administrator.
