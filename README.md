# SmartTask AI

AI-Powered Productivity Assistant built using Machine Learning, Natural Language Processing, and Streamlit.

## Overview

SmartTask AI helps users capture tasks, notes, reminders, and to-dos using natural language.

The system automatically:

- Extracts actionable tasks from text
- Categorizes tasks using Machine Learning
- Assigns priorities
- Stores tasks in a database
- Tracks completion status
- Summarizes meeting notes

This project was developed for the Claysys AI Hackathon under the "Lightweight Personal Productivity Capture Tool" problem statement.

---

## Features

### Task Extraction

Convert natural language notes into individual tasks.

Example Input:

Call customer regarding project update.
Prepare dashboard report.
Send invoice to vendor.
Pay electricity bill.

Output:

- Call customer regarding project update
- Prepare dashboard report
- Send invoice to vendor
- Pay electricity bill

---

### Machine Learning Based Categorization

Tasks are automatically categorized into:

- Work
- Meeting
- Finance
- Personal

Example:

| Task | Category |
|--------|-----------|
| Call customer | Meeting |
| Prepare dashboard report | Work |
| Send invoice | Finance |
| Pay electricity bill | Personal |

---

### Priority Detection

Tasks are assigned priority levels:

- High
- Medium
- Low

---

### Task Dashboard

Displays:

- Total Tasks
- Pending Tasks
- Completed Tasks

---

### Task Management

Users can:

- Save tasks
- View tasks
- Mark tasks as completed

---

### Meeting Notes Summarizer

Convert long meeting notes into concise summaries using AI.

---

## Machine Learning Pipeline

### Dataset

Custom curated productivity dataset.

Categories:

- Work
- Meeting
- Finance
- Personal

### Data Augmentation

Dataset expanded through task variations and paraphrasing.

Final Dataset Size:

160+ samples

### Feature Engineering

TF-IDF Vectorization

Converts task text into numerical features.

### Model

Multinomial Naive Bayes

### Evaluation

Classification Accuracy:

97%

Classification Report:

| Category | Precision | Recall |
|-----------|-----------|---------|
| Work | 1.00 | 0.88 |
| Meeting | 1.00 | 1.00 |
| Finance | 0.89 | 1.00 |
| Personal | 1.00 | 1.00 |

Overall Accuracy:

97%

---

## Tech Stack

Frontend:
- Streamlit

Backend:
- Python

Database:
- SQLite

Machine Learning:
- Scikit-Learn
- TF-IDF
- Naive Bayes

AI:
- Gemini API

---

## Project Structure

SmartTaskAI/

├── app.py

├── ai_processor.py

├── database.py

├── task_manager.py

├── train_model.py

├── test_model.py

├── task_classifier.pkl

├── data/

│   ├── task_dataset.csv

│   └── augmented_task_dataset.csv

├── requirements.txt

└── README.md

---

## Installation

Clone Repository

```bash
git clone https://github.com/yourusername/SmartTaskAI.git

cd SmartTaskAI
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Application

```bash
streamlit run app.py
```

---

## Future Improvements

- Voice Task Capture
- Calendar Integration
- Email Reminder Automation
- Task Recommendation Engine
- Deep Learning Based Classification
- User-Specific Personalization

---

## Author

Mehafil Salim

Claysys AI Hackathon 2026