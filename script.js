// Control Group Chatbot - Direct Response (No intermediate steps)
class ChatBot {
    constructor() {
        this.chatMessages = document.getElementById('chatMessages');
        this.userInput = document.getElementById('userInput');
        this.sendButton = document.getElementById('sendButton');
        
        this.init();
    }
    
    init() {
        // Event listeners
        this.sendButton.addEventListener('click', () => this.handleSend());
        this.userInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.handleSend();
            }
        });
        
        // Auto-resize textarea
        this.userInput.addEventListener('input', () => {
            this.userInput.style.height = 'auto';
            this.userInput.style.height = this.userInput.scrollHeight + 'px';
        });
    }
    
    handleSend() {
        const message = this.userInput.value.trim();
        if (!message) return;
        
        // Add user message
        this.addMessage(message, 'user');
        
        // Clear input
        this.userInput.value = '';
        this.userInput.style.height = 'auto';
        
        // Disable input while processing
        this.setInputState(false);
        
        // Show typing indicator
        const typingId = this.showTypingIndicator();
        
        // Simulate bot response (Control Group: Direct response)
        setTimeout(() => {
            this.removeTypingIndicator(typingId);
            this.generateBotResponse(message);
            this.setInputState(true);
            this.userInput.focus();
        }, 1500);
    }
    
    generateBotResponse(userMessage) {
        // Control Group: Direct response without intermediate steps
        // This simulates an AI that directly provides information
        
        let response = '';
        
        // Simple response logic for demonstration
        if (userMessage.includes('안녕') || userMessage.includes('hello') || userMessage.includes('hi')) {
            response = '안녕하세요! 무엇을 도와드릴까요?';
        } else if (userMessage.includes('이름') || userMessage.includes('name')) {
            response = '저는 AI 연구 어시스턴트입니다. PhD Study 1의 컨트롤 그룹 챗봇으로, 사용자의 질문에 직접 응답하는 방식으로 작동합니다.';
        } else if (userMessage.includes('기후변화') || userMessage.includes('climate change')) {
            response = `기후변화에 대한 정보를 제공해드리겠습니다.

기후변화는 장기간에 걸친 기온, 강수량, 기타 기상 패턴의 중요한 변화를 의미합니다. 주요 원인은 다음과 같습니다:

1. 온실가스 배출 증가 (CO2, 메탄 등)
2. 산림 파괴 및 토지 이용 변화
3. 산업화 및 화석 연료 사용

주요 영향:
- 해수면 상승
- 극한 기상 현상 증가
- 생태계 변화
- 농업 생산성 변화

이러한 정보는 IPCC 보고서, 과학 논문, 정부 기관 자료 등을 종합한 것입니다.`;
        } else if (userMessage.includes('인공지능') || userMessage.includes('AI') || userMessage.includes('머신러닝')) {
            response = `인공지능(AI)에 대해 설명드리겠습니다.

인공지능은 인간의 학습능력, 추론능력, 지각능력을 인공적으로 구현한 컴퓨터 시스템입니다.

주요 분야:
1. 머신러닝 (Machine Learning)
   - 지도학습, 비지도학습, 강화학습
   
2. 딥러닝 (Deep Learning)
   - 신경망 기반 학습
   - 이미지 인식, 자연어 처리 등
   
3. 자연어 처리 (NLP)
   - 텍스트 이해 및 생성
   - 번역, 요약, 질의응답

4. 컴퓨터 비전
   - 이미지/영상 분석
   - 객체 인식 및 추적

현재 AI는 의료, 금융, 교육, 교통 등 다양한 분야에서 활용되고 있습니다.`;
        } else {
            response = `"${userMessage}"에 대한 정보를 제공해드리겠습니다.

귀하의 질문과 관련된 정보를 다양한 출처(학술 논문, 신뢰할 수 있는 웹사이트, 공식 보고서 등)에서 종합하여 분석했습니다.

주요 내용:
1. 개념 및 정의
2. 현재 동향 및 상황
3. 관련 연구 및 자료
4. 실용적 적용 사례

더 구체적인 정보가 필요하시면 질문을 더 상세히 해주시면 도움을 드리겠습니다.

참고: 이는 컨트롤 그룹 챗봇으로, 질문에 대해 직접적인 응답을 제공하는 방식으로 작동합니다.`;
        }
        
        this.addMessage(response, 'bot');
    }
    
    addMessage(text, type) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${type}-message`;
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        contentDiv.innerHTML = `<p>${this.formatMessage(text)}</p>`;
        
        const timeDiv = document.createElement('div');
        timeDiv.className = 'message-time';
        timeDiv.textContent = this.getCurrentTime();
        
        messageDiv.appendChild(contentDiv);
        messageDiv.appendChild(timeDiv);
        this.chatMessages.appendChild(messageDiv);
        
        // Scroll to bottom
        this.scrollToBottom();
    }
    
    formatMessage(text) {
        // Convert newlines to <br> and preserve formatting
        return text.replace(/\n/g, '<br>');
    }
    
    showTypingIndicator() {
        const typingDiv = document.createElement('div');
        typingDiv.className = 'message bot-message';
        const typingId = 'typing-' + Date.now();
        typingDiv.id = typingId;
        
        const indicator = document.createElement('div');
        indicator.className = 'typing-indicator';
        indicator.innerHTML = '<span></span><span></span><span></span>';
        
        typingDiv.appendChild(indicator);
        this.chatMessages.appendChild(typingDiv);
        this.scrollToBottom();
        
        return typingId;
    }
    
    removeTypingIndicator(typingId) {
        const element = document.getElementById(typingId);
        if (element) {
            element.remove();
        }
    }
    
    setInputState(enabled) {
        this.userInput.disabled = !enabled;
        this.sendButton.disabled = !enabled;
    }
    
    scrollToBottom() {
        this.chatMessages.scrollTop = this.chatMessages.scrollHeight;
    }
    
    getCurrentTime() {
        const now = new Date();
        return now.toLocaleTimeString('ko-KR', { 
            hour: '2-digit', 
            minute: '2-digit' 
        });
    }
}

// Initialize chatbot when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    new ChatBot();
});
