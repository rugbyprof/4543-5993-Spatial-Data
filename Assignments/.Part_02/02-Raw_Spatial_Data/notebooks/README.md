# 🟩 Project 02 — Spatial Fundamentals

**Goal:** _Explain why spatial data breaks when scale, distance, and reference change._

Project 01 taught students to **edit** spatial data.
Project 02 teaches them to **distrust** it (productively).

---

## 🧩 02a — _When Coordinates Aren’t Enough_

### (aka: “Why (x, y) keeps lying to you”)

### Core Concept

Coordinates **require context** to mean anything useful.

This notebook formalizes discomfort students already felt in:

- Hello_GeoJSON
- 01b (Points as Places)

### Topics (Progressive)

- Coordinate pairs ≠ location
- What information is missing from (x, y)
- Reference systems as agreements
- Longitude / latitude ranges and asymmetry
- Why lon/lat order exists (not just “because”)

### Coding Problem Ideas

- Parse coordinates and print:
  - min/max lon
  - min/max lat

- Detect invalid ranges
- Identify swapped lon/lat automatically
- Compare two points numerically that _look_ close but aren’t

### Explicitly NOT Here

❌ Projections
❌ EPSG codes
❌ Distance formulas

This is about **meaning**, not measurement.

---

## 🧩 02b — _Distance Depends on Assumptions_

### (aka: “Straight lines betray you”)

### Core Concept

Distance is not a single thing — it depends on **how movement is modeled**.

This notebook _formalizes_ what 01c hinted at.

### Topics (Progressive)

- Euclidean distance (revisited, critically)
- Path-based distance
- Manhattan distance intuition
- Campus vs city vs global distance
- When degrees ≠ distance

### Coding Problem Ideas

- Compute:
  - straight-line distance
  - path distance

- Compare distances across scales
- Show numeric differences grow with scale
- Write a function that “chooses the wrong distance”

### Explicitly NOT Here

❌ Geodesics
❌ Haversine formula (yet)
❌ Projections

This is still **conceptual modeling**, not precision.

---

## 🧩 02c — _Scale, Resolution, and Detail_

### (aka: “Zoom is not scale”)

### Core Concept

What you see depends on **how much detail you choose to keep**.

This notebook turns:

- bounding boxes
- extents
- simplification

into _design decisions_.

### Topics (Progressive)

- Scale vs zoom
- Resolution as a choice
- What gets lost at small scales
- Why small changes disappear
- Generalization intuition

### Coding Problem Ideas

- Subset features by extent
- Drop points below a threshold
- Compare “full” vs “simplified” data
- Count features before/after filtering

### Explicitly NOT Here

❌ Raster math
❌ Cartographic styling theory

This is about **data reduction**, not visualization polish.

---

## 🧩 02d — _Geographic vs Projected Thinking_

### (aka: “Why the Earth ruins everything”)

### Core Concept

The Earth is curved, but computers prefer flat spaces.

This is where **projection thinking finally earns its keep**.

### Topics (Progressive)

- Geographic coordinates vs flat coordinates
- Why lon/lat fails for distance & area
- What projections _try_ to preserve
- Tradeoffs (distance, area, shape)
- “There is no perfect map”

### Coding Problem Ideas

- Compare distances before/after projection (conceptually)
- Identify distortion visually
- Reason about what breaks at large extents
- Choose a projection _based on purpose_ (no math)

### Explicitly NOT Here

❌ EPSG memorization
❌ Projection math derivations

This is **decision-making**, not cartography class.

---

## 🧩 02e — _Spatial Relationships Have Rules_

### (aka: “Space has grammar”)

### Core Concept

Spatial data supports questions that non-spatial data cannot.

This notebook introduces **topological thinking**.

### Topics (Progressive)

- Intersects
- Contains / within
- Touches / overlaps
- Proximity as a question
- Why topology exists at all

### Coding Problem Ideas

- Point-in-polygon checks
- Count intersections
- Find nearest features
- Detect ambiguous relationships

### Explicitly NOT Here

❌ Spatial databases
❌ Performance optimization

This is about **questions**, not speed.

---

## 🧩 02f — _Spatial Fundamentals Synthesis_

### (aka: “Why spatial data is hard”)

### Core Concept

Everything they’ve learned can fail — and that’s expected.

This notebook is **reflection + integration**, not new material.

### Topics

- Review of assumptions
- Common failure modes
- “Why did my map lie?”
- When to stop trusting results
- Preparing for Project 03

### Coding / Activity Ideas

- Diagnose broken analyses
- Explain incorrect maps
- Short written reflections
- Compare two “correct” answers

### Explicitly NOT Here

❌ New techniques

This is consolidation and confidence-building.

---

## 🧠 Why this structure works for _you_

- Each notebook has **one dominant idea**
- Each idea supports **multiple small coding tasks**
- You can:
  - skip a notebook
  - merge two
  - stretch one across weeks
    without breaking the arc

Most importantly:

> **Every notebook explains a pain students already felt earlier.**

That’s why it’ll stick.
