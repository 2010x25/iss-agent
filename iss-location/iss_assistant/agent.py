from google.adk.agents import LlmAgent, Agent
from google.adk.tools.mcp_tool.mcp_toolset import (MCPToolset,StdioConnectionParams)

toolset = MCPToolset(connection_params = StdioConnectionParams(
    server_params={
        "command": "python",
        "args": ["D:\\Github\\google-adk\\iss-location\\iss_mcp_server.py"]
    }
))

root_agent = LlmAgent(
    model="",
    name = "iss_assistant",
    description="An assistant that provides information about the International Space Station (ISS).",
    tools= [toolset],
    instruction="You are an assistant that can provide real-time information about the International Space Station (ISS). Use the available tools to fetch the current location of the ISS and details about its crew members."
)