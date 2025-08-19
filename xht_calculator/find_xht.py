from statistics import median

from page import *

import sys
from pathlib import Path

def find_xht(img_path):
    print("Processing ", img_path)
    page = Page(img_path)
    page._calc_hist()
    page._find_baselines()
    page._separate_lines()
    page.save_image_with_hist_and_lines(80)
    xhts = [l.xht for l in page.lines]
    median_xht = median(xhts)
    scale = int(48 * 48 / median_xht)
    print(f"Xhts: {xhts}, Median: {median_xht}, Scale: {scale}")

def main():
    dir_path = Path(sys.argv[1])

    for file_path in sorted(dir_path.glob("*.tif"), key=lambda f: f.name.lower()):
        try:
            find_xht(file_path)
        except ValueError as e:
            print(f"Could not process {file_path}. ", e)

if __name__ == "__main__":
    main()
