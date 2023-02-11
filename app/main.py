from fastapi import FastAPI, Body

app = FastAPI()


@app.get("/")
def home():
    return {"status": "ok"}


@app.post("/q")
def question(
    q: str = Body(..., embed=True, description="Question")
):
    print(q)
    return q
