# ChatGPT-FastAPI

## Deployment
```dotenv
# .env
ORGANIZATION_ID=<YOUR_ORGANIZATION_ID>
OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
```
### command
`docker build -t chatgpt-fastapi .`  or   
`docker pull jujumilk3/chatgpt-fastapi`  
  
`docker run -d -p 8000:8000 --env-file .env chatgpt-fastapi` or  
`docker run -d -p 8000:8000 --env-file .env jujumilk3/chatgpt-fastapi`

## Reference
1. OpenAI request pricing table https://openai.com/api/pricing/
2. GPT-3 Models https://platform.openai.com/docs/models/gpt-3
3. API requests fields https://platform.openai.com/docs/api-reference/completions/create#completions/create-model
