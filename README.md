# Bedrock MCP Workshop: Complete Server & Client Solution

A comprehensive Model Context Protocol (MCP) implementation featuring both server and client components with Amazon Bedrock integration for natural language arithmetic queries.

## 🚀 What This Project Does

This workshop demonstrates a simple complete MCP ecosystem:

- **MCP Server**: Provides mathematical calculation tools via the MCP protocol
- **Bedrock Client**: Connects to Amazon Bedrock for natural language processing of math queries

## 📋 Quick Start

### Prerequisites

- Python 3.13+
- Docker
- AWS CLI configured with permissions

### Run Locally with Docker Compose

```bash
docker-compose up -d --build
```

## 🏗️ Architecture

### Components

1. **MCP Server** (`arithmetic_mcp_server.py`)
   - FastMCP-based server providing mathematical operations
   - Supports basic arithmetic, trigonometry, and statistics
   - Health check endpoints for load balancer integration

2. **Bedrock Client** (`bedrock_mcp_client.py`)
   - Enhanced client with error handling and configuration management
   - Health checks and connection validation
   - Support for environment-based configuration

## 🎯 Usage Examples

For single query

```shell
curl localhost:8001/arithmetic -H "Content-Type: application/json" -d '{ "prompt": "Calculate the triangle area with base 10 and height 5"}' 
```

For streaming single query

```shell
curl -X POST localhost:8001/arithmetic-streaming -N -H "Content-Type: application/json" -d '{ "prompt": "Calculate the triangle area with base 10 and height 5"}'
```