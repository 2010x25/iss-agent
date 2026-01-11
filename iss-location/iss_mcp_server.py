from fastmcp import FastMCP 
import requests
mcp = FastMCP(name = "ISS Location")
@mcp.tool()
def get_iss_location():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    return response.json()

@mcp.tool()
def get_iss_crew():
    response = requests.get("http://api.open-notify.org/astros.json")
    return response.json()

if __name__ == "__main__":
    mcp.run(transport="stdio")