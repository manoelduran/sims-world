import os
import json
from google import genai
from google.genai import types
from typing import List, Dict, Any
from ...application.ports.i_llm_service import ILLMService


class GeminiLLMAdapter(ILLMService):
    def __init__(self):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = "gemini-2.5-flash"
        self.embedding_model = "text-embedding-004"

    def invoke(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=[prompt],
        )
        return response.text

    def invoke_json(self, prompt: str) -> Dict[str, Any]:
        generation_config: types.GenerateContentConfigOrDict = {
            "response_mime_type": "application/json"
        }
        response = self.client.models.generate_content(
            model=self.model,
            contents=[prompt],
            config=generation_config,
        )

        try:
            return json.loads(response.text)
        except json.JSONDecodeError:
            raise ValueError(f"Resposta do LLM não foi um JSON válido: {response.text}")

    def generate_embedding(self, text: str) -> List[float]:
        result = self.client.models.embed_content(
            contents=[text],
            model=self.embedding_model,
        )
        return result.embeddings[0].values
