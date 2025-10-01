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

    linehts, linewds, xhts, letter_wds, letter_hts = [], [], [], [], []
    for l in page.lines:
        linehts.append(l.ht)
        linewds.append(np.nonzero(np.sum(l.arr, axis=-2))[0][-1])
        xhts.append(l.xht)
        for c in l.letters:
            letter_wds.append(c.wd)
            letter_hts.append(c.ht)

    median_lineht = median(linehts)
    max_linewd = max(linewds)
    median_xht = median(xhts)
    median_letter_ht = median(letter_hts)
    median_wd = median(letter_wds)

    font = Path(img_path).stem
    print(f"{font},{max_linewd},{median_lineht},{median_xht},{median_letter_ht},{median_wd}")

def main():
    dir_path = Path(sys.argv[1])

    print(f"Font,MaxLineWd,LineHt,XHt,LetterHt,LetterWd")
    for file_path in sorted(dir_path.glob("*.tif"), key=lambda f: f.name.lower()):
        try:
            find_xht(file_path)
        except ValueError as e:
            print(f"Could not process {file_path}. ", e)

if __name__ == "__main__":
    main()
