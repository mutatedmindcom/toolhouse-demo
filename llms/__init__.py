import os
from openai import OpenAI
from anthropic import Anthropic
from groq import Groq

llms = {
    "GPT-4o": { 
        "provider": "openai", 
        "model": "gpt-4o", 
    },
    "Claude 3.5 Sonnet": { 
        "provider": "anthropic", 
        "model": "claude-3-5-sonnet-20240620",
    },
    "Llama (GroqCloud)": { 
        "provider": "openai", 
        "model": "llama3-70b-8192", 
    },
    "Mixtral (GroqCloud)": { 
        "provider": "openai", 
        "model": "mixtral-8x7b-32768", 
    },
}

def llm_call(provider, **kwargs):
  if "GroqCloud" in provider:
    return call_groq(**kwargs)
  elif provider == "GPT-4o":
    return call_openai(**kwargs)
  elif provider == "Claude 3.5 Sonnet":
    return call_anthropic(**kwargs)
  else:
    raise Exception(f"Invalid LLM provider: {provider}")
  
def call_openai(**kwargs):
  client = OpenAI()
  
  messages = []
  for message in kwargs.get("messages", []):
    msg = message.copy()
    if "function_call" in msg:
      del msg["function_call"]
      
    if "tool_calls" in msg and msg["tool_calls"] is None:
      del msg["tool_calls"]

    messages.append(msg)
    
  return client.chat.completions.create(
    model=kwargs.get("model"),
    messages=kwargs.get("messages"),
    stream=kwargs.get("stream"),
    tools=kwargs.get("tools"),
    max_tokens=kwargs.get("max_tokens"),
  )

def call_anthropic(**kwargs):
  client = Anthropic()
  return client.messages.create(
    model=kwargs.get("model"),
    messages=kwargs.get("messages"),
    stream=kwargs.get("stream"),
    tools=kwargs.get("tools"),
    max_tokens=kwargs.get("max_tokens"),
  )

def call_groq(**kwargs):
  client = Groq(api_key=os.environ.get('GROQCLOUD_API_KEY'))
  
  messages = []
  for message in kwargs.get("messages", []):
    msg = message.copy()
    if "function_call" in msg:
      del msg["function_call"]
      
    if "tool_calls" in msg and msg["tool_calls"] is None:
      del msg["tool_calls"]

    messages.append(msg)
  
  return client.chat.completions.create(
    model=kwargs.get("model"),
    messages=messages,
    stream=kwargs.get("stream"),
    tools=kwargs.get("tools"),
    max_tokens=kwargs.get("max_tokens"),
  )