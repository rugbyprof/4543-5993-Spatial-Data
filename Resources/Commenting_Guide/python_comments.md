# 🐍 Python Commenting & Documentation Standard

> **Read this before writing code.**
> Comments are not optional. They are part of the assignment.

This document defines the **required commenting and documentation standard** for all Python programs in this course. These rules exist to make your code:

- Understandable
- Maintainable
- Readable by someone other than you
- Gradable without guesswork

If you think comments are unnecessary, read Rule 1 again.

---

## 🚨 The Rules (Read Carefully)

### **RULE 1**

**Every Python program will contain comments.**

### **RULE 2**

If you are unsure whether something needs a comment,
**refer to RULE 1.**

### **RULE 3**

Code that runs but is poorly documented may receive **significant deductions**.

---

## 📄 File-Level Comment Block (Required)

Every Python file **must begin** with a **module docstring** that follows the structure below.

### ✅ Required File Header Template

```python
"""
**************************************************************************
*
* Author: Your Name
* Email: your.email@school.edu
* Label: A04
* Title: Assignment Title
* Course: CMPS XXXX
* Semester: Spring 2026
*
* Description:
* A thorough explanation of what this program does, how it works,
* and what concepts it demonstrates.
*
* Usage:
* python main.py [arguments if any]
*
* Files:
* main.py        : driver program
* module.py      : supporting module
*
**************************************************************************
"""
```

### Notes

- This **must** be the first thing in the file
- Do not remove the visual “box”
- Replace _only_ the contents, not the structure

---

## 🧱 Class Documentation (Required)

Every class **must** include a class-level docstring immediately under the `class` definition.

### ✅ Class Docstring Template

```python
class LinkedList:
    """
    LinkedList

    Description:
    This class implements a singly linked list that allows indexed
    access, insertion, and removal of elements.

    Public Methods:
    - append(value) -> None
    - pop() -> Any
    - __getitem__(index: int) -> Any
    - __len__() -> int

    Private Methods:
    - _traverse(index: int) -> Node

    Usage:
    ll = LinkedList()
    ll.append(10)
    print(ll[0])
    """
```

### Guidelines

- Public methods **must be listed**
- Private methods must be prefixed with `_`
- The usage example should be realistic

---

## 🔧 Function & Method Documentation (Required)

Every function and method **must** include a docstring describing:

- What it does
- What parameters it accepts
- What it returns

### ✅ Function Docstring Template

```python
def load_list(filename: str) -> list:
    """
    Load List

    Description:
    Reads integers from a file and loads them into a Python list.

    Params:
    filename (str): Name of the input file.

    Returns:
    list: A list of integers read from the file.
    """
```

### Notes

- One-line docstrings are **not acceptable** for non-trivial functions
- Return types must be described even if hinted

---

## 🔐 Public vs Private Methods (Python Convention)

Python does not enforce access modifiers.
**We enforce intent.**

| Intent  | Convention       |
| ------- | ---------------- |
| Public  | `method_name()`  |
| Private | `_method_name()` |

### Example

```python
def _build_tree(self):
    """
    Private: _build_tree

    Description:
    Builds the internal tree structure for encoding.
    """
```

---

## 🧠 Commenting Code Logic

Comments should explain **why**, not just **what**.

### ✅ Good Example

```python
if index >= self.size:
    return -1  # Index is out of bounds
```

### ❌ Bad Example

```python
if index >= self.size:
    return -1
```

---

## 📌 Variable Commenting (Required for Non-Obvious Variables)

Variables that are not self-explanatory **must** be commented.

### ✅ Good

```python
count = 0        # Number of processed records
average = 0.0   # Computed average score
scores = []     # List of exam scores
```

### ❌ Bad

```python
count = 0
average = 0.0
scores = []
```

---

## 🧠 Commenting Logical Blocks

Complex logic must be explained at a **high level**, not line-by-line.

### Example

```python
# Determine which child node should be swapped with the parent
if right_child >= self.next:
    if left_child >= self.next:
        return -1
    return left_child
```

The goal is clarity, not narration.

---

## 📉 Grading Impact (Read This Twice)

The following may result in **point deductions**:

- Missing file header comment
- Missing class docstrings
- Missing function docstrings
- Inaccurate or outdated comments
- Mismatch between documented and actual behavior

Code that works **but is undocumented** is considered **incomplete**.

---

## 🧠 Final Thought

You will read your own code months from now and ask:

> “What was I thinking?”

Good comments answer that question.

If your code cannot be understood by someone else **without explanation**,
it is not finished.

---

**Follow this standard.
Your future self (and your grader) will thank you.**

---
