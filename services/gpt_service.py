import os
from openai import AzureOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


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
        messages = []
        
        # Add conversation history if provided
        if conversation_history:
            messages.extend(conversation_history)
        
        # Add current user message
        messages.append({"role": "user", "content": user_message})
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Error getting GPT response: {str(e)}")
