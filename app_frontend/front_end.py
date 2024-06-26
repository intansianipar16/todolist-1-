import streamlit as st
import requests
from dotenv import load_dotenv
import os

# Memuat variabel lingkungan dari file .env
load_dotenv()

# Mendapatkan nilai BASE_URL dari variabel lingkungan
BASE_URL = 'https://788f-103-82-14-56.ngrok-free.app/tasks' if os.getenv("BASE_URL") is None else os.getenv("BASE_URL")

def get_tasks():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        return response.json()
    return []

def add_task(task):
    response = requests.post(BASE_URL, json={"task": task})
    return response.json()

def delete_task(task_id):
    response = requests.delete(f"{BASE_URL}/{task_id}")
    return response.json()

def main():
    st.title("Todo List App")

    # Input untuk task baru
    task = st.text_input("Enter a task")
    if st.button("Add Task"):
        if task:
            response = add_task(task)
            st.success(response['message'])
        else:
            st.error("Task content is missing!")

    st.write("## Todo List")
    tasks = get_tasks()
    for i, task in enumerate(tasks):
        st.write(f"{i+1}. {task}  ")
        if st.button(f"Delete Task {i+1}", key=i):
            response = delete_task(i)
            st.success(response['message'])

    st.write("## Refresh List")
    if st.button("Refresh"):
        st.experimental_rerun()

if __name__ == "__main__":
    main()
