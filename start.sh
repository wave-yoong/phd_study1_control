#!/bin/bash

# Flask Chatbot Startup Script

echo "Starting Flask Chatbot (Control Group)..."
echo "========================================="
echo ""

# Check if .env file exists
if [ ! -f .env ]; then
    echo "⚠️  Warning: .env file not found!"
    echo "Please copy .env.example to .env and add your OpenAI API key:"
    echo "  cp .env.example .env"
    echo "  # Then edit .env to add your API key"
    echo ""
    exit 1
fi

# Check if dependencies are installed
if ! python -c "import flask" 2>/dev/null; then
    echo "⚠️  Warning: Dependencies not installed!"
    echo "Please install dependencies first:"
    echo "  pip install -r requirements.txt"
    echo ""
    exit 1
fi

echo "✓ Environment configured"
echo "✓ Dependencies installed"
echo ""
echo "Starting server on http://localhost:5000"
echo "Press Ctrl+C to stop the server"
echo ""

cd backend
python app.py
