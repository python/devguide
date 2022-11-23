"""
Read in a JSON and generate two CSVs and a Mermaid file
"""
from __future__ import annotations

import csv
import datetime as dt
import json

MERMAID_HEADER = """
gantt
    dateFormat  YYYY-MM-DD
    title       Python release cycle
    axisFormat  %Y
""".lstrip()

MERMAID_SECTION = """
    section Python {version}
    {release_status}               :{mermaid_status}   python{version}, {release_date},{eol}
"""  # noqa: E501

MERMAID_STATUS_MAPPING = {
    "feature": "",
    "bugfix": "active,",
    "security": "done,",
    "end-of-life": "crit,",
}

CSV_HEADER = (
    "Branch",
    "Schedule",
    "Status",
    "First release",
    "End of life",
    "Release manager",
)


def pep(number: int) -> str:
    """Format PEP number with Sphinx role"""
    return f":pep:`{number}`"


def csv_date(date_str: str, now_str: str) -> str:
    """Format a date for CSV"""
    if date_str > now_str:
        # Future, add italics
        return f"*{date_str}*"
    return date_str


def mermaid_date(date_str: str) -> str:
    """Format a date for Mermaid"""
    if len(date_str) == len("yyyy-mm"):
        # Mermaid needs a full yyyy-mm-dd, so let's approximate
        date_str = f"{date_str}-01"
    return date_str


class Versions:
    """For converting JSON to CSV and Mermaid"""

    def __init__(self) -> None:
        with open("include/release-cycle.json") as f:
            self.versions = json.load(f)

    def save_csv(self) -> None:
        """Output CSV files"""
        now_str = str(dt.datetime.utcnow())

        with (
            open(
                "include/branches.csv", "w", encoding="UTF-8", newline=""
            ) as file_branches,
            open(
                "include/end-of-life.csv", "w", encoding="UTF-8", newline=""
            ) as file_eol,
        ):
            csv_branches = csv.writer(
                file_branches, quoting=csv.QUOTE_MINIMAL, lineterminator="\n"
            )
            csv_eol = csv.writer(
                file_eol, quoting=csv.QUOTE_MINIMAL, lineterminator="\n"
            )

            csv_branches.writerow(CSV_HEADER)
            csv_eol.writerow(CSV_HEADER)

            sorted_versions = sorted(
                self.versions.items(),
                key=lambda k: int(k[0].replace(".", "")),
                reverse=True,
            )
            for version, details in sorted_versions:
                row = (
                    details["branch"],
                    pep(details["pep"]),
                    details["status"],
                    csv_date(details["release_date"], now_str),
                    csv_date(details["eol"], now_str),
                    details["release_manager"],
                )

                if details["status"] == "end-of-life":
                    csv_eol.writerow(row)
                else:
                    csv_branches.writerow(row)

    def save_mermaid(self) -> None:
        """Output Mermaid file"""
        out = [MERMAID_HEADER]

        for version, details in reversed(self.versions.items()):
            v = MERMAID_SECTION.format(
                version=version,
                release_date=details["release_date"],
                eol=mermaid_date(details["eol"]),
                release_status=details["status"],
                mermaid_status=MERMAID_STATUS_MAPPING[details["status"]],
            )
            out.append(v)

        with open(
            "include/release-cycle.mmd", "w", encoding="UTF-8", newline="\n"
        ) as f:
            f.writelines(out)


def main() -> None:
    versions = Versions()
    versions.save_csv()
    versions.save_mermaid()


if __name__ == "__main__":
    main()
