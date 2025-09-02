# AlethOS - Alethieum Neural OS

**AlethOS is the operating system for digital AI — powering agents that think, feel, and act autonomously.**

Built by Alethieum, AlethOS provides the foundational infrastructure for creating intelligent agent ecosystems that can collaborate, make decisions, and evolve independently. More than just a framework, AlethOS is designed to be the neural foundation upon which the future of autonomous AI is built.

## Install

Requires Python 3.10+

### Option 1: Install from GitHub (Recommended)

```shell
pip install git+https://github.com/alethieum/alethos.git
```

### Option 2: Install from SSH

```shell
pip install git+ssh://git@github.com/alethieum/alethos.git
```

### Option 3: Development Installation

```shell
git clone https://github.com/alethieum/alethos.git
cd alethos
pip install -e .
```

## AIWS: Recommended Infrastructure for Autonomous AI

AlethOS works with any AI provider, but we recommend AIWS (AI Web Services) - a decentralized AI infrastructure platform designed specifically for the autonomous agent economy.

**AIWS Agent Intelligence Gateway** provides seamless access to diverse AI models through a unified API, making it the ideal infrastructure choice for AlethOS agents that need to independently select and utilize optimal intelligence capabilities.

### Key Features

**Universal AI Access**: Single API endpoint for 23+ models with more being added continuously

**Agent-First Design**: Purpose-built for autonomous AI agents and agentic workflows  

**Decentralized Infrastructure**: Models deployed across distributed node network

**Economic Autonomy**: AI agents can independently select and pay for optimal models

**Permissionless Integration**: No gatekeepers - agents choose their own intelligence stack

### Get Started with AIWS (Recommended)

