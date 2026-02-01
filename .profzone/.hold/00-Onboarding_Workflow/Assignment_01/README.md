# 📍 Assignment 01

## Hello Workflow

> **Read this first (seriously):**
> This assignment is not about geography.
> It’s not about maps.
> It’s not even really about code.
>
> This assignment is about **making sure you, me, and the computer can talk to each other** before we do anything interesting.

If something breaks _here_, we want it to break early — not three weeks into the course at 11:47 PM (and yes I've had some issues the first week).

---

## 🎯 Objectives (What This Proves)

By completing this assignment, you will demonstrate that you can:

- Install and run **Docker**
- Launch **Jupyter Lab**
- Open and run a **Jupyter Notebook**
- Read data from a **JSON file**
- Submit a working notebook for grading

Quietly, this also proves:

- Your file paths work
- Your Python environment works
- You can follow technical instructions (this matters)

---

## 🧰 Required Software

You must have the following installed **before starting**:

- **Docker Desktop**
- **Python 3.x** (local install is fine)
- **Jupyter Lab** (local install OR via Docker)
- A code editor (VS Code is recommended, but not required)

> ⚠️ Heads-up:
> We will be using **Docker throughout the semester**.
> If Docker is not working on your machine, contact me **now**, not later.

---

## 📁 Starter Files

You will be provided (or will clone) a folder structured like this:

```
Assignment_01_Workflow/
├── data/
│   └── geo_terms.json
├── notebooks/
│   └── workflow_check.ipynb
└── README.md
```

Do **not** rename folders.
Do **not** move files.
File paths matter more than feelings.

---

## 🗂️ The Data (Don’t Overthink This)

Inside the `data/` folder is a file called:

```
geo_terms.json
```

This file contains a small list of **geographic / spatial terms** stored as structured data.

You are **not expected to understand these terms yet**.

For now, treat them like:

> “Words in a file that Python can read.”

We will return to these ideas later — many times.

---

## 📓 Your Task (Step by Step)

Open `notebooks/workflow_check.ipynb` and complete the following:

---

### ✅ Step 1: Verify Python Is Running

Add a code cell and run:

```python
import sys
print(sys.version)
```

If this runs without error, Python is alive.
That’s a win.

---

### ✅ Step 2: Load the JSON File

In a new cell, load the data file:

```python
import json

with open("../data/geo_terms.json", "r") as f:
    geo_terms = json.load(f)

len(geo_terms)
```

If this runs:

- Your file paths are correct
- Python can read external data
- You are officially “set up”

---

### ✅ Step 3: Print the Terms (Human-Readable)

Add another cell and print the contents cleanly:

```python
for term in geo_terms:
    print(f"{term['term']} ({term['category']}):")
    print(f"  {term['description']}")
    print()
```

Your output should list several terms with short descriptions.

No plots.
No maps.
No panic.

---

## 📤 What to Submit

Submit **one** of the following (as instructed in the LMS):

- The completed `workflow_check.ipynb` file
  **AND**
- A PDF export or screenshot showing successful output

> ⚠️ Important:
>
> - The notebook must **run without errors**
> - “It works on my machine” is not a submission format

---

## 🧠 How This Is Graded

This assignment is **completion-based**.

| Criteria                     | Points |
| ---------------------------- | ------ |
| Notebook runs without errors | ✔      |
| JSON file loaded correctly   | ✔      |
| Output displayed             | ✔      |
| Submitted on time            | ✔      |

There are **no trick questions** and **no partial credit debates**.

---

## 🆘 If Something Breaks

Before messaging me, include:

1. What step you are on
2. The **exact error message**
3. A screenshot (if applicable)

Messages that say:

> “It doesn’t work”

…will be met with:

> “I need more information.”

That’s not me being mean — that’s real-world problem solving.

Typically I will zoom same day for help when asked. Just ask.

---

## 🧭 Why We’re Doing This

This assignment exists so that:

- You are not fighting tools while learning spatial concepts
- I know who needs help early
- The rest of the course runs smoothly

Think of this as:

> **“Checking the microphones before the concert.”**

---

## ✅ When You’re Done

If this assignment works:

- You are officially ready for Spatial Data & Mapping
- Everything else builds on this foundation
- You’ve already done some “real” data work (even if it felt simple)

---

### 🎉 That’s it.

- No maps yet.
- No GIS software yet.
- Just a clean start.

---

# 📚 External References (Use These, Don’t Panic)

You are **not expected to memorize Docker or Jupyter**.
You _are_ expected to know how to look things up.

These are **safe, official, beginner-friendly references**.

---

## 🐳 Docker (Recommended Starting Points)

### 🔗 **Docker — Official Docs**

- Get started guide:
  [https://docs.docker.com/get-started/](https://docs.docker.com/get-started/)

- Docker Desktop overview:
  [https://docs.docker.com/desktop/](https://docs.docker.com/desktop/)

What to focus on:

- What an _image_ is
- What a _container_ is
- Running containers (not building yet)

Ignore:

- Kubernetes
- Swarm
- Anything that sounds like DevOps cosplay

---

## 📓 Jupyter Notebooks & Jupyter Lab

### 🔗 **Jupyter — Official Docs**

- Jupyter Lab overview:
  [https://jupyterlab.readthedocs.io/en/stable/](https://jupyterlab.readthedocs.io/en/stable/)

- Notebook basics:
  [https://jupyter-notebook.readthedocs.io/en/stable/](https://jupyter-notebook.readthedocs.io/en/stable/)

What to focus on:

- Running cells
- Restarting kernel
- Saving notebooks

Ignore:

- Extensions
- Multi-user servers
- Anything mentioning “Hub” for now

---
