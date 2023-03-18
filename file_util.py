import hashlib
import os


def compare_files(file1, file2):
    # compare two files with hash
    with open(file1, 'rb') as f1:
        with open(file2, 'rb') as f2:
            if hashlib.md5(f1.read()).hexdigest() == hashlib.md5(f2.read()).hexdigest():
                return True
            else:
                return False


def compare_folders(source_folder, replica):
    # compare hash folder
    # return True if all file is same
    # return False if any file is different
    # get all file in folder
    files = os.listdir(source_folder)
    # get all file in backup
    files_backup = os.listdir(replica)
    # compare 2 list
    if len(files) != len(files_backup):
        return False

    for file in files:
        if file in files_backup:
            if not compare_files(source_folder + '/' + file, replica + '/' + file):
                return False
        else:
            return False
    return True
