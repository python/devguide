"""Read in a JSON and generate two CSVs and an SVG file."""
from __future__ import annotations

import csv
import datetime as dt
import json

import jinja2


def csv_date(date_str: str, now_str: str) -> str:
    """Format a date for CSV."""
    if date_str > now_str:
        # Future, add italics
        return f"*{date_str}*"
    return date_str


def parse_date(date_str: str) -> dt.date:
    if len(date_str) == len("yyyy-mm"):
        # We need a full yyyy-mm-dd, so let's approximate
        return dt.date.fromisoformat(date_str + "-01")
    return dt.date.fromisoformat(date_str)


class Versions:
    """For converting JSON to CSV and SVG."""

    def __init__(self) -> None:
        with open("include/release-cycle.json", encoding="UTF-8") as in_file:
            self.versions = json.load(in_file)

        # Generate a few additional fields
        for key, version in self.versions.items():
            version["key"] = key
            version["first_release_date"] = parse_date(version["first_release"])
            version["end_of_life_date"] = parse_date(version["end_of_life"])
        self.sorted_versions = sorted(
            self.versions.values(),
            key=lambda v: [int(i) for i in v["key"].split(".")],
            reverse=True,
        )

    def write_csv(self) -> None:
        """Output CSV files."""
        now_str = str(dt.datetime.utcnow())

        versions_by_category = {"branches": {}, "end-of-life": {}}
        headers = None
        for details in self.sorted_versions:
            row = {
                "Branch": details["branch"],
                "Schedule": f":pep:`{details['pep']}`",
                "Status": details["status"],
                "First release": csv_date(details["first_release"], now_str),
                "End of life": csv_date(details["end_of_life"], now_str),
                "Release manager": details["release_manager"],
            }
            headers = row.keys()
            cat = "end-of-life" if details["status"] == "end-of-life" else "branches"
            versions_by_category[cat][details["key"]] = row

        for cat, versions in versions_by_category.items():
            with open(f"include/{cat}.csv", "w", encoding="UTF-8", newline="") as file:
                csv_file = csv.DictWriter(file, fieldnames=headers, lineterminator="\n")
                csv_file.writeheader()
                csv_file.writerows(versions.values())

    def write_svg(self) -> None:
        """Output SVG file."""
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader("_tools/"),
            autoescape=True,
            lstrip_blocks=True,
            trim_blocks=True,
            undefined=jinja2.StrictUndefined,
        )
        template = env.get_template("release_cycle_template.svg")

        # Scale. Should be roughly the pixel size of the font.
        # All later sizes are miltiplied by this, so you can think of all other
        # numbers being multiples of the font size, like using `em` units in
        # CSS.
        # (Ideally we'd actually use `em` units, but SVG viewBox doesn't take
        # those.)
        SCALE = 18

        # Width of the drawing and main parts
        DIAGRAM_WIDTH = 46
        LEGEND_WIDTH = 7
        RIGHT_MARGIN = 0.5

        # Height of one line. If you change this you'll need to tweak
        # some positioning numbers in the template as well.
        LINE_HEIGHT = 1.5

        first_date = min(ver["first_release_date"] for ver in self.sorted_versions)
        last_date = max(ver["end_of_life_date"] for ver in self.sorted_versions)

        def date_to_x(date: dt.date) -> float:
            """Convert datetime.date to an SVG X coordinate"""
            num_days = (date - first_date).days
            total_days = (last_date - first_date).days
            ratio = num_days / total_days
            x = ratio * (DIAGRAM_WIDTH - LEGEND_WIDTH - RIGHT_MARGIN)
            return x + LEGEND_WIDTH

        def year_to_x(year: int) -> float:
            """Convert year number to an SVG X coordinate of 1st January"""
            return date_to_x(dt.date(year, 1, 1))

        def format_year(year: int) -> str:
            """Format year number for display"""
            return f"'{year % 100:02}"

        with open(
            "include/release-cycle.svg", "w", encoding="UTF-8", newline="\n"
        ) as f:
            template.stream(
                SCALE=SCALE,
                diagram_width=DIAGRAM_WIDTH,
                diagram_height=(len(self.sorted_versions) + 2) * LINE_HEIGHT,
                years=range(first_date.year, last_date.year),
                LINE_HEIGHT=LINE_HEIGHT,
                versions=list(reversed(self.sorted_versions)),
                today=dt.date.today(),
                year_to_x=year_to_x,
                date_to_x=date_to_x,
                format_year=format_year,
            ).dump(f)


def main() -> None:
    versions = Versions()
    versions.write_csv()
    versions.write_svg()


if __name__ == "__main__":
    main()
