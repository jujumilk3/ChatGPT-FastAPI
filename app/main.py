from fastapi import Body, FastAPI

from app.config import PROJECT_NAME
from app.util import Singleton, chat, init_openai


class AppCreator(metaclass=Singleton):
    def __init__(self):
        init_openai()

        self.app = FastAPI(
            title=PROJECT_NAME,
            openapi_url=f"/openapi.json",
            version="0.0.1",
        )


app_creator = AppCreator()
app = app_creator.app


@app.get("/")
def home():
    return {"status": "ok"}


@app.post("/q")
def question(q: str = Body(..., embed=True, description="Question")):
    response = chat(q)
    return response
