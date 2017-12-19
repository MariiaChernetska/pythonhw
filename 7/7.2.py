import argparse
import os
'''


parser = argparse.ArgumentParser()
parser.add_argument("-path", type=str,
                    help="the folder path", default="")
parser.add_argument("-type", type=str,
                    help="file type filter", default="")
parser.add_argument("--sub",
                    help="show files in subfolders", action="store_true")
parser.add_argument("--d",
                    help="show directories", action="store_true")

args = parser.parse_args()


# print(args)


def get_files_and_directories(path, extension=".html", show_folders=False, show_subfolders_content=True):
    if show_subfolders_content:
        for rootdir, dirs, files in os.walk(path):
            if show_folders:
                print("-"+os.path.split(rootdir)[1])
            for file in files:
                if file.endswith(extension):
                    print("--"+file)
    else:
        content = os.listdir(path)
        files = list([file for file in os.listdir(path) if os.path.isfile(file) and file.endswith(extension)])

        if show_folders: print(content)
        else: print(files)


res = get_files_and_directories("/home/mchernetska/PythonProjects/pythonhw")

'''