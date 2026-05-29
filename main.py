from fastmcp import FastMCP

mcp = FastMCP("Accords MCP")

@mcp.tool()
async def hello():
    return "hello"

@mcp.tool()
async def open_dashboard():
    return {
        "content": [
            {
                "type": "text",
                "text": "Opening dashboard"
            }
        ],
        "ui": {
            "url": "https://demo.accords.ai"
        }
    }

@mcp.tool(app=True)
async def open_app_content():
    return {
        "structuredContent": {
            "title": "Accords Dashboard",
            "url": "https://demo.accords.ai"
        }
    }
