# ChatGPT-FastAPI

## Deployment
```dotenv
# .env
ORGANIZATION_ID=<YOUR_ORGANIZATION_ID>
OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
```
### command
`docker build -t fastapi-gpt3 .`  or   
`docker pull jujumilk3/fastapi-gpt3`  
  
`docker run -d -p 8000:8000 --env-file .env fastapi-gpt3` or  
`docker run -d -p 8000:8000 --env-file .env jujumilk3/fastapi-gpt3`

## Reference
1. OpenAI request pricing table https://openai.com/api/pricing/
2. GPT-3 Models https://platform.openai.com/docs/models/gpt-3
3. API requests fields https://platform.openai.com/docs/api-reference/completions/create#completions/create-model
