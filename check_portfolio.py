#!/usr/bin/env python3
"""
Run this from the root of your repo.

Shows the expected assignment structure alongside what you have in
completed_assignments/, so you can rename and reorganize until everything lines up.

Usage:
    python check_portfolio.py
"""

from pathlib import Path

# ---------------------------------------------------------------------------
# Expected notebooks — paths relative to completed_assignments/
# ---------------------------------------------------------------------------

EXPECTED = [
    # ── 01-Python_Foundations (38 notebooks — complete 40-50%) ──────────────
    "01-Python_Foundations/01-Working_with_Data_Basic/Assessments/02a-mini_quiz.ipynb",
    "01-Python_Foundations/01-Working_with_Data_Basic/Lessons/01-Lists/01-Lists.ipynb",
    "01-Python_Foundations/01-Working_with_Data_Basic/Lessons/02-Tuples/02-Tuples.ipynb",
    "01-Python_Foundations/01-Working_with_Data_Basic/Lessons/03-Data_Types_and_Arithmetic/03-Data_Types_and_Arithmetic.ipynb",
    "01-Python_Foundations/01-Working_with_Data_Basic/Lessons/03-Dictionaries/03-Dictionaries.ipynb",
    "01-Python_Foundations/02-Scalar_Types_and_Control_Flow/01-Scalar_Types/01-Scalar_Types.ipynb",
    "01-Python_Foundations/02-Scalar_Types_and_Control_Flow/Assessments/mini_quiz.ipynb",
    "01-Python_Foundations/02-Scalar_Types_and_Control_Flow/Lessons/02-Control_Flow/02-Control_Flow.ipynb",
    "01-Python_Foundations/03-Loops_and_Iteration/Assessments/mini_quiz.ipynb",
    "01-Python_Foundations/03-Loops_and_Iteration/Lessons/01-For_Loops/01-For_Loops.ipynb",
    "01-Python_Foundations/03-Loops_and_Iteration/Lessons/02-While_loops/02-While_Loops.ipynb",
    "01-Python_Foundations/03-Loops_and_Iteration/Lessons/03-File_Loops_and_With/03-File_Loops_and_With.ipynb",
    "01-Python_Foundations/04-Foundations/Assessments/01-Foundations_Quiz.ipynb",
    "01-Python_Foundations/04-Foundations/Assessments/02-mini_quiz.ipynb",
    "01-Python_Foundations/04-Foundations/Lessons/01-Magic_Commands/01-magic_commands.ipynb",
    "01-Python_Foundations/04-Foundations/Lessons/02-Markdown_and_Formatting/02-Markdown_and_Formatting.ipynb",
    "01-Python_Foundations/04-Foundations/Lessons/03-Work_With_Files/03-Work_With_Files.ipynb",
    "01-Python_Foundations/04-Foundations/Lessons/04-Data_Input_Output/04-Data_Input_Output.ipynb",
    "01-Python_Foundations/04-Foundations/Lessons/05-Plotting_Basics/05-Plotting_Basics.ipynb",
    "01-Python_Foundations/04-Foundations/Lessons/06-Jupyter_Shortcuts_and_Productivity/06-Jupyter_Shortcuts_and_Productivity.ipynb",
    "01-Python_Foundations/04-Foundations/Lessons/07-Using_Help_and_Docs/07-Using_Help_and_Docs.ipynb",
    "01-Python_Foundations/04-Foundations/Lessons/08-Timing_and_Performance/08-Timing_and_Performance.ipynb",
    "01-Python_Foundations/05-Working_with_Data_Adv/Assessments/mini_quiz.ipynb",
    "01-Python_Foundations/05-Working_with_Data_Adv/Lessons/01-Lists_Dicts_and_Tuples/01-Lists_Dicts_and_Tuples.ipynb",
    "01-Python_Foundations/05-Working_with_Data_Adv/Lessons/02-Pandas_Series_and_Dataframes/02-Pandas_Series_and_Dataframes.ipynb",
    "01-Python_Foundations/05-Working_with_Data_Adv/Lessons/03-Loading_and_Exploring_Eata/03-Loading_and_Exploring_Eata.ipynb",
    "01-Python_Foundations/05-Working_with_Data_Adv/Lessons/04-Indexing_and_Selection/04-Indexing_and_Selection.ipynb",
    "01-Python_Foundations/05-Working_with_Data_Adv/Lessons/05-Basic_Cleaning/05-Basic_Cleaning.ipynb",
    "01-Python_Foundations/05-Working_with_Data_Adv/Lessons/06-Column_Operations/06-Column_Operations.ipynb",
    "01-Python_Foundations/05-Working_with_Data_Adv/Lessons/07-Sorting_and_Filtering/07-Sorting_and_Filtering.ipynb",
    "01-Python_Foundations/05-Working_with_Data_Adv/Lessons/08-Pandas_Wrangle_Lab/08-Pandas_Wrangle_Lab.ipynb",
    "01-Python_Foundations/05-Working_with_Data_Adv/Lessons/09-Survey_Cleaning_Assignment/09-Survey_Cleaning_Assignment.ipynb",
    "01-Python_Foundations/06-Describing_and_Visualizing_Data/Assessments/mini_quiz.ipynb",
    "01-Python_Foundations/06-Describing_and_Visualizing_Data/Lessons/01-Types_of_Data/01-Types_of_Data.ipynb",
    "01-Python_Foundations/06-Describing_and_Visualizing_Data/Lessons/02-Summary_Statistics/02-Summary_Statistics.ipynb",
    "01-Python_Foundations/06-Describing_and_Visualizing_Data/Lessons/03-Matplotlib_Basics/03-Matplotlib_Basics.ipynb",
    "01-Python_Foundations/06-Describing_and_Visualizing_Data/Lessons/04-Seaborn_Basics/04-Seaborn_Basics.ipynb",
    "01-Python_Foundations/06-Describing_and_Visualizing_Data/Lessons/05-Visualization_MiniLab/05-Visualization_MiniLab.ipynb",
    # ── 02-Missile_Geometry_101 (11 notebooks — do all + working project) ───
    "02-Missile_Geometry_101/setup.ipynb",
    "02-Missile_Geometry_101/_micro_lessons/00-Working_Directory.ipynb",
    "02-Missile_Geometry_101/_micro_lessons/01-Data_Elsewhere.ipynb",
    "02-Missile_Geometry_101/_micro_lessons/02-Viewing_Geojson.ipynb",
    "02-Missile_Geometry_101/_micro_lessons/03-Style_W_Logic.ipynb",
    "02-Missile_Geometry_101/_micro_lessons/04-Distance.ipynb",
    "02-Missile_Geometry_101/_micro_lessons/05-Geo_and_Json_overview.ipynb",
    "02-Missile_Geometry_101/_micro_lessons/06-Distances.ipynb",
    "02-Missile_Geometry_101/_micro_lessons/07-InteractiveMaps.ipynb",
    "02-Missile_Geometry_101/_micro_lessons/08-InstallingLocalLib.ipynb",
    "02-Missile_Geometry_101/_micro_lessons/09-YourOwnLibrary.ipynb",
    # ── 02-Missile_Geometry_202 (60 notebooks — do all) ─────────────────────
    "02-Missile_Geometry_202/_micro_lessons/00-Paths/00-Working_Directory.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/00-Paths/01-Relative_vs_Absolute.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/00-Paths/02-Data_Elsewhere.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/00-Paths/03-Find_Project_Root.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/01-JSON_GeoJSON/00-Reading_JSON.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/01-JSON_GeoJSON/01-GeoJSON_Structure.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/01-JSON_GeoJSON/02-Feature_Collections.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/02-Viewing_GeoJSON/00-Geojson.io.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/02-Viewing_GeoJSON/01-iPyLeaflet_Intro.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/02-Viewing_GeoJSON/02-Add_GeoJSON.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/02-Viewing_GeoJSON/03-Map_Control.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/03-Attributes_Styling_Filtering/00-Properties.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/03-Attributes_Styling_Filtering/01-Style_Functions.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/03-Attributes_Styling_Filtering/02-Filtering.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/04-Interactive_Maps/00-Map_Events.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/04-Interactive_Maps/01-Click_Interactions.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/04-Interactive_Maps/02-Dynamic_Layers.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/04-Interactive_Maps/03-User_Feedback.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/05-Coordinate_Geometry/00-Coordinate_Ranges.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/05-Coordinate_Geometry/01-Compute_BBox.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/05-Coordinate_Geometry/02-Draw_BBox.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/05-Coordinate_Geometry/03-Why_LatLon_Is_Weird.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/06-Distance/00-Euclidean_Distance.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/06-Distance/01-Haversine_Distance.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/06-Distance/02-Compare_Methods.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/06-Distance/03-Distance_Applications.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/06-Distance/04-Performance_Batching.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/07-Bearing/00-What_Is_Bearing.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/07-Bearing/01-Compute_Bearing.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/07-Bearing/02-Bearing_V_Direction.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/07-Bearing/03-Bearing_Applications.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/07-Bearing/04-Advanced_Bearing.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/08-Intercept_Pursuit_Module_Design/00-Problem_Setup.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/08-Intercept_Pursuit_Module_Design/01-Constant_Velocity_Intercept.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/08-Intercept_Pursuit_Module_Design/02-Iterative_Pursuit.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/08-Intercept_Pursuit_Module_Design/03-Visual_Simulation.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/08-Intercept_Pursuit_Module_Design/04-Strategy_and_Limits.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/08-Intercept_Pursuit_Module_Design/05-Advanced_Topics.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/09-Intersections/00-Lines_as_Paths.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/09-Intersections/01-Line_Segment_Intersection.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/09-Intersections/02-Line_vs_Polygon_Basics.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/09-Intersections/03-Detecting_Intersections.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/09-Intersections/04-Highlighting_Intersected_Features.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/09-Intersections/05-Applications_Missile_Paths.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/10-Buffers/00_Buffer_Concepts.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/10-Buffers/01_Buffering_Points.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/10-Buffers/02-Buffering_Lines.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/10-Buffers/03-Comparing_Buffer_Sizes.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/10-Buffers/04-Buffer_Visualization_Strategies.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/10-Buffers/05-CRS_Limitations.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/10-Buffers/06-Applications_Impact_Zones.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/11-Point_In_Polygon/00_Click_Capture.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/11-Point_In_Polygon/01_Point_Representation.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/11-Point_In_Polygon/02_Point_In_Polygon_Basics.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/11-Point_In_Polygon/03_Ray_Casting_Algorithm.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/11-Point_In_Polygon/04_Testing_Against_Multiple_Features.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/11-Point_In_Polygon/05_Region_Classification.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/11-Point_In_Polygon/06_Interactive_Click_Applications.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/12-Refactoring/01-From-Notebook-to-Module.ipynb",
    "02-Missile_Geometry_202/_micro_lessons/13-WDO_Library/01-Installing-and-Using-WDO.ipynb",
    # ── 03-Data_Manager (21 notebooks — do all) ─────────────────────────────
    "03-Data_Manager/_micro_lessons/00-Data_Exploration/00-Loading_and_Inspecting.ipynb",
    "03-Data_Manager/_micro_lessons/00-Data_Exploration/01-Measuring_the_Problem.ipynb",
    "03-Data_Manager/_micro_lessons/01-Douglas_Peucker/00-The_Algorithm.ipynb",
    "03-Data_Manager/_micro_lessons/01-Douglas_Peucker/01-Implementation.ipynb",
    "03-Data_Manager/_micro_lessons/01-Douglas_Peucker/02-Epsilon_and_Tradeoffs.ipynb",
    "03-Data_Manager/_micro_lessons/02-LOD_Generation/00-Designing_the_Pipeline.ipynb",
    "03-Data_Manager/_micro_lessons/02-LOD_Generation/01-Writing_the_LOD_Files.ipynb",
    "03-Data_Manager/_micro_lessons/02-LOD_Generation/02-Comparing_the_Levels.ipynb",
    "03-Data_Manager/_micro_lessons/03-Bounding_Box_Culling/00-Bounding_Boxes.ipynb",
    "03-Data_Manager/_micro_lessons/03-Bounding_Box_Culling/01-Intersection_Test.ipynb",
    "03-Data_Manager/_micro_lessons/03-Bounding_Box_Culling/02-Viewport_Culling.ipynb",
    "03-Data_Manager/_micro_lessons/04-Spatial_Grid_Index/00-The_Grid_Idea.ipynb",
    "03-Data_Manager/_micro_lessons/04-Spatial_Grid_Index/01-Building_the_Index.ipynb",
    "03-Data_Manager/_micro_lessons/04-Spatial_Grid_Index/02-Querying_and_Benchmarking.ipynb",
    "03-Data_Manager/_micro_lessons/05-Zoom_Layer_Switching/00-The_Decision_Function.ipynb",
    "03-Data_Manager/_micro_lessons/05-Zoom_Layer_Switching/01-Live_Layer_Switching.ipynb",
    "03-Data_Manager/_micro_lessons/06-Putting_It_Together/00-The_Viewer.ipynb",
    "03-Data_Manager/_micro_lessons/06-Putting_It_Together/01-What_We_Built.ipynb",
    "03-Data_Manager/_micro_lessons/07-The_Library_Version/00-What_Are_Vector_Tiles.ipynb",
    "03-Data_Manager/_micro_lessons/07-The_Library_Version/01-Using_Tippecanoe.ipynb",
    "03-Data_Manager/_micro_lessons/07-The_Library_Version/02-The_Comparison.ipynb",
]