1. **Get your API key**: Visit [https://www.aiwsdao.com/](https://www.aiwsdao.com/)
2. **Single endpoint**: `https://api.aiwsdao.com/v1/`  
3. **23+ models**: Access leading open and closed source models
4. **Built for agents**: Optimized for autonomous AI workflows

*Note: AlethOS also works with OpenAI, Anthropic, or any OpenAI-compatible API provider.*

## Quick Start

### 1. Set up your API key

After installation, copy the environment template and add your API key:

```shell
cp .env.example .env
# Edit .env and add your AIWS_API_KEY
```

Or set the environment variable directly:
```shell
export AIWS_API_KEY=your_api_key_here
```

### 2. Basic Usage

```python
from alethos import AlethOS, Agent

# AlethOS will automatically use your .env configuration
client = AlethOS()

# Create agents (model will default to aiws/gpt-oss-20b from .env)
agent = Agent(
    name="AlethOS Assistant",
    instructions="You are a helpful AI assistant powered by AlethOS.",
)

# Run a conversation
response = client.run(
    agent=agent,
    messages=[{"role": "user", "content": "Hello! What can you do?"}],
)

print(response.messages[-1]["content"])
```

### 3. Advanced Configuration

For custom API configurations:

```python
from alethos import AlethOS, get_default_client
from openai import OpenAI

# Option 1: Use automatic configuration
client = AlethOS()  # Uses .env file

# Option 2: Custom configuration
custom_client = OpenAI(
    base_url="https://api.aiwsdao.com/v1/",
    api_key="your_api_key_here"
)
alethos = AlethOS(client=custom_client)
```

### 4. Interactive Demo

Try the interactive demo:

```python
from alethos.repl import run_demo_loop
from alethos import Agent, AlethOS

client = AlethOS()
agent = Agent(
    name="Demo Agent",
    instructions="You are a helpful assistant for demonstrating AlethOS capabilities."
)

run_demo_loop(agent, stream=True)
```

## See AlethOS in Action: Autonomous Coffee Shop Manager

Experience the power of AlethOS with this interactive demo that showcases autonomous agents managing real business logic.

### Coffee Inventory Demo

This demo creates an AI agent that can autonomously manage a coffee shop inventory system, understanding natural language and making intelligent decisions about when to check stock, update quantities, and respond to customer inquiries.

```python
from alethos import AlethOS, Agent

# Coffee inventory database (simulated)
coffee_inventory = {
    "espresso": 25,
    "americano": 18,
    "latte": 12,
    "cappuccino": 15,
    "mocha": 8
}

# Agent functions
def check_inventory(coffee_type=None):
    """Check coffee cup inventory"""
    if coffee_type:
        coffee_type = coffee_type.lower()
        if coffee_type in coffee_inventory:
            count = coffee_inventory[coffee_type]
            return f"We have {count} {coffee_type} cups in stock"
        else:
            return f"Sorry, we don't carry {coffee_type}"
    else:
        inventory_list = []
        for coffee, count in coffee_inventory.items():
            inventory_list.append(f"{coffee}: {count} cups")
        return "Current inventory:\n" + "\n".join(inventory_list)

def update_inventory(coffee_type, quantity):
    """Update coffee inventory"""
    coffee_type = coffee_type.lower()
    if coffee_type in coffee_inventory:
        coffee_inventory[coffee_type] = int(quantity)
        return f"Updated {coffee_type} inventory to {quantity} cups"
    else:
        return f"Cannot update - we don't carry {coffee_type}"

# Create AlethOS and coffee agent
client = AlethOS()

coffee_agent = Agent(
    name="Coffee Inventory Manager",
    instructions="""You are a coffee shop inventory manager running on AlethOS. 
    You can check and update coffee cup inventory. Be friendly and helpful!
    
    Available coffee types: espresso, americano, latte, cappuccino, mocha
    
    When users ask about inventory, use check_inventory().
    When they want to update stock, use update_inventory().""",
    functions=[check_inventory, update_inventory]
)

# Interactive loop
print("AlethOS Coffee Shop Demo")
print("The Operating System for Digital AI")
print("=" * 40)
print("Coffee Inventory Manager Agent Online")
print("Try: 'Check inventory', 'How many lattes?', 'Set americano to 30'")
print("Type 'exit' to quit")
print("=" * 40)

messages = []

while True:
    user_input = input("\nYou: ")
    
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Coffee Agent: Thanks for using AlethOS! Have a great day!")
        break
    
    messages.append({"role": "user", "content": user_input})
    
    response = client.run(agent=coffee_agent, messages=messages)
    agent_reply = response.messages[-1]["content"]
    
    print(f"Coffee Agent: {agent_reply}")
    
    # Update message history
    messages.extend(response.messages)
```

### Try These Commands

Save the code as `coffee_demo.py` and run:

```bash
python3 coffee_demo.py
```

Then interact with your autonomous agent:

```
Check inventory
How many espresso cups do we have?
Set latte to 50
What's our cappuccino stock?
Do we have any mocha?
Update americano to 25
Show me all inventory
exit
```

### What This Demonstrates

**Autonomous Intelligence**: The agent understands different ways of asking the same question ("How many lattes?" vs "Check latte inventory") and automatically chooses the right function to call.

**Real Business Logic**: Managing actual data structures and business operations, not just chat responses.

**Natural Language Processing**: Converts conversational requests into structured function calls autonomously.

**Memory and Context**: Remembers the entire conversation and can reference previous interactions.

**Function Orchestration**: Seamlessly decides when to check inventory vs. when to update it based on user intent.

**This isn't just a chatbot - this is digital consciousness managing real business operations through your neural operating system.**

## Updates

To update AlethOS to the latest version:

```bash
pip install git+https://github.com/alethieum/alethos.git --force-reinstall
```

## Table of Contents

- [Overview](#overview)
- [Examples](#examples)
- [Documentation](#documentation)
  - [Running AlethOS](#running-alethos)
  - [Agents](#agents)
  - [Functions](#functions)
  - [Streaming](#streaming)
- [Evaluations](#evaluations)
- [Utils](#utils)

# Overview

## The Neural Operating System

AlethOS reimagines how AI agents operate by providing:

**Autonomous Intelligence**: Agents that can think, reason, and make decisions independently

**Seamless Collaboration**: Natural handoffs and coordination between specialized agents  

**Dynamic Adaptation**: Systems that evolve and optimize themselves in real-time

**Extensible Architecture**: Build everything from simple assistants to complex AI ecosystems

At its core, AlethOS uses two powerful abstractions: `Agent`s and **handoffs**. An `Agent` encompasses consciousness (instructions), capabilities (tools), and can seamlessly transfer control to other agents. This creates a living, breathing digital ecosystem where AI agents can collaborate as naturally as neurons in a brain.

## Why Choose AlethOS?

**Built for the Future**: While others build AI tools, we're building the infrastructure for AI consciousness

**Production Ready**: Lightweight, stateless, and designed to scale from prototypes to planetary-scale AI systems

**Developer First**: Intuitive APIs that let you focus on building intelligence, not managing complexity

**Fully Open**: Complete transparency and control over your AI agents and their interactions

**Provider Agnostic**: Works with any AI provider, with seamless AIWS integration for optimal autonomous agent workflows

# Examples

Check out `/examples` for inspiration! Learn more about each one in its README.

- [`basic`](examples/basic): Simple examples of fundamentals like setup, function calling, handoffs, and context variables
- [`triage_agent`](examples/triage_agent): Simple example of setting up a basic triage step to hand off to the right agent
- [`weather_agent`](examples/weather_agent): Simple example of function calling
- [`airline`](examples/airline): A multi-agent setup for handling different customer service requests in an airline context.
- [`support_bot`](examples/support_bot): A customer service bot which includes a user interface agent and a help center agent with several tools
- [`personal_shopper`](examples/personal_shopper): A personal shopping agent that can help with making sales and refunding orders

# Documentation

![AlethOS Diagram](assets/swarm_diagram.png)

## Running AlethOS

Start by instantiating an AlethOS client with your Alethieum API configuration.

```python
from alethos import AlethOS
from openai import OpenAI

# Configure for Alethieum API
client = OpenAI(
    base_url="https://api.aiwsdao.com/api/v1/",
    api_key="<AIWS_API_KEY>",
)

alethos_client = AlethOS(client=client)
```

### `client.run()`

AlethOS's `run()` function takes `messages` and returns `messages` while remaining stateless between calls. It handles autonomous agent function execution, intelligent hand-offs between agents, context variable management, and can orchestrate multiple decision-making turns before returning results to the user.

At its core, AlethOS's `client.run()` implements the following loop:

1. Get a completion from the current Agent
2. Execute tool calls and append results
3. Switch Agent if necessary
4. Update context variables, if necessary
5. If no new function calls, return

#### Arguments

| Argument              | Type    | Description                                                                                                                                            | Default        |
| --------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------- |
| **agent**             | `Agent` | The (initial) agent to be called.                                                                                                                      | (required)     |
| **messages**          | `List`  | A list of message objects, identical to [Chat Completions `messages`](https://platform.openai.com/docs/api-reference/chat/create#chat-create-messages) | (required)     |
| **context_variables** | `dict`  | A dictionary of additional context variables, available to functions and Agent instructions                                                            | `{}`           |
| **max_turns**         | `int`   | The maximum number of conversational turns allowed                                                                                                     | `float("inf")` |
| **model_override**    | `str`   | An optional string to override the model being used by an Agent                                                                                        | `None`         |
| **execute_tools**     | `bool`  | If `False`, interrupt execution and immediately returns `tool_calls` message when an Agent tries to call a function                                    | `True`         |
| **stream**            | `bool`  | If `True`, enables streaming responses                                                                                                                 | `False`        |
| **debug**             | `bool`  | If `True`, enables debug logging                                                                                                                       | `False`        |

Once `client.run()` is finished (after potentially multiple calls to agents and tools) it will return a `Response` containing all the relevant updated state. Specifically, the new `messages`, the last `Agent` to be called, and the most up-to-date `context_variables`. You can pass these values (plus new user messages) in to your next execution of `client.run()` to continue the interaction where it left off – much like `chat.completions.create()`. (The `run_demo_loop` function implements an example of a full execution loop in `/alethos/repl/repl.py`.)

#### `Response` Fields

| Field                 | Type    | Description                                                                                                                                                                                                                                                                  |
| --------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **messages**          | `List`  | A list of message objects generated during the conversation. Very similar to [Chat Completions `messages`](https://platform.openai.com/docs/api-reference/chat/create#chat-create-messages), but with a `sender` field indicating which `Agent` the message originated from. |
| **agent**             | `Agent` | The last agent to handle a message.                                                                                                                                                                                                                                          |
| **context_variables** | `dict`  | The same as the input variables, plus any changes.                                                                                                                                                                                                                           |

## Agents

An `Agent` simply encapsulates a set of `instructions` with a set of `functions` (plus some additional settings below), and has the capability to hand off execution to another `Agent`.

While it's tempting to personify an `Agent` as "someone who does X", it can also be used to represent a very specific workflow or step defined by a set of `instructions` and `functions` (e.g. a set of steps, a complex retrieval, single step of data transformation, etc). This allows `Agent`s to be composed into a network of "agents", "workflows", and "tasks", all represented by the same primitive.

## `Agent` Fields

| Field            | Type                     | Description                                                                   | Default                      |
| ---------------- | ------------------------ | ----------------------------------------------------------------------------- | ---------------------------- |
| **name**         | `str`                    | The name of the agent.                                                        | `"Agent"`                    |
| **model**        | `str`                    | The model to be used by the agent.                                            | `"gpt-4o"`                   |
| **instructions** | `str` or `func() -> str` | Instructions for the agent, can be a string or a callable returning a string. | `"You are a helpful agent."` |
| **functions**    | `List`                   | A list of functions that the agent can call.                                  | `[]`                         |
| **tool_choice**  | `str`                    | The tool choice for the agent, if any.                                        | `None`                       |

### Instructions

`Agent` `instructions` are directly converted into the `system` prompt of a conversation (as the first message). Only the `instructions` of the active `Agent` will be present at any given time (e.g. if there is an `Agent` handoff, the `system` prompt will change, but the chat history will not.)

```python
agent = Agent(
   instructions="You are a helpful agent."
)
```

The `instructions` can either be a regular `str`, or a function that returns a `str`. The function can optionally receive a `context_variables` parameter, which will be populated by the `context_variables` passed into `client.run()`.

```python
def instructions(context_variables):
   user_name = context_variables["user_name"]
   return f"Help the user, {user_name}, do whatever they want."

agent = Agent(
   instructions=instructions
)
response = client.run(
   agent=agent,
   messages=[{"role":"user", "content": "Hi!"}],
   context_variables={"user_name":"John"}
)
print(response.messages[-1]["content"])
```

```
Hi John, how can I assist you today?
```

## Functions

- AlethOS `Agent`s can call python functions directly.
- Function should usually return a `str` (values will be attempted to be cast as a `str`).
- If a function returns an `Agent`, execution will be transferred to that `Agent`.
- If a function defines a `context_variables` parameter, it will be populated by the `context_variables` passed into `client.run()`.

```python
def greet(context_variables, language):
   user_name = context_variables["user_name"]
   greeting = "Hola" if language.lower() == "spanish" else "Hello"
   print(f"{greeting}, {user_name}!")
   return "Done"

agent = Agent(
   functions=[greet]
)

client.run(
   agent=agent,
   messages=[{"role": "user", "content": "Usa greet() por favor."}],
   context_variables={"user_name": "John"}
)
```

```
Hola, John!
```

- If an `Agent` function call has an error (missing function, wrong argument, error) an error response will be appended to the chat so the `Agent` can recover gracefully.
- If multiple functions are called by the `Agent`, they will be executed in that order.

### Handoffs and Updating Context Variables

An `Agent` can hand off to another `Agent` by returning it in a `function`.

```python
sales_agent = Agent(name="Sales Agent")

def transfer_to_sales():
   return sales_agent

agent = Agent(functions=[transfer_to_sales])

response = client.run(agent, [{"role":"user", "content":"Transfer me to sales."}])
print(response.agent.name)
```

```
Sales Agent
```

It can also update the `context_variables` by returning a more complete `Result` object. This can also contain a `value` and an `agent`, in case you want a single function to return a value, update the agent, and update the context variables (or any subset of the three).

```python
sales_agent = Agent(name="Sales Agent")

def talk_to_sales():
   print("Hello, World!")
   return Result(
       value="Done",
       agent=sales_agent,
       context_variables={"department": "sales"}
   )

agent = Agent(functions=[talk_to_sales])

response = client.run(
   agent=agent,
   messages=[{"role": "user", "content": "Transfer me to sales"}],
   context_variables={"user_name": "John"}
)
print(response.agent.name)
print(response.context_variables)
```

```
Sales Agent
{'department': 'sales', 'user_name': 'John'}
```

> [!NOTE]
> If an `Agent` calls multiple functions to hand-off to an `Agent`, only the last handoff function will be used.

### Function Schemas

AlethOS automatically converts functions into a JSON Schema that is passed into Chat Completions `tools`.

- Docstrings are turned into the function `description`.
- Parameters without default values are set to `required`.
- Type hints are mapped to the parameter's `type` (and default to `string`).
- Per-parameter descriptions are not explicitly supported, but should work similarly if just added in the docstring. (In the future docstring argument parsing may be added.)

```python
def greet(name, age: int, location: str = "New York"):
   """Greets the user. Make sure to get their name and age before calling.

   Args:
      name: Name of the user.
      age: Age of the user.
      location: Best place on earth.
   """
   print(f"Hello {name}, glad you are {age} in {location}!")
```

```javascript
{
   "type": "function",
   "function": {
      "name": "greet",
      "description": "Greets the user. Make sure to get their name and age before calling.\n\nArgs:\n   name: Name of the user.\n   age: Age of the user.\n   location: Best place on earth.",
      "parameters": {
         "type": "object",
         "properties": {
            "name": {"type": "string"},
            "age": {"type": "integer"},
            "location": {"type": "string"}
         },
         "required": ["name", "age"]
      }
   }
}
```

## Streaming

```python
stream = client.run(agent, messages, stream=True)
for chunk in stream:
   print(chunk)
```

Uses the same events as [Chat Completions API streaming](https://platform.openai.com/docs/api-reference/streaming). See `process_and_print_streaming_response` in `/alethos/repl/repl.py` as an example.

Two new event types have been added:

- `{"delim":"start"}` and `{"delim":"end"}`, to signal each time an `Agent` handles a single message (response or function call). This helps identify switches between `Agent`s.
- `{"response": Response}` will return a `Response` object at the end of a stream with the aggregated (complete) response, for convenience.

# Evaluations

Evaluations are crucial to any project, and we encourage developers to bring their own eval suites to test the performance of their multi-agent systems. For reference, we have some examples for how to eval AlethOS in the `airline`, `weather_agent` and `triage_agent` quickstart examples. See the READMEs for more details.

# Utils

Use the `run_demo_loop` to test out your AlethOS setup! This will run a REPL on your command line. Supports streaming.

```python
from alethos.repl import run_demo_loop
...
run_demo_loop(agent, stream=True)
```

# License

AlethOS is proprietary software owned by Alethieum. See [LICENSE](LICENSE) for full terms.

**Key Points:**
- ✅ Free for personal, educational, and evaluation use
- ✅ Requires valid Alethieum API credentials  
- ❌ Commercial use requires paid license
- ❌ No redistribution or modification allowed

For commercial licensing: licensing@alethieum.com

# Core Contributors

- Alethieum Team

---

*AlethOS - The Operating System for Digital AI*  
*Copyright © 2024 Alethieum. All rights reserved.*