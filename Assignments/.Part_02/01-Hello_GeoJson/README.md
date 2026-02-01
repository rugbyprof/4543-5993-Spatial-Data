# 01 — Hello GeoJSON 🗺️

Welcome to your first spatial data lab.

This assignment is intentionally small, intentionally messy, and intentionally **not** GIS-software based.

Before we use fancy libraries or mapping tools or write code, you need to understand **what spatial data actually looks like** and how easy it is to break — and fix.

GeoJSON is the perfect place to start.

---

## Editing Files

I created a few GeoJson files for you to use, edit, and visualize. This assignment is really about intro to spatial terms and knocking out the fact that you need to understand Json and GeoJson (superset of the rules of json). 

## 🧠 What This Lab Is Really About

By the end of this mini-lab, you should be comfortable with the idea that:

- Spatial data is just structured text
- Maps are created from data, not magic
- Small syntax mistakes can break everything
- Geometry has rules
- Visualization is a form of debugging

If you can fix and extend a GeoJSON file, you can survive this course.

---

## 📁 What’s in This Folder

```

01-HelloGeoJSON/
├── broken_world.geojson
├── README.md

```

You are given **one file**:  
`broken_world.geojson`

It represents a tiny spatial world:

- three locations (coffee, school, bookstore)
- a route between places
- a bounding box around everything

The file is **intentionally broken**.

That is not a mistake.

---

## 🧪 What You Will Do

This mini-lab has **three parts**, all working with the same file.

### Part 1 — Fix the Syntax

Your first job is to make the file **load successfully**.

You will:

- fix missing commas
- correct malformed coordinate lists
- make the file valid JSON

At this stage, the map may still look wrong — that’s expected.

---

### Part 2 — Fix the Geometry

Next, you will repair a geometric issue.

You will:

- identify an invalid polygon
- close it correctly
- verify that it renders as expected

This introduces an important idea:

> Geometry is not just shapes — it has rules.

---

### Part 3 — Extend the World

Finally, you will add your own spatial feature.

You will:

- draw a **MultiLineString** route from MSU campus to a restaurant of your choice
- add meaningful properties
- style your feature (color, thickness, opacity)

You may use **https://geojson.io** to help with drawing and exporting.

---

## 🎨 Styling Matters

Some GeoJSON properties affect how features are drawn.

You are required to style your added feature using at least **two** visual properties, such as:

- stroke color
- line thickness
- opacity
- marker styling

This reinforces an important idea:

> Properties are how data becomes visualization.

---

## 📤 How You Submit (Important)

You will submit **one thing**:

👉 a **public GitHub Gist URL**

### Submission Steps

1. Fix and extend the GeoJSON file
2. Verify it renders correctly in:
   - https://geojson.io
3. Create a **GitHub Gist**
4. Upload your final `.geojson` file
5. Confirm GitHub renders the map
6. Submit the **Gist URL**

If GitHub can render it, the structure is valid.

---

## ✍️ Reflection (Required)

You will answer a few short reflection questions after completing the lab.  
These are about **understanding**, not opinions.

Be concise and honest.

---

## 🚫 What Not to Do

- Do not rename required GeoJSON keys
- Do not invent new geometry types
- Do not add comments to the file (JSON does not allow comments)
- Do not panic when something breaks — that’s the point

---

## 🧠 Final Thought

This lab is not about memorizing formats.

It’s about learning to **trust data less and understand it more**.

We will reuse everything you learn here — with bigger datasets, more tools, and better questions.

If you can fix this file, you’re ready to move on.

---

➡️ Next up: **Raw Spatial Data — Points, Lines, and Polygons**
