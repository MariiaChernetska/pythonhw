import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-d", type=str,
                    help="the folder path", default=".")
parser.add_argument("-type", type=str,
                    help="file type filter", default="")
parser.add_argument("--sub",
                    help="show files in subfolders", action="store_true", default=False)
parser.add_argument("--dirs",
                    help="show directories", action="store_true", default=False)

args = parser.parse_args()


print(args)


def get_files_and_directories(path, extension="", show_folders=False, show_subfolders_content=False):

    if show_subfolders_content:
        for rootdir, dirs, files in os.walk(path):
            if show_folders:

                if(rootdir == path):
                    print(os.path.split(rootdir)[1])
                else: print(str(rootdir).replace(path, ''))

            for file in files:

                if len(extension ) > 0:
                    if file.endswith(extension): print("\t--"+file)
                else: print("\t--"+file)
    else:
        content = os.listdir(path)

        files = list([file for file in content if os.path.isfile(os.path.join(path,file))])

        if show_folders:
            for item in content:
                if os.path.isdir(os.path.join(path,item)):
                    print(item)


        for file in files:

            if len(extension ) > 0:
                if file.endswith(extension): print(file)

            else:
                print(file)


res = get_files_and_directories(args.d, args.type, args.dirs, args.sub)