SECTION_NOTES = {
    "01-Python_Foundations": "complete 40–50% of notebooks",
    "02-Missile_Geometry_101": "complete all 11 + include your working project",
    "02-Missile_Geometry_202": "complete all 60 notebooks",
    "03-Data_Manager": "complete all 21 notebooks",
}

IGNORE_DIRS = {
    ".git",
    "__pycache__",
    ".ipynb_checkpoints",
    ".venv",
    "venv",
    "env",
    "node_modules",
}


# ---------------------------------------------------------------------------
# Expected tree rendering
# ---------------------------------------------------------------------------


def build_expected_tree(paths: list[str], base: Path) -> dict:
    """Build a nested dict from flat path list. Leaves are True (found) / False (missing)."""
    tree = {}
    for p in paths:
        parts = Path(p).parts
        node = tree
        for part in parts[:-1]:
            node = node.setdefault(part, {})
        node[parts[-1]] = (base / p).exists()
    return tree


def render_expected_tree(node: dict, prefix: str = "", lines: list = None) -> list[str]:
    if lines is None:
        lines = []
    keys = sorted(node.keys(), key=lambda k: (isinstance(node[k], dict), k.lower()))
    for i, key in enumerate(keys):
        connector = "└── " if i == len(keys) - 1 else "├── "
        value = node[key]
        if isinstance(value, dict):
            lines.append(prefix + connector + key + "/")
            extension = "    " if i == len(keys) - 1 else "│   "
            render_expected_tree(value, prefix + extension, lines)
        else:
            marker = "✅" if value else "❌"
            lines.append(prefix + connector + marker + " " + key)
    return lines


