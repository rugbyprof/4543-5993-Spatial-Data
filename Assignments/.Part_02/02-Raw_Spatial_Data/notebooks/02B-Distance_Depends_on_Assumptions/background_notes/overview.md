# Distance Depends on Assumptions — Overview

Distance feels obvious in everyday life.

If two places are close, the distance is small.  
If they are far apart, the distance is large.

In spatial computing, that intuition breaks down quickly.

This lesson exists to show that **distance is not a fact — it is a model**.

---

## Why Distance Is Not as Simple as It Seems

When we ask for the distance between two locations, we are really asking a deeper question:

> _“Distance according to what rules?”_

Those rules are often **unstated assumptions** about:

- how movement is allowed
- what paths are possible
- what space looks like

Change the assumptions, and the distance changes — even if the locations stay the same.

---

## Distance Depends on How Movement Is Modeled

In this lesson, we explore three common ways to model distance:

### Straight-Line (Euclidean) Distance

- Assumes free movement in any direction
- Ignores obstacles, paths, and constraints
- Answers: _“How far apart are these points in ideal space?”_

### Path-Based Distance

- Measures distance along an actual route
- Reflects how people or vehicles really move
- Answers: _“How far do I actually travel?”_

### Manhattan (Grid) Distance

- Assumes movement is restricted to perpendicular directions
- Models city blocks, grid layouts, and constrained environments
- Answers: _“How far is this if I can’t move diagonally?”_

Each model is internally consistent — and each can be correct **for the right question**.

---

## Why Multiple Distances Can All Be Correct

It is common for two distance calculations to produce different values for the same locations.

This does **not** mean:

- one calculation is wrong
- one dataset is broken
- one person made a mistake

It means the **assumptions changed**.

Understanding this prevents a common failure in spatial analysis:

> trusting a number without understanding how it was produced.

---

## Why This Lesson Matters

Using the wrong distance model can:

- misrepresent travel time
- distort spatial relationships
- lead to incorrect conclusions that look reasonable

These are especially dangerous errors because they often **do not produce obvious failures**.

---

## Key Takeaway

> **Distance is not just how far apart things are —  
> it is how far apart they are _under a specific set of assumptions_.**

If you understand that idea, later topics like:

- scale
- resolution
- spatial analysis
- routing
- projections

will feel logical instead of arbitrary.
