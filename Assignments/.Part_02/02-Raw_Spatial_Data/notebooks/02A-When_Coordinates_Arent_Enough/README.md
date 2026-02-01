# 🧩 02a — When Coordinates Aren’t Enough

**Module:** Project 02 – Spatial Fundamentals

---

## 0️⃣ Framing the Problem (Opening Section)

**Purpose:**
Re-anchor students mentally before introducing _new_ ideas.

### Concepts

- We’ve been using coordinates already
- Things “worked”… but felt weird
- That discomfort was not accidental

### Instructor intent

This section explicitly validates:

- lon/lat confusion
- bounding box oddities
- routes appearing in strange places

> _“If coordinates were enough, GIS wouldn’t exist.”_

---

## 1️⃣ Coordinates Are Just Numbers

**Big idea:**
Without context, coordinates are meaningless.

### Concepts

- `(x, y)` ≠ location
- Numbers don’t imply units
- Numbers don’t imply reference
- Computers do not know geography

### Typical prompts (no code yet)

- “What could this pair represent?”
- “Could this be a valid location?”
- “What assumptions are you making?”

### Coding-friendly ideas (later)

- Print raw coordinate lists
- Compare identical numbers used in different contexts

---

## 2️⃣ What’s Missing from an (x, y) Pair?

**Big idea:**
Meaning comes from _what surrounds_ the numbers.

### Missing components (explicit list)

- reference system
- units
- origin
- orientation
- context / purpose
- precision / uncertainty

### Conceptual prompts

- “What questions must be answered before using this?”
- “Which missing piece is the most dangerous to ignore?”

### Exam gold

This section alone can generate:

- short answer
- select-all-that-apply
- explain-the-failure questions

---

## 3️⃣ Longitude and Latitude Are Not Symmetric

**Big idea:**
Lat/lon looks like x/y — but behaves nothing like it.

### Concepts

- valid latitude range
- valid longitude range
- asymmetry (−90↔90 vs −180↔180)
- convention vs intuition
- why order matters

### Conceptual prompts

- “Which value _could_ be latitude?”
- “Why didn’t this error crash anything?”
- “Why do maps fail silently?”

### Guardrail

🚫 No trigonometry
🚫 No Earth geometry
🚫 No distance math

This is **sanity checking**, not modeling.

---

## 4️⃣ Reference Systems Are Agreements

**Big idea:**
Location is relational, not absolute.

### Concepts

- reference systems as contracts
- “absolute” locations still depend on agreement
- why datasets must agree to be comparable

### Prompts

- Compare:
  - “next to the library”
  - `(33.88, -98.52)`

- Ask:
  - Which is more precise?
  - Which is more meaningful?
  - Which is more useful _without_ context?

### Pedagogical role

This section quietly prepares students for:

- CRS
- projections
- EPSG
  without naming them yet.

---

## 5️⃣ Common Failure Modes (Why Things Go Wrong)

**Big idea:**
Spatial data often fails _quietly_.

### Failure patterns

- swapped lon/lat
- wrong units
- mixed reference systems
- “looks right” but isn’t

### Prompts

- “Why is a wrong answer worse than an error?”
- “Why didn’t the software stop you?”
- “What should have been checked earlier?”

### Coding-friendly ideas

- Detect out-of-range values
- Flag suspicious clusters
- Warn instead of failing

---

## 6️⃣ Why This Matters _Before_ Distance or Projections

**Big idea:**
Bad coordinates poison everything downstream.

### Concepts

- distance depends on meaning
- projections don’t fix nonsense
- validation precedes analysis

### Bridge language

> _“If coordinates are wrong, distance is meaningless.”_

This cleanly tees up **02b — Distance Depends on Assumptions**.

---

## 7️⃣ Introspective Pause (No Code)

**Purpose:**
Slow students down and lock in mental models.

### Example prompts

- Why does location require a reference?
- Why do coordinate errors often go unnoticed?
- What makes spatial data riskier than non-spatial data?
- When would “looks right” be unacceptable?

📌 These directly feed:

- quizzes
- midterm questions
- reflection grading

---

## 🚧 Scope Guardrails (Locked)

This notebook will **not**:

- compute distances
- introduce projections
- use EPSG codes
- discuss Earth curvature
- solve accuracy problems

Those belong to:

- **02b** (distance)
- **02d** (projection thinking)

---

## 🧠 Success Criteria for 02a

If 02a works, students should say things like:

- “Oh… coordinates alone don’t mean anything.”
- “That explains why my route was in the ocean.”
- “I shouldn’t trust numbers without context.”

If they say:

- “I still don’t get projections”

That’s **correct** at this stage.
