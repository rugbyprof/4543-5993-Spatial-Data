---
title: Safe Editing Rules for GeoJSON
course: Spatial Data & Mapping
purpose: Prevent accidental breakage while encouraging exploration
---

# 🛑 Safe Editing Rules for GeoJSON

GeoJSON is just text — which means it’s easy to edit and easy to break.

These rules exist so you can **experiment confidently** without destroying the file structure.

---

## ✅ What You ARE Allowed to Edit

### 1️⃣ Coordinates

You may:

- Change coordinate values
- Add new coordinate pairs
- Remove coordinate pairs
- Add new Point features
- Extend existing LineStrings

> If you’re editing numbers inside `"coordinates"`, you’re usually safe.

---

### 2️⃣ Properties

You may:

- Add new properties
- Rename property keys
- Change property values
- Remove unused properties

This is where you add **meaning** to spatial data.

---

### 3️⃣ Features

You may:

- Add new `Feature` objects
- Use geometry types already present in the file
- Give features meaningful names or labels

---

### 4️⃣ Bounding Box

You may:

- Modify bounding box values
- Expand the bounding box to include new features

All features **must lie inside the bounding box**.

---

## 🚫 What You Must NOT Break

### ❌ GeoJSON Structure

Do NOT:

- Remove `"type": "FeatureCollection"`
- Rename `"features"`
- Remove `"geometry"` or `"properties"`

---

### ❌ Geometry Type Names

Do NOT:

- Misspell geometry types (`Point`, `LineString`, `Polygon`)
- Invent new geometry types

---

### ❌ Coordinate Shape

Do NOT:

- Change how many bracket levels exist
- Flatten or over-nest coordinates

Examples:

- Point → `[x, y]`
- LineString → `[[x, y], [x, y]]`
- Polygon → `[[[x, y], ...]]`

Brackets matter.

---

### ❌ Polygon Closure

If editing a polygon:

- The first and last coordinate **must match**

---

### ❌ JSON Syntax

Do NOT:

- Remove commas
- Forget quotes
- Add comments (`//` or `#`)

JSON does **not** allow comments.

---

## ⚠️ Allowed but Risky

These won’t break the file, but can cause **logical errors**:

- Mixing up longitude and latitude
- Using unrealistic coordinate values
- Putting features outside the bounding box

These are learning moments — not automatic penalties.

---

## 🧪 How to Check Your File

Before submission:

1. Load it in Python using `json.load()`
2. Paste it into https://geojson.io

If it renders, the structure is valid.

---

## 🧠 Final Rule

> **You may change the world — just don’t destroy the universe.**

If the file loads, you’re probably fine.
