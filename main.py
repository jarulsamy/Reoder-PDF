import argparse
from pathlib import Path

from pyfiglet import Figlet

from ReorderPDF import reorder

ap = argparse.ArgumentParser()
ap.add_argument(
    "-i", "--input", required=True, help="Input path to PDF doc.",
)

ap.add_argument(
    "-o", "--output", required=False, help="Optional output path of file.",
)

ap.add_argument(
    "-p",
    "--page_order",
    nargs="+",
    type=int,
    required=False,
    help="Whitespace seperate list of numbers to use as a pageorder, start at 1",
)


args = vars(ap.parse_args())

f = Figlet()
print(f.renderText("Reorder PDF"))

filename = Path(args["input"])

if not filename.is_file:
    raise ValueError(f"Cannot open {filename}.")

reorder(filename, output_filename=args["output"], page_order=args["page_order"])
