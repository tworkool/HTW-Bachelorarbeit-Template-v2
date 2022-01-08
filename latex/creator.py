import os
import sys
import pyperclip


def find_file(directory, file_name):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if file_name in basename:
                extension = basename.split('.')
                extension = extension[len(extension) - 1]
                fl_name = basename.replace(f'.{extension}', "")
                return root, basename, fl_name, extension


def generate_latex():
    try:
        if sys.argv and len(sys.argv) > 1:
            out = None
            print("INFO: found argument ", sys.argv[1])
            cur_path = os.path.dirname(os.path.abspath(__file__))
            file_name = input()
            if "-c" in sys.argv[1]:
                new_path = f"{cur_path}/code"
                basepath, full, short, ext = find_file(
                    new_path, file_name.strip())
                short_basepath = basepath.replace(new_path, "")
                short_basepath_and_file = f'code{short_basepath}/{full}'
                out = f'\codefull{{code:{short}}}{{XXXXX}}{{{ext}}}{{{short_basepath_and_file}}}'
            elif "-a" in sys.argv[1]:
                new_path = f"{cur_path}/abb"
                basepath, full, short, ext = find_file(
                    new_path, file_name.strip())
                short_basepath = basepath.replace(new_path, "")
                short_basepath_and_file = f'abb{short_basepath}/{short}'
                out = f'\\begin{{figure}}[H]\n\t\\centering\n\t\\includegraphics[width=1.0\\textwidth]{{{short_basepath_and_file}}}\n\t\\caption{{XXXXXX}}\n\t\\label{{img:{short}}}\n\\end{{figure}}'
            else:
                print(f"ERROR: INVALID ARGUMENT, -a for images, -c for code")
                return
            print("----------------")
            print(out)
            print("----------------")
            pyperclip.copy(out)
        else:
            print(f"ERROR: NO ARGUMENT FOUND")

    except Exception:
        print(f"ERROR: NO FILE FOUND")


generate_latex()
