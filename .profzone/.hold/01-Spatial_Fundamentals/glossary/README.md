# 📖 Spatial Fundamentals — Glossary

> This glossary exists so we all use the **same words the same way**.
>
> These definitions are intentionally simple.
> They will grow deeper as the course progresses.

---

## **Location**

A description of _where something is_ relative to a reference system.

A location is **not** a place name or a map pin by itself — it is data that only makes sense if everyone agrees on the reference being used.

---

## **Position**

A specific numeric representation of location, often expressed as coordinates such as `(x, y)` or `(latitude, longitude)`.

Position is how a computer understands location.

---

## **Coordinate**

A numeric value (or set of values) used to describe position within a coordinate system.

Coordinates are **numbers with meaning we assign**, not inherently “geographic” by themselves.

---

## **Absolute Location**

A location described using a fixed reference system that does not depend on other objects.

Examples include GPS coordinates or a point in a defined coordinate system.

---

## **Relative Location**

A location described in relation to another object.

Examples include “5 miles north of campus” or “two blocks east of the library.”

---

## **Distance**

A measure of separation between two locations.

Distance is **model-dependent** — different distance formulas can produce different results for the same two points.

---

## **Direction**

A description of where one location lies relative to another.

Direction depends on:

- how axes are defined
- how orientation is interpreted
- what reference frame is being used

---

## **Scale**

A description of **how much of the world is being viewed**.

- Large scale → small area, high detail
- Small scale → large area, less detail

Scale describes _context_, not data quality.

---

## **Resolution**

A description of **how detailed the data itself is**.

Resolution controls:

- the smallest feature that can be represented
- how finely space is sampled or divided

Higher resolution is not always better.

---

## **Extent**

The geographic area covered by a dataset.

Anything outside the extent:

- is not represented
- should not be analyzed as if it exists

Ignoring extent is a common source of spatial error.

---

## **Bounding Box**

A simple rectangular representation of spatial extent, defined by:

- minimum x
- minimum y
- maximum x
- maximum y

Bounding boxes are used for fast filtering, clipping, and sanity checks.

---

## **Spatial Abstraction**

A simplified representation of the real world used to make spatial data manageable and analyzable.

All spatial data is an abstraction — there is no such thing as a perfect or complete representation.

---

## **Vector Data**

A spatial abstraction that represents features as:

- points
- lines
- polygons

Vector data is well suited for discrete objects with clear boundaries.

---

## **Raster Data**

A spatial abstraction that represents space as a grid of cells.

Raster data is well suited for continuous surfaces such as elevation, temperature, or imagery.

---

## **Granularity**

The level of detail at which spatial data is represented.

Granularity is closely related to resolution and strongly influences what questions can be answered.

---

## **Reference System**

The agreed-upon framework that gives meaning to coordinates, distances, and directions.

Without a reference system, spatial numbers are just numbers.

---

## **Model**

A simplified representation of reality created to answer specific questions.

Spatial models always involve assumptions and tradeoffs.

---

## **Tradeoff**

A necessary compromise between competing goals such as:

- accuracy vs performance
- detail vs clarity
- precision vs usability

Spatial analysis is full of tradeoffs — recognizing them is a core skill.

---

## **Common Misconception**

An incorrect assumption that often leads to spatial errors.

Examples include:

- “More detail is always better”
- “Maps show reality”
- “Coordinates are exact”

---

### ✅ End of Module 01 Glossary

> You are not expected to memorize this glossary.
> You _are_ expected to recognize these terms when they appear.

You will see them again. Often.
