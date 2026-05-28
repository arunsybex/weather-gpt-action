from fastapi import FastAPI
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

app = FastAPI()

@app.get("/")
async def root():
    return {"ok": True}

app.mount("/mcp", mcp.http_app())