# ---------------------------------------------------------------------------
# Actual tree rendering
# ---------------------------------------------------------------------------


def render_actual_tree(path: Path, prefix: str = "", lines: list = None) -> list[str]:
    if lines is None:
        lines = []
    items = [
        p
        for p in sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
        if p.name not in IGNORE_DIRS and not p.name.startswith(".")
    ]
    for i, item in enumerate(items):
        connector = "└── " if i == len(items) - 1 else "├── "
        lines.append(prefix + connector + item.name)
        if item.is_dir():
            extension = "    " if i == len(items) - 1 else "│   "
            render_actual_tree(item, prefix + extension, lines)
    return lines


# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------


def section_stats(paths: list[str], base: Path) -> dict[str, tuple[int, int]]:
    stats: dict[str, list] = {}
    for p in paths:
        section = Path(p).parts[0]
        stats.setdefault(section, [0, 0])
        stats[section][1] += 1
        if (base / p).exists():
            stats[section][0] += 1
    return {k: tuple(v) for k, v in stats.items()}


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def emit(lines_buf: list, text: str = "") -> None:
    """Print a line and collect it for the output file."""
    print(text)
    lines_buf.append(text)


def main():
    root = Path.cwd()
    completed = root / "completed_assignments"

    if not completed.exists():
        print()
        print("  ERROR: 'completed_assignments/' folder not found.")
        print("  Create it in your repo root and place your notebooks inside.")
        print()
        return

    buf: list[str] = []

    # ── Expected tree ────────────────────────────────────────────────────────
    emit(buf)
    emit(buf, "=" * 60)
    emit(buf, "  EXPECTED STRUCTURE")
    emit(buf, "  (✅ = found in your completed_assignments/  ❌ = missing)")
    emit(buf, "=" * 60)
    emit(buf)
    emit(buf, "completed_assignments/")
    tree = build_expected_tree(EXPECTED, completed)
    for line in render_expected_tree(tree):
        emit(buf, line)

    # ── Actual tree ──────────────────────────────────────────────────────────
    emit(buf)
    emit(buf, "=" * 60)
    emit(buf, "  YOUR completed_assignments/ TREE")
    emit(buf, "=" * 60)
    emit(buf)
    emit(buf, "completed_assignments/")
    actual_lines = render_actual_tree(completed)
    if actual_lines:
        for line in actual_lines:
            emit(buf, line)
    else:
        emit(buf, "  (empty)")

    # ── Summary ──────────────────────────────────────────────────────────────
    emit(buf)
    emit(buf, "=" * 60)
    emit(buf, "  SUMMARY")
    emit(buf, "=" * 60)
    emit(buf)
    stats = section_stats(EXPECTED, completed)
    total_found = total_expected = 0
    for section, (found, expected) in stats.items():
        note = SECTION_NOTES.get(section, "")
        bar = "█" * found + "░" * (expected - found)
        emit(buf, f"  {section}")
        emit(buf, f"    {found}/{expected}  [{bar}]")
        if note:
            emit(buf, f"    Goal: {note}")
        emit(buf)
        total_found += found
        total_expected += expected

    emit(buf, f"  Total: {total_found}/{total_expected} notebooks found")
    emit(buf)

    # ── Self-reported progress score placeholder ─────────────────────────────
    score_section = [
        "",
        "=" * 60,
        "  SELF-REPORTED PROGRESS SCORE",
        "  Edit this file and replace the line below with your score.",
        "  Use a number from 0 to 10, where 10 = 100% complete.",
        "=" * 60,
        "",
        "  Score: __ / 10",
        "",
    ]
    for line in score_section:
        buf.append(line)

    # ── Write progress_checklist.txt ─────────────────────────────────────────
    out_path = root / "progress_checklist.txt"
    out_path.write_text("\n".join(buf) + "\n", encoding="utf-8")
    print()
    print(f"  Saved: {out_path}")
    print("  Open that file and replace '__ / 10' with your score before submitting.")
    print()


if __name__ == "__main__":
    main()
