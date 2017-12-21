import argparse
import os
import datetime
parser = argparse.ArgumentParser()
parser.add_argument("-d", type=str,
                    help="the folder path", default=".")
parser.add_argument("-type", type=str,
                    help="file type filter", default="")
parser.add_argument("-date", type=str,
                    help="file type filter", default="")
parser.add_argument("--sub",
                    help="show files in subfolders", action="store_true", default=False)
parser.add_argument("--dirs",
                    help="show directories", action="store_true", default=False)

args = parser.parse_args()


print(args)

def check_by_ext(files_list, ext):
    if len(ext)>0:
        return list([file for file in files_list if file.endswith(ext)])
    else:
        return files_list

def check_by_date(files_list, date_mod, root_dir):
    if len(date_mod)>0:
        date_c = datetime.datetime.strptime(date_mod, "%d/%m/%Y")
        return list([file for file in files_list if datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(root_dir,file)))<=date_c])
    else:
        return files_list


def get_files_and_directories(path, extension, date_modified, show_folders=False, show_subfolders_content=False):

    if show_subfolders_content:
        for rootdir, dirs, files in os.walk(path):
            if show_folders:

                if(rootdir == path):
                    print(os.path.split(rootdir)[1])
                else: print(str(rootdir).replace(path, ''))
            files_res =  check_by_ext(check_by_date(files, date_modified, rootdir), extension)
            for file in files_res:
                    print("\t--" + file)

    else:

        content = os.listdir(path)

        files = list([file for file in content if os.path.isfile(os.path.join(path,file))])

        if show_folders:
            for item in content:
                if os.path.isdir(os.path.join(path,item)):
                    print(item)

        files_res = check_by_ext(check_by_date(files, date_modified, path), extension)
        for file in files_res:
            print("\t--" + file)


res = get_files_and_directories(args.d, args.type, args.date, args.dirs, args.sub)


