# 00 — Development Environment & Workflow 🛠️

Before we work with spatial data, maps, or GeoJSON, we need a **shared, predictable development environment**.

This course is fully online, which means:
- your computer may not look like mine
- your operating system may differ
- your Python setup may not exist yet

To avoid problems, we standardize the workflow.

---

## 🎯 Official Course Workflow (Recommended)

> **GitHub Codespaces + VS Code + Jupyter Notebooks**

This is the **primary workflow** for the course and the one fully supported.

### Why this approach?
- No local installation required
- Same environment for everyone
- Works on Windows, macOS, Linux, Chromebooks
- Built-in GitHub integration
- Jupyter notebooks run out-of-the-box
- Easy transition to Docker later in the course

If you can open a browser, you can do this course.

---

## 🧰 Tools You Will Use

| Tool | Purpose |
|---|---|
| GitHub | version control & submissions |
| GitHub Codespaces | cloud-based development |
| VS Code | code editor (in browser) |
| Jupyter Notebooks | interactive coding & analysis |

---

## 🚀 Part 1 — Create Your Course Repository

1. Log into **https://github.com**
2. Create a **new repository**
3. Name it something like:

```

username-Spatial-Data-Mapping

```

4. Make it **public**
5. Check **Initialize with README**
6. Click **Create repository**

---

## ☁️ Part 2 — Launch a Codespace

1. Open your repository on GitHub
2. Click the green **Code** button
3. Select the **Codespaces** tab
4. Click **Create codespace on main**

After a short setup, you will see **VS Code running in your browser**.

📌 This *is* VS Code — just hosted in the cloud.

---

## 📓 Part 3 — Working with Jupyter Notebooks

Inside Codespaces:
- Create or open `.ipynb` files normally
- The Python environment is already configured
- Jupyter kernels are automatically available

You do **not** need to:
- install Python
- manage virtual environments
- install Jupyter manually

---

## 🗂️ Repository Organization

Your repository will follow this structure:

```

00-Dev_Environment/
01-HelloGeoJSON/
02-Raw_Spatial_Data/
Assignments_Completed/
README.md

```

You will:
- work inside assignment folders
- copy completed work into `Assignments_Completed/`
- submit links or URLs as instructed

---

## 💾 Saving Your Work

Codespaces automatically saves your files, but **saving is not the same as committing**.

When finished:
1. Use the **Source Control** tab in VS Code
2. Stage your changes
3. Commit with a short message
4. Push to GitHub

If it’s on GitHub, it’s backed up.

---

## 🔄 Alternative Workflows (Allowed, Not Recommended)

These options are **permitted**, but **you are responsible** for configuration issues.

### Option A — VS Code + Local Jupyter
- Install Python
- Install Jupyter
- Manage environments
- Select correct kernel

This works — but errors here are harder to debug remotely.

---

### Option B — Google Colab
- Works well for notebooks
- Easy GitHub integration
- Limited file system control
- Less ideal for raw spatial files

Colab is acceptable for **some notebooks**, but not all projects.

---

## ⚠️ Important Notes

- Always run notebooks **top to bottom**
- Always verify outputs before submission
- If something doesn’t work:
  - restart the kernel
  - rerun all cells
- Spatial bugs often come from **environment mismatch**

---

## 🧠 Why We Do This

Spatial data workflows break when:
- environments differ
- libraries don’t match
- paths behave differently

By standardizing early, we avoid confusion later — especially when we introduce:
- raw spatial files
- visualization libraries
- Docker containers
- cloud servers

---

## ✅ Checklist Before Moving On

- [ ] GitHub account created
- [ ] Course repository created
- [ ] Codespace launched successfully
- [ ] Jupyter notebook opened
- [ ] File saved and committed

If all boxes are checked, you’re ready.

---

## 🚦What’s Next

Next up:
> **01 — Hello GeoJSON**

You’ll work with real spatial data immediately — and break it on purpose.

Welcome to spatial thinking.
```

---

### Instructor Notes (not for students)

* This README mirrors the **successful Data Science course workflow** you used before 
* Codespaces gives you:

  * consistent kernels
  * fewer Zoom debug calls
  * cleaner grading
* You can later layer in:

  * Docker
  * Digital Ocean
  * local dev for advanced students

---

If you want, next we can:

1. Add a **student checklist version**
2. Create a **“what to do when something breaks” flowchart**
3. Draft the **00 assignment meta.yaml**
4. Write a **short video script** to introduce the workflow

My vote: **checklist + meta.yaml next** — those age very well.
