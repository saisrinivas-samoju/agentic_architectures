"""
Model Context Protocol (MCP) | Agent Protocols

Run with: python 42-mcp.py (uses stdio transport)
Requires: uv pip install mcp
"""

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    print("MCP package not installed. Install with: uv pip install mcp")
    import sys; sys.exit(0)

mcp = FastMCP("weather-service")

WEATHER_DATA = {
    "new york": {"temp": 72, "condition": "Partly Cloudy", "humidity": 65},
    "london": {"temp": 58, "condition": "Rainy", "humidity": 80},
    "tokyo": {"temp": 68, "condition": "Clear", "humidity": 55},
}

@mcp.tool()
def get_weather(city: str) -> str:
    """Get current weather for a city."""
    data = WEATHER_DATA.get(city.lower())
    if not data:
        return f"Weather data not available for '{city}'."
    return f"{city.title()}: {data['temp']}F, {data['condition']}, Humidity: {data['humidity']}%"

@mcp.tool()
def compare_weather(city1: str, city2: str) -> str:
    """Compare weather between two cities."""
    d1, d2 = WEATHER_DATA.get(city1.lower()), WEATHER_DATA.get(city2.lower())
    if not d1 or not d2:
        return "One or both cities not found."
    diff = d1["temp"] - d2["temp"]
    warmer = city1 if diff > 0 else city2
    return f"{city1.title()}: {d1['temp']}F | {city2.title()}: {d2['temp']}F | {warmer.title()} is {abs(diff)}F warmer"

@mcp.resource("weather://cities")
def list_cities() -> str:
    """List all available cities."""
    return ", ".join(c.title() for c in WEATHER_DATA.keys())

if __name__ == "__main__":
    mcp.run()
