# MCP Server Dev Deploy

A Model Context Protocol (MCP) server implementation featuring arithmetic operations, designed for deployment and integration with AI assistants like Claude Dev (Cline) and other MCP-compatible clients.

## Overview

This project provides a complete MCP server that implements basic arithmetic operations including addition, subtraction, multiplication, division, power, and square functions. The server uses the FastMCP framework for easy development and deployment.

## Features

- **Arithmetic Operations**: Add, subtract, multiply, divide, power, and square operations
- **MCP Protocol Support**: Full compatibility with MCP 1.13.1+
- **Easy Deployment**: Simple configuration for AI assistants
- **Type Safety**: Fully typed Python implementation
- **Extensible**: Easy to add new tools and functions

## Project Structure

```
mcp-server-dev-deploy/
├── src/
│   └── mcpserver/
│       ├── __init__.py
│       ├── __main__.py          # Main entry point
│       └── deployment.py        # MCP server implementation
├── main.py                      # Alternative entry point
├── pyproject.toml              # Project configuration
├── README.md                   # This file

```

## Available Tools

The MCP server provides the following arithmetic tools:

### `add(a: int, b: int) -> int`
Add two integers together.

### `subtract(a: int, b: int) -> int`
Subtract the second integer from the first.

### `multiply(a: int, b: int) -> int`
Multiply two integers together.

### `divide(a: int, b: int) -> float`
Divide the first integer by the second.

### `power(a: int, b: int) -> int`
Raise the first integer to the power of the second.

### `square(a: int) -> int`
Square the given integer.

## Installation

### Prerequisites

- Python 3.10 or higher
- UV package manager (recommended) or pip

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/codesnippetsforall/mcpserverarithmeticoperation.git
cd mcpserverarithmeticoperation
```

2. Install dependencies:
```bash
uv sync
```

3. Run the server locally:
```bash
uv run mcp-server
```

### Quick Start (No Clone Required)

You can run this MCP server directly from GitHub without cloning the repository:

```bash
uvx --from git+https://github.com/codesnippetsforall/mcpserverarithmeticoperation.git mcp-server
```

This command will:
- Download the project directly from GitHub
- Install all dependencies automatically  
- Run the MCP server immediately
- Work on any system with UV installed

## Configuration for AI Assistants

### Claude Dev (Cline) Configuration

To use this MCP server with Claude Dev (Cline), add the following configuration to your Cline MCP settings file:

**File Location**: `%APPDATA%\Roaming\Cursor\User\globalStorage\saoudrizwan.claude-dev\settings\cline_mcp_settings.json`

```json
{
  "mcpServers": {
    "mcp-server-dev-deploy": {
      "command": "uvx",
      "args": [
        "--from", 
        "git+https://github.com/codesnippetsforall/mcpserverarithmeticoperation.git",
        "mcp-server"
      ]
    }
  }
}
```

### Alternative Local Configuration

If you have the project cloned locally:

```json
{
  "mcpServers": {
    "mcp-server-dev-deploy": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "D:/learning/mcp/mcp-server-dev-deploy",
        "mcp-server"
      ]
    }
  }
}
```

### General MCP Client Configuration

For other MCP clients, use the following configuration format:

```json
{
  "mcpServers": {
    "arithmetic-server": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/codesnippetsforall/mcpserverarithmeticoperation.git",
        "mcp-server"
      ]
    }
  }
}
```

## Usage Examples

Once configured with your AI assistant, you can use the arithmetic operations:

```
User: "Add 15 and 27"
Assistant: I'll add 15 and 27 for you.
Result: 42

User: "What's 8 squared?"
Assistant: I'll calculate 8 squared.
Result: 64

User: "Divide 100 by 4"
Assistant: I'll divide 100 by 4.
Result: 25.0
```

## Development

### Adding New Tools

To add new arithmetic operations, edit `src/mcpserver/deployment.py`:

```python
@mcp.tool()
def your_new_function(param: int) -> int:
    """Description of your function.
    
    Args:
        param (int): Parameter description
        
    Returns:
        int: Return value description
    """
    return your_calculation
```

### Testing Locally

Run the server in development mode:

```bash
uv run python -m mcpserver
```

### Building for Distribution

The project uses setuptools for building:

```bash
uv build
```

## Dependencies

- **mcp[cli]**: Model Context Protocol implementation (≥1.13.1)
- **Python**: ≥3.10

## Configuration Files

### pyproject.toml
Contains project metadata, dependencies, and build configuration.

### uv.lock
Locks specific versions of dependencies for reproducible builds.

## Troubleshooting

### Common Issues

1. **Server not starting**: Ensure Python 3.10+ is installed and UV is available
2. **Configuration not loaded**: Check the JSON syntax in your MCP settings file
3. **Tools not available**: Verify the server is running and properly configured

### Debug Mode

Run with debug output:

```bash
uv run mcp-server --debug
```

*This MCP server is designed to demonstrate arithmetic operations and serve as a template for more complex MCP implementations.*
