import json
from openai import OpenAI
import os

def plan_tasks(manager_goal):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    prompt = f"""
    You re a productivity agent for a newcomer/onboarder engineer at a company.
    Break this goal down into smaller tasks, arranged according to priority: High, Medium, Low.

    Goal: {manager_goal}

    Respond ONLY in valid JSON like:
    [
      {{"task": "...", "priority": "..."}}
    ]
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return json.loads(response.choices[0].message.content)
