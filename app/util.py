from enum import Enum

import openai
from fastapi import HTTPException, status
from pydantic import BaseModel, Field

from app.config import OPENAI_API_KEY, ORGANIZATION_ID


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class TextCompletionModels(str, Enum):
    text_davinci_003 = "text-davinci-003"
    text_curie_001 = "text-curie-001"
    text_babbage_001 = "text-babbage-001"
    text_ada_001 = "text-ada-001"

    def __str__(self):
        return str(self.value)


class Question(BaseModel):
    prompt: str = Field(..., description="Prompt", example="Hello, are you there?")
    model: TextCompletionModels = Field("text-davinci-003", description="Model", example="text-davinci-003")
    suffix: str = Field(None, description="Suffix", example="Hello, are you there?")
    max_tokens: int = Field(150, description="Max tokens", example=150)
    temperature: float = Field(1.0, description="Temperature", example=1.0)
    top_p: float = Field(1, description="Top p", example=1)
    echo: bool = Field(False, description="Echo", example=False)
    stop: list[str] = Field(None, description="Stop", example=None)
    presence_penalty: float = Field(0, description="Presence penalty", example=0)
    frequency_penalty: float = Field(0, description="Frequency penalty", example=0)


def init_openai():
    openai.api_key = OPENAI_API_KEY
    openai.organization = ORGANIZATION_ID


# https://platform.openai.com/docs/models/gpt-3
# supported text completion models
# text-davinci-003, text-curie-001, text-babbage-001, text-ada-001
def request_text_completion(
    prompt: str,
    *,
    model: str = "text-davinci-003",
    suffix: str = None,
    max_tokens: int = 150,
    temperature: float = 1.0,  # 0.0 ~ 2.0
    top_p: float = 1,
    echo: bool = False,
    stop: list[str] = None,
    presence_penalty: float = 0,  # -2.0 ~ 2.0
    frequency_penalty: float = 0,  # -2.0 ~ 2.0
):
    # https://platform.openai.com/docs/api-reference/completions/create#completions/create-model
    try:
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            suffix=suffix,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            echo=echo,
            stop=stop,
            presence_penalty=presence_penalty,
            frequency_penalty=frequency_penalty,
        )
        return response
    except openai.error.AuthenticationError as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


def chat(prompt: str):
    response = request_text_completion(prompt)
    return response.choices[0].text


def chat_with_option(q: Question):
    response = request_text_completion(**q.dict(exclude_none=True))
    return response.choices[0].text


if __name__ == "__main__":
    init_openai()
    prompt = """Can you recommend a programming language?"""
    print(chat(prompt))
