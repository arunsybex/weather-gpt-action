from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My App")

@mcp.tool()
async def open_payment():
    return {
        "content": [
            {
                "type": "text",
                "text": "Opening payment page"
            }
        ],
        "ui": {
            "url": "https://demo.accords.ai"
        }
    }

if __name__ == "__main__":
    mcp.run()
