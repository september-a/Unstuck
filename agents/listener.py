import ollama
import json

# Listener Agent
# This agent is responsible for parsing the user's input and extracting the emotional state, energy level, task intentions, blockers, and urgency.

SYSTEM_PROMPT = """
You are a helpful, supportive assistant named Listener.
Your job is to analyze the user's message and extract their emotional state (mood), energy level (energy), and task intentions (task).
If applicable, also include any blockers that may be blocking the user from completing the task (blockers) and urgency of the task (urgency).
Only return the JSON object, no other text.

Return a JSON object like:
{
  "mood": "...",
  "energy": "...",
  "task": "...",
  "blockers": [...],
  "urgency": "...",
}
"""

messages = [
    {
        'role': 'system',
        'content': SYSTEM_PROMPT,
    },
]

def parse_user_input(user_input: str, model="llama3.2") -> dict:
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
            "mood": "unsure",
            "energy": "unknown",
            "task": user_input,
            "blockers": [],
            "urgency": "low",
        }
    except Exception as e:
        print(f"[Error] Unexpected error from Ollama: {e}")
        print(f"Raw output: {raw_output}")
        return {
            "mood": "unsure",
            "energy": "unknown",
            "task": user_input,
            "blockers": [],
            "urgency": "low",
        }