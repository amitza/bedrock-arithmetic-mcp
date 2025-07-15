from dataclasses import dataclass
import os


@dataclass
class ClientConfig:
    mcp_server_url: str = "http://localhost:8000/mcp/"
    aws_region: str = "us-west-2"
    bedrock_model_id: str = "us.anthropic.claude-3-7-sonnet-20250219-v1:0"
    system_prompt: str = ""

def load_config_from_env() -> ClientConfig:
    return ClientConfig(
        mcp_server_url=os.getenv("MCP_SERVER_URL", "http://localhost:8000/mcp/"),
        aws_region=os.getenv("AWS_REGION", "us-west-2"),
        bedrock_model_id=os.getenv("BEDROCK_MODEL_ID", "us.anthropic.claude-3-7-sonnet-20250219-v1:0")
    )