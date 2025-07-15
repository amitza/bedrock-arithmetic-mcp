import logging
import os
from fastapi import FastAPI
from pydantic import BaseModel

from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse, PlainTextResponse
from pydantic import BaseModel
import uvicorn
import os

from bedrock_mcp_client import ArithmeticClient
from client_config import load_config_from_env


logger = logging.getLogger(__name__)

app = FastAPI(title="Arithmetic API")

SYSTEM_PROMPT = ""


class PromptRequest(BaseModel):
    prompt: str

@app.get('/health')
def health_check():
    """Health check endpoint for the load balancer."""
    return {"status": "healthy"}


@app.post('/arithmetic')
async def get_arithmetic(request: PromptRequest):
    prompt = request.prompt
    
    if not prompt:
        raise HTTPException(status_code=400, detail="No prompt provided")

    try:
        config = load_config_from_env()
        client = ArithmeticClient(config=config)
        client.init()
        response = client.process_query(query=prompt)
        
        content = str(response)
        return PlainTextResponse(content=content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def run_agent_and_stream_response(prompt: str):
    config = load_config_from_env()
    client = ArithmeticClient(config=config)
    client.init()

    async for item in client.stream_query(prompt):
        if "data" in item:
            yield item['data']

@app.post('/arithmetic-streaming')
async def get_arithmetic_streaming(request: PromptRequest):
    try:
        prompt = request.prompt

        if not prompt:
            raise HTTPException(status_code=400, detail="No prompt provided")

        return StreamingResponse(
            run_agent_and_stream_response(prompt),
            media_type="text/plain"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8001))
    uvicorn.run(app, host='0.0.0.0', port=port)