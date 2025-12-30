import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

st.set_page_config(page_title="FlowAgent", layout="centered")
st.title("FlowAgent")

def plan_tasks(goal):
    return [
        {"task": f"Analyze goal: {goal}", "priority": "High"},
        {"task": "Break into subtasks", "priority": "Medium"}
    ]

def schedule_task(task):
    return f"Scheduled: {task}"

def fetch_status():
    return {"status": "All systems operational"}

def reflect(tasks, status):
    return "Tasks planned and executed successfully."

def run_agent(manager_goal):
    tasks = plan_tasks(manager_goal)

    tool_logs = []
    for task in tasks:
        if task["priority"] == "High":
            tool_logs.append(schedule_task(task["task"]))

    status = fetch_status()
    reflection = reflect(tasks, status)

    return tasks, tool_logs, status, reflection

goal = st.text_input("Enter manager goal")

if st.button("Run Agent"):
    with st.spinner("Running agent..."):
        tasks, tool_logs, status, reflection = run_agent(goal)

    st.subheader("Tasks")
    st.write(tasks)

    st.subheader("Tool Logs")
    st.write(tool_logs)

    st.subheader("Status")
    st.write(status)

    st.subheader("Reflection")
    st.write(reflection)
