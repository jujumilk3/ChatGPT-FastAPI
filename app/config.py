import os

from dotenv import load_dotenv

load_dotenv()

PROJECT_NAME = "fastapi-gpt3"

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
ORGANIZATION_ID = os.environ.get("ORGANIZATION_ID", "")
