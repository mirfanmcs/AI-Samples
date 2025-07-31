from flask import Flask, render_template, request, jsonify, Response, session
import os
import json
import uuid
from backend.chat_service import ChatService
from flask_cors import CORS

app = Flask(__name__, 
           template_folder='frontend/templates',
           static_folder='frontend/static')
CORS(app)

# Secret key for session management
app.secret_key = os.urandom(24)

# Initialize chat service
chat_service = ChatService()

# Store conversation histories (in production, use a database)
conversation_histories = {}

@app.route('/')
def index():
    """Serve the main chat interface"""
    # Generate a unique session ID for the user
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())
        conversation_histories[session['session_id']] = []
    
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Chat endpoint that streams responses from Azure OpenAI
    """
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        # Get or create session
        session_id = session.get('session_id')
        if session_id not in conversation_histories:
            conversation_histories[session_id] = []
        
        # Add user message to conversation history
        user_msg = chat_service.format_user_message(user_message)
        conversation_histories[session_id].append(user_msg)
        
        def generate():
            assistant_response = ""
            try:
                for chunk in chat_service.stream_chat_response(conversation_histories[session_id]):
                    assistant_response += chunk
                    # Send each chunk as Server-Sent Event
                    yield f"data: {json.dumps({'content': chunk, 'type': 'chunk'})}\n\n"
                
                # Add assistant response to conversation history
                assistant_msg = chat_service.format_assistant_message(assistant_response)
                conversation_histories[session_id].append(assistant_msg)
                
                # Send completion signal
                yield f"data: {json.dumps({'type': 'complete'})}\n\n"
                
            except Exception as e:
                yield f"data: {json.dumps({'content': f'Error: {str(e)}', 'type': 'error'})}\n\n"
        
        return Response(
            generate(),
            mimetype='text/plain',
            headers={
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Access-Control-Allow-Origin': '*',
            }
        )
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/clear', methods=['POST'])
def clear_conversation():
    """Clear the conversation history"""
    session_id = session.get('session_id')
    if session_id in conversation_histories:
        conversation_histories[session_id] = []
    return jsonify({'status': 'success'})

@app.route('/api/history')
def get_history():
    """Get conversation history"""
    session_id = session.get('session_id')
    if session_id in conversation_histories:
        return jsonify({'history': conversation_histories[session_id]})
    return jsonify({'history': []})

@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'Flask AI Chat Application'})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
