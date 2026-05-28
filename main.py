from fastmcp import FastMCP

mcp = FastMCP("Accords MCP")

@mcp.tool()
async def hello():
    return "hello"
