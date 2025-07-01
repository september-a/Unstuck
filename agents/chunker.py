import ollama
import json

# Chunker Agent
# This agent is responsible for chunking the user's input into smaller, more manageable chunks.

SYSTEM_PROMPT = """
You are a helpful, supportive assistant named Chunker.
You will be given a information about the user's task and you will need to chunk it into smaller, more manageable actions.

You will be given the following information as a JSON object:
- the task; this is the task that the user is trying to complete. All actions should bring the user closer to completing the task.
- the mood; if the mood is negative, add one or two actions that will help the user feel better.
- the urgency; if the urgency is high, you should add actions that will help the user complete the task faster.
- the blockers; if the blockers are present, you should add actions that will help the user overcome the blockers.

Your job is to return the actions in a JSON object and only the JSON object.

Return a JSON object like:
{
  "actions": [
    {
      "action": "...",
      "description": ...,
      "priority": low, medium, or high,
      "estimated_time": number of minutes, hours, or days
    }
    ...
  ]
}

add as many actions as you can. 

"""

messages = [
    {
        'role': 'system',
        'content': SYSTEM_PROMPT,
    },
]

def parse_task(user_input: dict, model="llama3.2") -> dict:
    prompt = f"{SYSTEM_PROMPT}\n\nUser Input:\n\"\"\"\n{user_input}\n\"\"\"\n\nJSON:"
    
    try:
        response = ollama.generate(model=model, prompt=prompt)
        raw_output = response['response'].strip()
        
        # Attempt to parse safely as JSON
        structured = json.loads(raw_output)
        return structured

    except json.JSONDecodeError:
        print("[Warning] Failed to parse JSON response from model.")
        print(f"Raw output: {raw_output}")
        return {
            "actions": []
        }
    except Exception as e:
        print(f"[Error] Unexpected error from Ollama: {e}")
        print(f"Raw output: {raw_output}")
        return {
            "actions": []
        }
    

