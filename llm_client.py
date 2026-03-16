# LLM Client abstraction - easily switch between Ollama and Nova
import json
from abc import ABC, abstractmethod
from enum import Enum


class LLMProvider(Enum):
    OLLAMA = "ollama"
    NOVA = "nova"


class BaseLLMClient(ABC):
    """Abstract base class for LLM clients."""
    
    @abstractmethod
    def generate(self, prompt: str, max_tokens: int = 1000, temperature: float = 0.7) -> str:
        """Generate a response from the LLM."""
        pass


class OllamaClient(BaseLLMClient):
    """Ollama LLM client."""
    
    def __init__(self, model: str = "llama3.2", base_url: str = "http://localhost:11434"):
        self.model = model
        self.base_url = base_url
    
    def generate(self, prompt: str, max_tokens: int = 1000, temperature: float = 0.7) -> str:
        import requests
        
        response = requests.post(
            f"{self.base_url}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "num_predict": max_tokens,
                    "temperature": temperature
                }
            },
            timeout=120
        )
        response.raise_for_status()
        return response.json()["response"]


class NovaClient(BaseLLMClient):
    """Amazon Nova LLM client via AWS Bedrock."""
    
    def __init__(self, model_id: str = "amazon.nova-lite-v1:0", region: str = "us-east-1"):
        import boto3
        self.model_id = model_id
        self.client = boto3.client("bedrock-runtime", region_name=region)
    
    def generate(self, prompt: str, max_tokens: int = 1000, temperature: float = 0.7) -> str:
        body = json.dumps({
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": max_tokens,
            "temperature": temperature
        })
        
        response = self.client.invoke_model(
            modelId=self.model_id,
            body=body,
            contentType="application/json"
        )
        
        response_body = json.loads(response["body"].read())
        return response_body["output"]["message"]["content"][0]["text"]


def get_llm_client(provider: LLMProvider = LLMProvider.OLLAMA, **kwargs) -> BaseLLMClient:
    """Factory function to get the appropriate LLM client."""
    
    if provider == LLMProvider.OLLAMA:
        return OllamaClient(**kwargs)
    elif provider == LLMProvider.NOVA:
        return NovaClient(**kwargs)
    else:
        raise ValueError(f"Unknown provider: {provider}")
