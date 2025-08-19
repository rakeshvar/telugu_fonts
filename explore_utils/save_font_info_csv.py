
import os, sys
from fontTools.ttLib import TTFont

def contains_telugu(text):
    return any('\u0c00' <= ch <= '\u0c7f' for ch in text)

def get_font_names(font):
    names1 = set()
    names4 = set()
    for record in font['name'].names:
        if record.nameID in (1, 4):  # 1=Family, 2=Subfamily, 4=Full name
            try:
                name_str = record.string.decode(record.getEncoding())
            except:
                name_str = record.string
            if record.nameID == 1:
                names1.add(name_str)
            elif record.nameID == 4:
                names4.add(name_str)
    
    return ";".join(sorted(names1)), ";".join(sorted(names4))


# Information about fonts in directory
def font_info_dir(folder):
    entries = []

    for root, dirs, files in os.walk(folder):
        if "archive" in root.lower():
            print(f"Skipping {root} folder.")
            continue

        print(f"############## {root} {len(files)} files")

        for file in sorted(files, key=str.lower):
            if not file.lower().endswith((".ttf", ".otf", ".woff", ".woff2")):
                continue

            path = os.path.join(root, file)

            try:
                font = TTFont(path)

                # Get supported characters
                cmap = font['cmap'].getBestCmap()
                chars = [chr(cp) for cp in cmap.keys()]
                charstr = ''.join(chars)
                
                nchars = len(chars)
                is_variable = 'fvar' in font
                has_telugu = contains_telugu(charstr)
                has_aa = "అ" in charstr 
                names, full_names = get_font_names(font)
                size_kb = os.path.getsize(path)/1024

                entries.append(f"{names},{full_names[:50]},{nchars},{size_kb:.2f},{has_telugu},{has_aa},{file},{root}")

            except Exception as e:
                print(f"Error reading {path}: {e}")
    
    return entries


# Main script
if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv) > 1 else "."
    out_csv = sys.argv[2] if len(sys.argv) > 2 else "font_info.csv"
    entries = font_info_dir(folder) 
    with open(out_csv, "w", encoding="utf-8") as f:
        f.write("Name,Style,Count,Size_KB,Telugu,Has_Aa,File,Folder\n")
        for entry in entries:
            f.write(entry + "\n")

