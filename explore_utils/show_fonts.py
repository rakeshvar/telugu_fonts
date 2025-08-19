import base64
import sys

from io import BytesIO
from tqdm import tqdm
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

sys.path.append(str(Path(__file__).parent.parent))
from scribe_pango_backend import scribe_text
from fonts import font_properties
from font_faces import font_faces

def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

################################################################################ HTML Writer
html_head = """
<!DOCTYPE html>
<html>
<head>
    <title>Font Samples</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .font-sample { margin: 20px 0; border: 1px solid #ccc; padding: 10px; }
        .font-name { font-weight: bold; margin-bottom: 5px; }
    </style>
</head>
<body>
    <h1>Font Samples</h1>
"""

html_tail = "</body></html>"

class HTMLWriter:
    """
    Writes output to a html file. Fonts, properties info and a sample image.
    """
    def __init__(self, out_html):
        self.out_html = out_html
        self.content = []

    def __enter__(self):
        self.content.append(html_head)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.content.append(html_tail)
        with open(self.out_html, "w") as f:
            f.writelines(self.content)
        print(f"Saved HTML {self.out_html}")

    def add_image(self, font, img_base64, info, style="", style_color="black"):
        self.content.append(f"""
        <div class="font-sample">
            <div class="font-name">{font} <span style="color: {style_color};">{style}</span> {info}</div>
            <img src="data:image/png;base64,{img_base64}" alt="{font}">
        </div>""")

    def add_font_text(self, font, style, size, text, sytle_color="black"):
        css = f"font-family: '{font}'; font-size: {size}px;"
        style_lower = style.lower().strip()

        if "bold" in style_lower:
            css += " font-weight: bold;"
        elif style_lower in ("regular", "normal", ""):
            css += " font-weight: normal;"

        if "italic" in style_lower:
            css += " font-style: italic;"
        else:
            css += " font-style: normal;"

        self.content.append(f"""<div class='font-sample'><div style=\"{css}\">{font} {style} {size}px {text}</div></div>""")

    def add_text(self, text, style, aux="<hr>"):
        self.content.append(f"{aux}<{style}>{text}</{style}>\n")

################################################################################ Saving Fonts from List

def print_faces_html_text(font_names_list, out_html, text, size=0):
    """
    Print all the font faces in the list to a html file
    """
    out_html_path = Path(out_html).with_suffix(".html")
    with HTMLWriter(out_html_path) as h:
        for font_name in tqdm(font_names_list):
            h.add_text(font_name, "h2")
            sz, gho, rep, ppu, sp, bold, abbr = font_properties[font_name]
            faces_orig = font_faces[font_name]
            faces = set(faces_orig + ["", "Regular", "Bold", "Italic", "Bold Italic"])
            use_sz = sz if size==0 else size
            for face in faces:
                font_style = f"{font_name} {face} {use_sz}"
                print(f"Adding {font_style}")
                h.add_font_text(font_name, face, use_sz, text, "green" if face in faces_orig else "red")

################################################################################ Saving Fonts from List

def print_faces(font_names_list, out_html, text, width, height, size):
    """
    Print all the font faces in the list to a html file
    """
    out_html_path = Path(out_html).with_suffix(".html")
    with HTMLWriter(out_html_path) as h:
        for font_name in tqdm(font_names_list):
            h.add_text(font_name, "h2")
            sz, gho, rep, ppu, sp, bold, abbr = font_properties[font_name]
            faces_orig = font_faces[font_name]
            faces = set(faces_orig + ["", "Regular", "Bold", "Italic", "Bold Italic"])
            use_sz = sz if size==0 else size
            for face in faces:
                font_style = f"{font_name} {face} {use_sz}"
                print(f"Adding {font_style}")
                img = scribe_text(text, font_style, width, height, 10, 10)
                img = Image.fromarray(255-img, "L")
                img_base64 = image_to_base64(img)
                h.add_image(font_name, img_base64, font_properties[font_name], face,
                            "green" if face in faces_orig else "red")


def save_images_from_list(font_names, out_folder, sample_text, width, height, sz):
    """
    Save samples of all the fonts to images in out_folder
    """
    out_folder = Path(out_folder)
    out_folder.mkdir(exist_ok=True)
    for font_name in font_names:
        size = font_properties[font_name][0] if sz==0 else sz
        font_style = f"{font_name} {size}"
        tif_file = out_folder / f"{font_name}.tif"
        print(f"Saving {font_style} to image {tif_file}")

        img = scribe_text(sample_text, font_style, width, height, 10, 10)
        img = Image.fromarray(255 - img)
        img.save(tif_file)

#################################################################################### Saving from a directory

def get_font_names(ttfont):
    """
    Get all the font faces in a TTF font from TTfont library
    """
    names = set()
    for record in ttfont['name'].names:
        if record.nameID in (1, 4):  # 1=Family, 2=Subfamily, 4=Full name
            try:
                name_str = record.string.decode(record.getEncoding())
            except:
                name_str = record.string
            names.add((record.nameID, name_str))

    return " ".join([f"{'' if i==1 else '﹥'}{n}" for i, n in sorted(list(names), key=lambda x: x[0])])


