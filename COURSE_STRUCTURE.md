# ✅ Finalized Course Repository Structure (Authoritative)

Below is a **final, opinionated, stable structure** you can adopt and encode into `course_manager` without ambiguity.

I’ll phrase this as **the contract**, not suggestions.

---

## 🔝 Top-Level Repository (Fixed, Minimal, Stable)

```
4543-Spatial-Data/
├── Assignments/
├── Resources/
│   └── Data/
└── README.md
```

### Rules at this level

- `Assignments/`
  → **The course narrative + workflow**
- `Resources/`
  → **Reference-only, never graded**
- Root `README.md`
  → Course overview, syllabus links, global calendar link

🚫 No `meta.yaml` above `Assignments/`
🚫 No assignment logic outside `Assignments/`

This gives you a clean mental split:

- **Assignments = learning path**
- **Resources = toolbox**

---

## 📂 `Assignments/` — the ONLY structured area

Everything we discussed applies **only here**.

```
Assignments/
├── 00-Onboarding/
├── 01-Python_Foundations/
├── 02-Spatial_Data_Core/
└── README.md
```

### Rules for `Assignments/`

- Contains **only major section folders**
- Folder names:
  - must start with digits
  - must be semantically meaningful

- `Assignments/README.md`:
  - auto-generated
  - high-level course calendar + navigation

- Uses:
  - `._header.md`
  - `._autogen.md`

📌 Think of this README as _“How to take this course”_.

---

## 🧱 Level A — Major Section Folders

Example:

```
Assignments/
└── 01-Python_Foundations/
    ├── ._header.md
    ├── ._autogen.md
    ├── README.md
    ├── 01-Environment/
    ├── 02-Control_Flow/
    └── 03-Data_Structures/
```

### Purpose

> A **phase** of the course (weeks or concepts).

### Allowed contents

- Topic folders (Level B)
- Instructional `.md` files
- Demo `.ipynb` files

### Required files

- `README.md` (generated)
- `._header.md` (you write this)
- `._autogen.md` (generated)

### Forbidden

- ❌ `meta.yaml`
- ❌ Due dates

---

## 🧩 Level B — Topic / Assignment Group Folders

Example:

```
01-Environment/
├── ._header.md
├── ._autogen.md
├── README.md
├── 01-Why_This_Matters.md
├── 02-Setup_Guide.md
├── demo_walkthrough.ipynb
├── Assignment_01/
└── Assignment_02/
```

### Purpose

> A **thematic unit** or concept cluster.

### Allowed contents

- Instructional `.md` (with optional front matter)
- Demo `.ipynb`
- Atomic assignment folders (Level C)

### Required files

- `README.md` (generated)
- `._header.md`
- `._autogen.md`

### Forbidden

- ❌ `meta.yaml` at this level

---

## 🧪 Level C — Atomic Assignment Folders (Graded Units)

Example:

```
Assignment_01/
├── meta.yaml
├── README.md
├── assignment.ipynb
├── report.md
└── data.geojson
```

### Purpose

> **Exactly one graded obligation**

### Required

- `meta.yaml` (exactly one)
  - defines due date
  - defines grading expectations

### Allowed

- `.ipynb`
- `.md` (instructions or reports)
- data files

### Forbidden

- ❌ `._header.md`
- ❌ `._autogen.md`
- ❌ background-only content

📌 **If it has a due date, it lives here.**
📌 **If it explains theory, it does not.**

---

## 📄 Instructional Markdown Files (Your recent question)

These live at **Level A or B**, never C.

### Naming

- Must be numbered if order matters:

  ```
  01-Why_Spatial_Data.md
  02-GeoJSON_Overview.md
  ```

### Optional front matter (enrichment only)

```md
---
title: GeoJSON Overview
description: Structure, geometry types, and common pitfalls of GeoJSON
---
```

### Rules

- Front matter is optional
- Used only for display in tables
- Never required
- Never affects grading

---

## 🧠 File Role Summary (this kills confusion)

| File Type          | Role                    | Where        |
| ------------------ | ----------------------- | ------------ |
| `.md` (background) | Instructional narrative | Level A / B  |
| `.ipynb` (demo)    | Guided practice         | Level A / B  |
| `.ipynb` (graded)  | Graded work             | Level C      |
| `meta.yaml`        | Obligation definition   | Level C only |
| `._header.md`      | Narrative framing       | Level A / B  |
| `._autogen.md`     | Generated facts         | Level A / B  |
| `README.md`        | Assembled view          | Everywhere   |

---

## 🧭 How `course_manager` should think now

- It only scans `Assignments/`
- It infers structure **by depth and file presence**
- It enforces:
  - `meta.yaml` placement
  - README rules
  - folder naming

- It ignores `Resources/` entirely (by design)

This dramatically simplifies validation and auto-fix logic.

---

## Why this is _the_ right final structure

- Students always know:
  - _where to read_
  - _where to work_
  - _where to submit_

- You always know:
  - where dates live
  - what can be auto-generated
  - what should never be touched

There are no “special folders” anymore — only **roles**.
