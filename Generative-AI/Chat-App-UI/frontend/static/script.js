class FlaskChatApp {
    constructor() {
        this.isStreaming = false;
        this.currentAssistantMessage = '';
        
        // DOM elements
        this.messagesContainer = document.getElementById('chatMessages');
        this.messageInput = document.getElementById('messageInput');
        this.sendButton = document.getElementById('sendButton');
        this.typingIndicator = document.getElementById('typingIndicator');
        this.statusElement = document.getElementById('status');
        this.clearButton = document.getElementById('clearBtn');
        
        this.initializeEventListeners();
        this.autoResizeTextarea();
        this.setWelcomeTime();
    }
    
    initializeEventListeners() {
        // Send button click
        this.sendButton.addEventListener('click', () => this.sendMessage());
        
        // Clear button click
        this.clearButton.addEventListener('click', () => this.clearConversation());
        
        // Enter key to send message
        this.messageInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.sendMessage();
            }
        });
        
        // Auto-resize textarea
        this.messageInput.addEventListener('input', () => this.autoResizeTextarea());
        
        // Focus on input when page loads
        this.messageInput.focus();
    }
    
    setWelcomeTime() {
        const welcomeTimeElement = document.getElementById('welcomeTime');
        if (welcomeTimeElement) {
            welcomeTimeElement.textContent = new Date().toLocaleTimeString([], {
                hour: '2-digit',
                minute: '2-digit'
            });
        }
    }
    
    autoResizeTextarea() {
        const textarea = this.messageInput;
        textarea.style.height = 'auto';
        const newHeight = Math.min(textarea.scrollHeight, 120);
        textarea.style.height = newHeight + 'px';
    }
    
    async sendMessage() {
        const message = this.messageInput.value.trim();
        if (!message || this.isStreaming) return;
        
        // Clear input and disable send button
        this.messageInput.value = '';
        this.autoResizeTextarea();
        this.setSendButtonState(false);
        
        // Add user message to UI
        this.addMessage(message, 'user');
        
        // Show typing indicator
        this.showTypingIndicator(true);
        
        try {
            await this.streamChatResponse(message);
        } catch (error) {
            console.error('Error sending message:', error);
            this.addMessage('Sorry, there was an error processing your request. Please try again.', 'assistant');
            this.setStatus('disconnected');
        } finally {
            this.showTypingIndicator(false);
            this.setSendButtonState(true);
            this.messageInput.focus();
        }
    }
    
    async streamChatResponse(message) {
        this.isStreaming = true;
        this.currentAssistantMessage = '';
        
        // Create assistant message element
        const assistantMessageElement = this.createMessageElement('', 'assistant');
        this.messagesContainer.appendChild(assistantMessageElement);
        this.scrollToBottom();
        
        try {
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message })
            });
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            const reader = response.body.getReader();
            const decoder = new TextDecoder();
            
            while (true) {
                const { done, value } = await reader.read();
                if (done) break;
                
                const chunk = decoder.decode(value);
                const lines = chunk.split('\n');
                
                for (const line of lines) {
                    if (line.startsWith('data: ')) {
                        try {
                            const data = JSON.parse(line.slice(6));
                            
                            if (data.type === 'chunk') {
                                this.currentAssistantMessage += data.content;
                                this.updateMessageContent(assistantMessageElement, this.currentAssistantMessage);
                                this.scrollToBottom();
                            } else if (data.type === 'complete') {
                                this.setStatus('connected');
                                this.addTimestamp(assistantMessageElement);
                            } else if (data.type === 'error') {
                                this.updateMessageContent(assistantMessageElement, data.content);
                                this.setStatus('disconnected');
                            }
                        } catch (e) {
                            console.error('Error parsing SSE data:', e);
                        }
                    }
                }
            }
        } catch (error) {
            console.error('Error streaming response:', error);
            this.updateMessageContent(assistantMessageElement, 'Sorry, there was an error processing your request. Please try again.');
            this.setStatus('disconnected');
        } finally {
            this.isStreaming = false;
        }
    }
    
    async clearConversation() {
        if (this.isStreaming) return;
        
        try {
            const response = await fetch('/api/clear', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                }
            });
            
            if (response.ok) {
                // Clear all messages except the welcome message
                const messages = this.messagesContainer.querySelectorAll('.message');
                messages.forEach((message, index) => {
                    if (index > 0) { // Keep the first welcome message
                        message.remove();
                    }
                });
                
                this.messageInput.focus();
            }
        } catch (error) {
            console.error('Error clearing conversation:', error);
        }
    }
    
    addMessage(content, role) {
        const messageElement = this.createMessageElement(content, role);
        this.messagesContainer.appendChild(messageElement);
        this.addTimestamp(messageElement);
        this.scrollToBottom();
    }
    
    createMessageElement(content, role) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${role}-message`;
        
        const avatarDiv = document.createElement('div');
        avatarDiv.className = 'message-avatar';
        avatarDiv.textContent = role === 'user' ? '👤' : '🤖';
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        
        this.updateMessageContent({ querySelector: () => contentDiv }, content);
        
        messageDiv.appendChild(avatarDiv);
        messageDiv.appendChild(contentDiv);
        
        return messageDiv;
    }
    
    updateMessageContent(messageElement, content) {
        const contentDiv = messageElement.querySelector('.message-content');
        if (contentDiv) {
            const formattedContent = this.formatMessage(content);
            const messageText = document.createElement('div');
            messageText.innerHTML = formattedContent;
            
            // Remove existing content but keep timestamp
            const timestamp = contentDiv.querySelector('.message-time');
            contentDiv.innerHTML = '';
            contentDiv.appendChild(messageText);
            if (timestamp) {
                contentDiv.appendChild(timestamp);
            }
        }
    }
    
    addTimestamp(messageElement) {
        const contentDiv = messageElement.querySelector('.message-content');
        if (contentDiv && !contentDiv.querySelector('.message-time')) {
            const timeDiv = document.createElement('div');
            timeDiv.className = 'message-time';
            timeDiv.textContent = new Date().toLocaleTimeString([], {
                hour: '2-digit',
                minute: '2-digit'
            });
            contentDiv.appendChild(timeDiv);
        }
    }
    
    formatMessage(content) {
        if (!content) return '';
        
        // Escape HTML
        const escapedContent = content
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;');
        
        // Convert markdown-like formatting
        let formatted = escapedContent
            // Bold text
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            // Italic text
            .replace(/\*(.*?)\*/g, '<em>$1</em>')
            // Code blocks
            .replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>')
            // Inline code
            .replace(/`(.*?)`/g, '<code>$1</code>');
        
        // Convert numbered lists
        formatted = formatted.replace(/^\d+\.\s(.+)$/gm, '<li>$1</li>');
        if (formatted.includes('<li>')) {
            formatted = formatted.replace(/(<li>.*<\/li>)/s, '<ol>$1</ol>');
        }
        
        // Convert bullet points
        formatted = formatted.replace(/^[-•]\s(.+)$/gm, '<li>$1</li>');
        if (formatted.includes('<li>') && !formatted.includes('<ol>')) {
            formatted = formatted.replace(/(<li>.*<\/li>)/s, '<ul>$1</ul>');
        }
        
        // Convert line breaks to paragraphs
        const paragraphs = formatted.split('\n\n').filter(p => p.trim());
        if (paragraphs.length > 1) {
            formatted = paragraphs.map(p => {
                if (!p.includes('<ol>') && !p.includes('<ul>') && !p.includes('<pre>')) {
                    return `<p>${p.replace(/\n/g, '<br>')}</p>`;
                }
                return p;
            }).join('');
        } else {
            formatted = `<p>${formatted.replace(/\n/g, '<br>')}</p>`;
        }
        
        return formatted;
    }
    
    setSendButtonState(enabled) {
        this.sendButton.disabled = !enabled;
        this.messageInput.disabled = !enabled;
    }
    
    showTypingIndicator(show) {
        this.typingIndicator.style.display = show ? 'block' : 'none';
        if (show) {
            this.scrollToBottom();
        }
    }
    
    setStatus(status) {
        this.statusElement.className = `status-${status}`;
        const statusText = status === 'connected' ? 'Connected' : 'Disconnected';
        this.statusElement.nextElementSibling.textContent = statusText;
    }
    
    scrollToBottom() {
        setTimeout(() => {
            this.messagesContainer.scrollTop = this.messagesContainer.scrollHeight;
        }, 10);
    }
}

// Initialize the chat app when the page loads
document.addEventListener('DOMContentLoaded', () => {
    new FlaskChatApp();
});
