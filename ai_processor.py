from ml_predictor import predict_category


def get_priority(task):

    task = task.lower()

    if "urgent" in task:
        return "High"

    elif "call" in task:
        return "High"

    elif "report" in task:
        return "Medium"

    elif "invoice" in task:
        return "Medium"

    else:
        return "Low"


def extract_tasks(user_text):

    separators = [
        " and ",
        ",",
        ".",
        "\n"
    ]

    tasks = [user_text]

    for separator in separators:

        new_tasks = []

        for task in tasks:
            new_tasks.extend(task.split(separator))

        tasks = new_tasks

    cleaned_tasks = []

    for task in tasks:

        task = task.strip()

        if task:

            cleaned_tasks.append(
                {
                    "task": task,
                    "category": predict_category(task),
                    "priority": get_priority(task)
                }
            )

    return cleaned_tasks


def summarize_notes(notes):

    lines = notes.split(".")

    summary = []

    for line in lines:

        line = line.strip()

        if line:
            summary.append("• " + line)

    return "\n".join(summary)