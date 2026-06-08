import streamlit as st
import pandas as pd

from database import create_database

from task_manager import (
    save_task,
    get_tasks,
    get_task_stats,
    mark_completed
)

from ai_processor import (
    extract_tasks,
    summarize_notes
)

# Create database if it doesn't exist
create_database()

# Page configuration
st.set_page_config(
    page_title="SmartTask AI",
    page_icon="✅",
    layout="wide"
)

# Header
st.title("✅ SmartTask AI")
st.subheader("AI Powered Productivity Assistant")

# Dashboard Stats
total_tasks, pending_tasks, completed_tasks = get_task_stats()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Tasks", total_tasks)

with col2:
    st.metric("Pending Tasks", pending_tasks)

with col3:
    st.metric("Completed Tasks", completed_tasks)

# =====================================
# TASK EXTRACTION SECTION
# =====================================

st.subheader("🤖 AI Task Extraction")

user_input = st.text_area(
    "Enter your task or note:",
    height=150
)

if st.button("Process"):

    if user_input.strip():

        ai_tasks = extract_tasks(user_input)

        # Save extracted tasks
        for item in ai_tasks:
            save_task(item["task"])

        st.success(
            f"{len(ai_tasks)} tasks extracted and saved successfully!"
        )

        st.subheader("🤖 AI Analysis")

        ai_df = pd.DataFrame(ai_tasks)

        st.dataframe(
            ai_df,
            width="stretch"
        )

    else:
        st.warning("Please enter a task.")

# =====================================
# MEETING NOTES SUMMARIZER
# =====================================

st.subheader("📝 Meeting Notes Summarizer")

meeting_notes = st.text_area(
    "Paste meeting notes here:",
    height=150,
    key="meeting_notes"
)

if st.button("Summarize Notes"):

    if meeting_notes.strip():

        summary = summarize_notes(meeting_notes)

        st.success("Summary Generated")

        st.text(summary)

    else:
        st.warning("Please enter meeting notes.")

# =====================================
# SAVED TASKS
# =====================================

st.subheader("Saved Tasks")

tasks = get_tasks()

if tasks:

    df = pd.DataFrame(
        tasks,
        columns=["ID", "Task", "Status"]
    )

    st.dataframe(
        df,
        width="stretch"
    )

    pending_tasks_list = [
        task for task in tasks
        if task[2] == "Pending"
    ]

    if pending_tasks_list:

        task_options = {
            f"{task[0]} - {task[1]}": task[0]
            for task in pending_tasks_list
        }

        selected_task = st.selectbox(
            "Select task to mark as completed",
            task_options.keys()
        )

        if st.button("Mark Completed"):

            task_id = task_options[selected_task]

            mark_completed(task_id)

            st.success("Task marked as completed!")

            st.rerun()

else:
    st.info("No tasks found.")