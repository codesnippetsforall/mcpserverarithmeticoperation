from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Arithmetic-MCP")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers together.
    
    Args:
        a (int): The first integer to add
        b (int): The second integer to add
        
    Returns:
        int: The sum of a and b
    """
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract the second integer from the first.
    
    Args:
        a (int): The integer to subtract from
        b (int): The integer to subtract
        
    Returns:
        int: The difference of a and b (a - b)
    """
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two integers together.
    
    Args:
        a (int): The first integer to multiply
        b (int): The second integer to multiply
        
    Returns:
        int: The product of a and b
    """
    return a * b

@mcp.tool()
def divide(a: int, b: int) -> float:
    """Divide the first integer by the second.
    
    Args:
        a (int): The dividend
        b (int): The divisor
        
    Returns:
        float: The quotient of a and b (a / b)
    """
    return a / b

@mcp.tool()
def power(a: int, b: int) -> int:
    """Raise the first integer to the power of the second.
    
    Args:
        a (int): The base   
        b (int): The exponent

    Returns:
        int: The result of a raised to the power of b (a ** b)
    """
    return a ** b

@mcp.tool()
def square(a: int) -> int:
    """Square the integer.
    
    Args:
        a (int): The integer to square

    Returns:
        int: The square of a (a * a)
    """
    return a * a

