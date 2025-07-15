from typing import List
from contextlib import AsyncExitStack
from strands import Agent
from mcp.client.streamable_http import streamablehttp_client
from strands.tools.mcp.mcp_client import MCPClient
from strands.tools.mcp.mcp_agent_tool import MCPAgentTool
from strands.agent.agent_result import AgentResult
from strands.models import BedrockModel
import boto3
from dotenv import load_dotenv
from client_config import ClientConfig

load_dotenv()


class ArithmeticClient:

    def __init__(self, config: ClientConfig):
        self.config: ClientConfig = config
        self.exit_stack = AsyncExitStack()
        self.agent = Agent()
        self.mcp_client: MCPClient
        self.tools: List[MCPAgentTool] = []

    def init_mcp_client(self) -> None:
        self.mcp_client = MCPClient(lambda: streamablehttp_client(self.config.mcp_server_url))

    def init_list_tools(self) -> None:
        with self.mcp_client:
            self.tools = self.mcp_client.list_tools_sync()
        
    def init_agent(self) -> None:
        with self.mcp_client:
            session = boto3.Session(region_name=self.config.aws_region)

            bedrock_model = BedrockModel(
                    model_id=self.config.bedrock_model_id,
                    boto_session=session
                )
            
            self.agent = Agent(model=bedrock_model,
                            tools=self.tools,
                            system_prompt=self.config.system_prompt)

    def init(self) -> None:
        self.init_mcp_client()
        self.init_list_tools()
        self.init_agent()

    def process_query(self, query: str) -> AgentResult:
        with self.mcp_client:
            response = self.agent(prompt=query)
        return response

    async def stream_query(self, query: str):
        with self.mcp_client:
            async for item in self.agent.stream_async(query):
                yield item

if __name__ == "__main__":
    config = ClientConfig()
    client = ArithmeticClient(config=config)
    client.init()
    print(client.process_query("Hi!"))
