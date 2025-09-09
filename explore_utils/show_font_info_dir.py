
import os, sys
from fontTools.ttLib import TTFont

def contains_telugu(text):
    return any('\u0c00' <= ch <= '\u0c7f' for ch in text)

def get_font_names(font):
    names = set()
    for record in font['name'].names:
        if record.nameID in (1, 4):  # 1=Family, 2=Subfamily, 4=Full name
            try:
                name_str = record.string.decode(record.getEncoding())
            except:
                name_str = record.string
            names.add((record.nameID, name_str))

    return " ".join([f'{"" if i==1 else "﹥"}{n}' for i, n in sorted(list(names), key=lambda x: x[0])])


# Information about fonts in directory
def show_font_info_dir(folder, show_all=False):
    print("############## ", folder)
    for file in sorted(os.listdir(folder), key=str.lower):
        if not file.lower().endswith((".ttf", ".otf", ".woff", ".woff2")):
            continue
        path = os.path.join(folder, file)

        try:
            font = TTFont(path)

            # Get supported characters
            cmap = font['cmap'].getBestCmap()
            chars = [chr(cp) for cp in cmap.keys()]
            charstr = ''.join(chars)

            # Check if variable font
            is_variable = 'fvar' in font

            if show_all or contains_telugu(charstr): # or is_variable:
                print(f"\n{file}:\t {get_font_names(font)}", )
                if contains_telugu(charstr):
                    print("\tContains TELUGU")
                print(f"\tCharacters: {len(chars):3d} : {charstr}")
                if is_variable:
                    print("\tVariable font axes: #############################################################")
                    for axis in font['fvar'].axes:
                        print(f"\t  - {axis.axisTag}: {axis.minValue} → {axis.maxValue} (default {axis.defaultValue})")

        except Exception as e:
            print(f"Error reading {file}: {e}")

# Main script
if __name__ == "__main__":
    show_font_info_dir(sys.argv[1], show_all=True)