def get_font_info(font_path):
    font = TTFont(font_path)
    cmap = font['cmap'].getBestCmap()
    nchars = len([chr(cp) for cp in cmap.keys()])
    return f"{font_path} {nchars} {get_font_names(font)}"

def generate_font_sample_pil(font_path, sample_text, width, height, size):
    font = ImageFont.truetype(str(font_path), size)
    image = Image.new("L", (width, height), 255)
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), sample_text, font=font, fill=0)
    return image

def print_folder(font_folder, out_html, text, width, height, size):
    """
    Generates a html file with sample text rendered in all the fonts in a given folder
    """
    font_folder_path = Path(font_folder)
    out_html_path = Path(out_html).with_suffix(".html")

    found_fonts = []
    for ext in ['*.ttf', '*.otf', '*.woff', '*.woff2']:
        found_fonts.extend(font_folder_path.rglob(ext))

    with HTMLWriter(out_html_path) as h:
        for font_path in found_fonts:
            print("Printing ", font_path)
            img = generate_font_sample_pil(font_path, text, width, height, size)
            img_base64 = image_to_base64(img)
            h.add_image(font_path, img_base64, get_font_info(font_path))

def save_images_from_folder(font_folder, out_folder, text, width, height, size):
    """
    Save samples of all the fonts in a given directory to images in out_folder
    """
    font_folder_path = Path(font_folder)
    found_fonts = []
    for ext in ['*.ttf', '*.otf', '*.woff', '*.woff2']:
        found_fonts.extend(font_folder_path.rglob(ext))

    out_folder = Path(out_folder)
    out_folder.mkdir(exist_ok=True)
    for font_path in found_fonts:
        tif_file = out_folder / f"{font_path.stem}.tif"
        print(f"Saving {font_path} to image {tif_file}")
        img = generate_font_sample_pil(font_path, text, width, height, size)
        img.save(tif_file)

####################################################################################
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Render (Telugu) fonts from a predefined list or from a directory, and output as HTML or images.")

    # Mutually exclusive: predefined list 'telugu' or a directory
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-T", "--telugu", action="store_true",
        help="Use the predefined list of Telugu fonts.")
    group.add_argument("-D", "--dir", type=str,
        help="Path to a directory containing TTF font files.")

    # Output type
    parser.add_argument("-O", "--output-type", choices=["embedded", "css", "images"], required=True,
        help="""Choose whether to output as 
        - embedded : one html file with embedded images 
        - css     : one html file with text and css
        - images   : separate images in the output folder
        """)
    # Output paths depending on type
    def_out = "out"
    parser.add_argument("-P", "--output-path", type=str, default=def_out,
        help=f"Path to output HTML or Image Folder. Default={def_out}.html or {def_out}/")

    # Sample text input
    sample_group = parser.add_mutually_exclusive_group(required=True)
    sample_group.add_argument("-s", "--sample-text", type=str,
        help="Sample text to render.")
    sample_group.add_argument("-f", "--sample-file", type=str,
        help="File containing sample text to render.")

    # Rendering parameters
    def_w, def_h, def_z = 600, 300, 72
    parser.add_argument("-W", "--width", type=int, default=def_w,
        help=f"Image width in pixels. Default={def_w}")
    parser.add_argument("-H", "--height", type=int, default=def_h,
        help=f"Image height in pixels. Default={def_h}")
    parser.add_argument("-Z", "--size", type=int, default=def_z,
        help=f"Font size. Default={def_z}. Give 0 for using size from properties.")

    args = parser.parse_args()

    # Get sample text
    sample_text = "Text not Specified."
    if args.sample_text:
        sample_text = args.sample_text
    elif args.sample_file:
        with open(args.sample_file, "r", encoding="utf-8") as f:
            sample_text = f.read().strip()

    # Decide font sources
    if args.telugu:
        fonts_list = sorted(font_properties.keys())
        # Routing based on output type
        if args.output_type == "embedded":
            print(f"Rendering {len(fonts_list)} fonts to HTML at {args.output_path} as embedded images.")
            print_faces(fonts_list, args.output_path, sample_text, args.width, args.height, args.size)

        elif args.output_type == "images":
            print(f"Rendering {len(fonts_list)} fonts as tif images into {args.output_path} .")
            save_images_from_list(fonts_list, args.output_path, sample_text, args.width, args.height, args.size)

        elif args.output_type == "css":
            print(f"Rendering {len(fonts_list)} fonts to HTML at {args.output_path} with CSS styles.")
            print_faces_html_text(fonts_list, args.output_path, sample_text, args.size)

    else:
        if args.output_type == "embedded":
            print(f"Rendering fonts in {args.dir} to HTML at {args.output_path}")
            print_folder(args.dir, args.output_path, sample_text, args.width, args.height, args.size)

        elif args.output_type == "images":
            print(f"Rendering fonts in {args.dir} as images into {args.output_path}")
            save_images_from_folder(args.dir, args.output_path, sample_text, args.width, args.height, args.size)

if __name__ == "__main__":
    main()
