"""
Various functions to check, manaage, and explore Telugu fonts
    and system fonts.
"""
from fonts import font_properties as tel_font_dict

from gi.repository import PangoCairo
system_font_families = PangoCairo.font_map_get_default().list_families()
system_font_families = sorted(system_font_families, key=lambda f: f.get_name().lower())
system_font_families_dict = {f.get_name():f for f in system_font_families}
system_font_names = sorted(system_font_families_dict.keys())

def get_faces_of_family(font_family):
    return [ff.get_face_name() for ff in font_family.list_faces()]

def get_faces_of_font(font):
    return get_faces_of_family(system_font_families_dict[font])

####################################################################################

def lookup_system_fonts_in_telugu_list():
    """
    Go through all the fonts on the system and sees if they are present in the telugu fonts dictionary.
    :return:
    """
    for sys_font in sorted(system_font_names):
        if sys_font in tel_font_dict:
            print(f"\n[✓]{sys_font} ({tel_font_dict[sys_font]})", end="\t")
        else:
            print(f"[X]{sys_font}", end='\t')

####################################################################################

def lookup_telugu_fonts_in_system():
    """
    For all the Telugu fonts, it looks up in two places:
        - the font_map of PangoCairo
        - the font-cache of the system (in posix)
    """
    import subprocess
    for tel_font in sorted(tel_font_dict.keys()):
        if tel_font in system_font_names:
            print(f"\n[✓]{tel_font} : {get_faces_of_font(tel_font)}")

        else:
            print(f"\n[X]{tel_font} NOT INSTALLED\n")

        escaped_myfont = tel_font.replace('-', '\\\\\\\\-')
        command = f'fc-list | grep "{escaped_myfont}"'
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        print(result.stdout)

####################################################################################

def write_system_font_families_to_txt(out_file_name="system_font_families.txt"):
    with open(out_file_name, "w", encoding="utf-8") as file:
        for family in system_font_families:
            file.write(f"{family.get_name()} : {get_faces_of_family(family)} \n")

####################################################################################

def save_telugu_font_faces(out_file_name):
    """
    Writes all the faces of all the Telugu fonts to a file like font_faces.py
    """
    with open(out_file_name, "w", encoding="utf-8") as file:
        file.write("font_faces = {\n")
        for tel_font in sorted(tel_font_dict.keys()):
            try:
                spaces = ' ' * (25 - len(tel_font))
                info = f"'{tel_font}': {spaces}{get_faces_of_font(tel_font)}, \n"
                file.write(info)
            except KeyError as e:
                print(f"\n[X]{tel_font} NOT INSTALLED\n", e)
                continue
        file.write("}")

####################################################################################

if __name__ == '__main__':
    """
    Put what ever function you are intersted in executing here.
    """
    lookup_telugu_fonts_in_system()
    save_telugu_font_faces("font_faces.py")
