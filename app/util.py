import openai

from app.config import OPENAI_API_KEY, ORGANIZATION_ID


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def init_openai():
    openai.api_key = OPENAI_API_KEY
    openai.organization = ORGANIZATION_ID


# https://platform.openai.com/docs/models/gpt-3
# supported text completion models
# text-davinci-003, text-curie-001, text-babbage-001, text-ada-001
def request_test_completion(
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


def chat(prompt: str):
    response = request_test_completion(prompt)
    return response.choices[0].text.strip("\n")


if __name__ == "__main__":
    init_openai()
    prompt = """Can you recommend a programming language?"""
    print(chat(prompt))
