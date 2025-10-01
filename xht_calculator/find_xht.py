from statistics import median

from page import *

import sys
from pathlib import Path

def find_xht(img_path):
    page = Page(img_path)
    page._calc_hist()
    page._find_baselines()
    page._separate_lines()
    page.save_image_with_hist_and_lines(80)

    linehts, xhts, letter_wds, letter_hts = [], [], [], []
    for l in page.lines:
        linehts.append(l.ht)
        xhts.append(l.xht)
        for c in l.letters:
            letter_wds.append(c.wd)
            letter_hts.append(c.ht)

    median_lineht = median(linehts)
    median_xht = median(xhts)
    median_letter_ht = median(letter_hts)
    median_wd = median(letter_wds)
    scale = int(48 * 48 / median_xht)

    font = Path(img_path).stem
    print(f"{font},{median_lineht},{median_xht},{median_letter_ht},{median_wd},{scale}")

def main():
    dir_path = Path(sys.argv[1])

    print(f"Font,LineHt,XHt,LetterHt,LetterWd,Scale")
    for file_path in sorted(dir_path.glob("*.tif"), key=lambda f: f.name.lower()):
        try:
            find_xht(file_path)
        except ValueError as e:
            print(f"Could not process {file_path}. ", e)

if __name__ == "__main__":
    main()
