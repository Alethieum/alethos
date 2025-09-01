# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

AlethOS is the operating system for digital AI — powering agents that think, feel, and act autonomously. Built by Alethieum that focuses on making agent coordination and execution lightweight, highly controllable, and easily testable. The framework is built around two primitive abstractions: `Agent`s and **handoffs**.

## Architecture

### Core Components

- **`alethos/core.py`**: Main orchestration engine containing the `AlethOS` class with the `run()` method that handles the agent execution loop
- **`alethos/types.py`**: Core data structures including `Agent`, `Response`, `Result` classes using Pydantic models
- **`alethos/util.py`**: Utility functions for function schema conversion and debugging
- **`alethos/repl/`**: REPL implementation for interactive testing with `run_demo_loop`

### Agent System

Agents are defined with:
- `name`: Agent identifier
- `model`: LLM model (defaults to "gpt-4o")  
- `instructions`: System prompt (string or callable)
- `functions`: List of callable functions the agent can execute
- `tool_choice`: Optional tool selection strategy
- `parallel_tool_calls`: Boolean for parallel function execution

Agents can hand off execution to other agents by returning an `Agent` instance from a function, enabling complex multi-agent workflows.

## Development Commands

### Testing
```bash
# Run all tests
pytest

# Run specific test file  
pytest tests/test_core.py

# Run with debug output
pytest -s tests/
```

### Installation
```bash
# Install from local repository
pip install .

# Install in development mode
pip install -e .

# Install dependencies
pip install -r requirements.txt  # (if requirements file exists in examples)
```

### Examples
Most examples include their own setup:
```bash
# For examples with Makefile (like support_bot)
cd examples/support_bot
make install  # pip3 install -r requirements.txt
make prep     # python3 prep_data.py  
make run      # PYTHONPATH=../.. python3 -m main

# For basic examples
cd examples/basic
python agent_handoff.py
python function_calling.py

# For complex examples with evaluations
cd examples/airline
python evals/function_evals.py
```

### API Configuration
```python
from openai import OpenAI
from alethos import AlethOS

# Configure for Alethieum API
client = OpenAI(
    base_url="https://api.aiwsdao.com/api/v1/",
    api_key="<AIWS_API_KEY>",
)

alethos_client = AlethOS(client=client)
```

### Code Quality
The project uses:
- **autopep8** for code formatting (configured in setup.cfg with max line length 120)
- **pre-commit** hooks (included in dependencies)
- Standard Python imports organization (stdlib, third-party, local)

## Key Patterns

### Function Definition
Functions called by agents should:
- Return strings (values are cast to strings)  
- Return `Agent` instances for handoffs
- Return `Result` objects for complex responses with context variable updates
- Accept `context_variables` parameter if needed for accessing shared state

### Context Variables
Shared state between agents using dictionary that persists across agent handoffs and function calls.

### Response Handling
The `client.run()` method returns a `Response` object containing:
- `messages`: Conversation history with sender attribution
- `agent`: Last active agent
- `context_variables`: Updated shared state

### Recommended Models
For use with Alethieum API, recommended models:
- `aiws/gpt-oss-20b`: High-performance open-source model
- Set model in Agent constructor: `Agent(model="aiws/gpt-oss-20b")`

### Streaming Support
Enable streaming responses with `stream=True` parameter. The framework supports Chat Completions API streaming events plus custom delimiters for agent switches.

## Project Structure

- `/examples/`: Comprehensive examples from basic usage to complex multi-agent systems
- `/alethos/`: Core framework code
- `/tests/`: Test suite with mock clients and core functionality tests  
- `/logs/`: Session logs for debugging and analysis