# Personal AI Assistant

A personal AI assistant built with Python, FastAPI, and the OpenAI API.

## Tech Stack

* Python
* FastAPI
* OpenAI Responses API
* Pydantic

## Features

* Chat API
* LLM integration
* System prompt
* Token usage tracking
* Response logging
* Output token limit

## Getting Started

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file:

   ```env
   PORT=8000
   OPENAI_API_KEY=your_api_key
   LLM_MODEL=gpt-6-luna
   ```

4. Start the server:

   ```bash
   python -m app.main
   ```

## API

| Method | Endpoint       | Description                        |
| ------ | -------------- | ---------------------------------- |
| GET    | `/api/health/` | Health check                       |
| POST   | `/api/chat/`   | Send a message to the AI assistant |

Interactive API documentation: `http://localhost:8000/docs`

## Roadmap

* [x] V1 Basic LLM Assistant (core API)
* [ ] V2 Tool Calling
* [ ] V3 Memory
* [ ] V4 RAG
* [ ] V5 AI Agent
* [ ] V6 MCP Integration
* [ ] V7 Multi-Agent System
* [ ] V8 Production Deployment

## License

MIT
