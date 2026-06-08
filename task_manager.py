import sqlite3


def save_task(task):

    conn = sqlite3.connect("tasks.db")

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks(task, status) VALUES (?, ?)",
        (task, "Pending")
    )

    conn.commit()
    conn.close()


def get_tasks():

    conn = sqlite3.connect("tasks.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")

    tasks = cursor.fetchall()

    conn.close()

    return tasks


def mark_completed(task_id):

    conn = sqlite3.connect("tasks.db")

    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tasks SET status='Completed' WHERE id=?",
        (task_id,)
    )

    conn.commit()
    conn.close()


def get_task_stats():

    conn = sqlite3.connect("tasks.db")

    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM tasks")
    total_tasks = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM tasks WHERE status='Pending'"
    )
    pending_tasks = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM tasks WHERE status='Completed'"
    )
    completed_tasks = cursor.fetchone()[0]

    conn.close()

    return total_tasks, pending_tasks, completed_tasks