from __future__ import annotations

from fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP(name="Collatz Server", )


@mcp.tool()
def collatz_length(number: int) -> int:
    """
    Return the length of the Collatz sequence starting at `number`,
    including the final 1 in the count.

    Raises:
        ValueError: if `number` is not a positive integer.
    """
    if number <= 0:
        raise ValueError("The input must be positive.")

    n = number
    length = 1  # count the starting number itself

    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        length += 1

    return length


if __name__ == "__main__":
    # Use HTTP transport for network access (recommended)
    # Server will be accessible at http://0.0.0.0:8765/mcp
    mcp.run(transport="http", host="0.0.0.0", port=8765)
