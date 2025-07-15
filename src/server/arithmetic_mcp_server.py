import os
from typing import List, Union
from fastmcp import FastMCP
import arithmetic_functions as calc
from starlette.responses import JSONResponse

mcp = FastMCP("Arithmetic Calculator")

@mcp.custom_route("/health", methods=["GET"])
async def health_endpoint(request):
    """Health check endpoint that returns 200 OK."""
    return JSONResponse({"status": "healthy"}, status_code=200)

@mcp.tool()
async def add(a: float, b: float) -> float:
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b
    """
    return calc.add(a, b)

@mcp.tool()
async def subtract(a: float, b: float) -> float:
    """
    Subtract the second number from the first.
    
    Args:
        a: Number to subtract from
        b: Number to subtract
        
    Returns:
        The difference (a - b)
    """
    return calc.subtract(a, b)

@mcp.tool()
async def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The product of a and b
    """
    return calc.multiply(a, b)

@mcp.tool()
async def divide(a: float, b: float) -> float:
    """
    Divide the first number by the second.
    
    Args:
        a: Dividend (number to be divided)
        b: Divisor (number to divide by)
        
    Returns:
        The quotient (a / b)
        
    Raises:
        ValueError: If attempting to divide by zero
    """
    return calc.divide(a, b)

@mcp.tool()
async def power(base: float, exponent: float) -> float:
    """
    Raise a number to a power.
    
    Args:
        base: The base number
        exponent: The exponent
        
    Returns:
        base raised to the power of exponent
    """
    return calc.power(base, exponent)

@mcp.tool()
async def square_root(number: float) -> float:
    """
    Calculate the square root of a number.
    
    Args:
        number: The number to find the square root of
        
    Returns:
        The square root of the number
        
    Raises:
        ValueError: If the number is negative
    """
    return calc.square_root(number)

@mcp.tool()
async def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.
    
    Args:
        n: Non-negative integer
        
    Returns:
        The factorial of n (n!)
        
    Raises:
        ValueError: If n is negative or not an integer
    """
    return calc.factorial(n)

@mcp.tool()
async def logarithm(number: float, base: float = 2.718281828459045) -> float:
    """
    Calculate the logarithm of a number with specified base.
    
    Args:
        number: The number to find the logarithm of
        base: The base of the logarithm (async default: e for natural log)
        
    Returns:
        The logarithm of number with the specified base
        
    Raises:
        ValueError: If number <= 0 or base <= 0 or base == 1
    """
    return calc.logarithm(number, base)

@mcp.tool()
async def sin(angle: float, degrees: bool = False) -> float:
    """
    Calculate the sine of an angle.
    
    Args:
        angle: The angle
        degrees: If True, angle is in degrees; if False, angle is in radians
        
    Returns:
        The sine of the angle
    """
    return calc.sin(angle, degrees)

@mcp.tool()
async def cos(angle: float, degrees: bool = False) -> float:
    """
    Calculate the cosine of an angle.
    
    Args:
        angle: The angle
        degrees: If True, angle is in degrees; if False, angle is in radians
        
    Returns:
        The cosine of the angle
    """
    return calc.cos(angle, degrees)

@mcp.tool()
async def tan(angle: float, degrees: bool = False) -> float:
    """
    Calculate the tangent of an angle.
    
    Args:
        angle: The angle
        degrees: If True, angle is in degrees; if False, angle is in radians
        
    Returns:
        The tangent of the angle
    """
    return calc.tan(angle, degrees)

@mcp.tool()
async def calculate_mean(numbers: List[float]) -> float:
    """
    Calculate the arithmetic mean (average) of a list of numbers.
    
    Args:
        numbers: List of numbers
        
    Returns:
        The arithmetic mean of the numbers
        
    Raises:
        ValueError: If the list is empty
    """
    return calc.calculate_mean(numbers)

@mcp.tool()
async def calculate_median(numbers: List[float]) -> float:
    """
    Calculate the median of a list of numbers.
    
    Args:
        numbers: List of numbers
        
    Returns:
        The median of the numbers
        
    Raises:
        ValueError: If the list is empty
    """
    return calc.calculate_median(numbers)

@mcp.tool()
async def calculate_mode(numbers: List[float]) -> float:
    """
    Calculate the mode (most common value) of a list of numbers.
    
    Args:
        numbers: List of numbers
        
    Returns:
        The mode of the numbers
        
    Raises:
        ValueError: If the list is empty or has no unique mode
    """
    return calc.calculate_mode(numbers)

@mcp.tool()
async def calculate_standard_deviation(numbers: List[float]) -> float:
    """
    Calculate the standard deviation of a list of numbers.
    
    Args:
        numbers: List of numbers
        
    Returns:
        The standard deviation of the numbers
        
    Raises:
        ValueError: If the list has fewer than 2 elements
    """
    return calc.calculate_standard_deviation(numbers)

@mcp.tool()
async def evaluate_expression(expression: str) -> Union[float, int]:
    """
    Safely evaluate a mathematical expression.
    
    Args:
        expression: Mathematical expression as a string (e.g., "2 + 3 * 4")
        
    Returns:
        The result of the expression
        
    Raises:
        ValueError: If the expression is invalid or contains unsafe operations
    """
    return calc.evaluate_expression(expression)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    mcp.run(transport="http",
            port=port,
            host="0.0.0.0")
