# Overview — Spatial Failure Modes & Data Pitfalls

Most spatial errors do not crash programs.

They produce results that *look reasonable* — but are wrong.

This lesson focuses on recognizing, diagnosing, and preventing the most common
ways spatial data quietly fails.

---

## Why Spatial Errors Are Dangerous

Spatial data often fails without warnings because:
- coordinate values appear valid
- maps render successfully
- outputs resemble real locations

These failures are dangerous precisely because they are believable.

---

## Common Spatial Failure Modes

This lesson highlights failures such as:
- latitude / longitude order swaps
- incorrect or missing reference assumptions
- mismatched scales and extents
- invalid but plausible coordinates
- geometry that technically exists but is meaningless

Many of these errors only become obvious through careful inspection.

---

## Silent Failures vs Visible Errors

A visible error is easy to fix.
A silent failure can persist unnoticed through analysis, visualization, and reporting.

Spatial thinking requires skepticism, not trust.

---

## Why This Lesson Matters

Understanding spatial failure modes helps prevent:
- incorrect conclusions
- misleading visualizations
- false confidence in results

This lesson prepares students to question outputs before trusting them.

---

## Key Takeaway

> **The most dangerous spatial errors are the ones that look correct.**
