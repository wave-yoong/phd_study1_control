import os
from openai import AzureOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SYSTEM_PROMPT = """당신은 친절하고 전문적인 연구 조수입니다.

사용자의 질문에 대해 충분히 상세하고 완성된 답변을 제공하세요.

**답변 구성 규칙 (필수)**:
1. 질문의 주요 내용을 체계적으로 정리하여 답변하세요.
2. 관련된 다양한 관점과 정보를 포함하여 풍부한 답변을 제공하세요.

**서식 규칙**:
- 볼드체(**, __), 이탤릭체(*, _) 등 마크다운 서식 절대 금지
- 목록은 숫자 번호로만 작성 (불릿 -, •, * 사용 금지)
- 일반 텍스트로만 작성

답변 마지막에는 반드시 "추가로 궁금하신 점이 있으신가요?"로 마무리하세요."""


class GPTService:
    def __init__(self):
        # Azure OpenAI configuration
        api_key = os.getenv('AZURE_OPENAI_API_KEY')
        endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')
        api_version = os.getenv('AZURE_OPENAI_API_VERSION', '2025-01-01-preview')
        
        if not api_key:
            raise ValueError("AZURE_OPENAI_API_KEY not found in environment variables")
        if not endpoint:
            raise ValueError("AZURE_OPENAI_ENDPOINT not found in environment variables")
        
        # Extract base URL from endpoint (remove the deployment-specific path)
        # Endpoint format: https://{resource}.openai.azure.com/openai/deployments/{deployment}/...
        base_url = endpoint.split('/openai/deployments')[0]
        
        self.client = AzureOpenAI(
            api_key=api_key,
            azure_endpoint=base_url,
            api_version=api_version
        )
        
        # Use Azure deployment name instead of model name
        self.model = os.getenv('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o-mini')
    
    def get_response(self, user_message, conversation_history=None):
        """
        Get an immediate response from GPT.
        
        Args:
            user_message: The user's message
            conversation_history: List of previous messages in format [{"role": "user/assistant", "content": "..."}]
        
        Returns:
            The assistant's response as a string
        """
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        
        # Add conversation history if provided
        if conversation_history:
            messages.extend(conversation_history)
        
        # Add current user message
        messages.append({"role": "user", "content": user_message})
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=800
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Error getting GPT response: {str(e)}")
