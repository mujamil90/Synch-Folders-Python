import os
import time
import argparse
from file_util import compare_files, compare_folders

parser = argparse.ArgumentParser()
parser.add_argument("--log_file", "-log", type=str, required=True)
parser.add_argument("--source_folder", "-source", type=str, required=True)
parser.add_argument("--replica_folder", "-replica", type=str, required=True)
parser.add_argument("--polling_time", "-sync_interval", type=int, required=True)
args = parser.parse_args()
LOG = args.log_file


# function area
# -------------------------------------------------------------

def log(message):
    # write log
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(LOG, 'a') as f:
        f.write('[' + now + ']' + message + '\n')
        print('[' + now + ']' + ' ' + message)


def check_folder(folder_1) -> object:
    if os.path.isdir(folder_1):
        log(folder_1 + ' : ONLINE')
    else:
        log(folder_1 + ' is not exist')
        return


def check_file_hash_source_backup(source_folder, replica_folder, sync_time):
    countSync = 0
    updateFile = 0
    deleteFile = 0

    # get all file in folder
    files = os.listdir(source_folder)
    # get all file in backup
    files_backup = os.listdir(replica_folder)
    # compare 2 list
    for file in files_backup:
        if file in files:
            if compare_files(source_folder + '/' + file, replica_folder + '/' + file):
                log(f'{file} is up to date')
                countSync += 1
            else:
                # copy file from folder to backup
                updateFile += 1
                os.remove(replica_folder + '/' + file)
                os.system('cp ' + source_folder + '/' + file + ' ' + replica_folder)
                log(f'{file} is updated')
        if file not in files:
            # delete file in backup
            log(f'{file} is deleted')
            deleteFile += 1
            os.remove(replica_folder + '/' + file)

    for file in files:
        if file not in files_backup:
            # copy file from folder to backup
            updateFile += 1
            log(f'{file} is copied')
            os.system('cp ' + source_folder + '/' + file + ' ' + replica_folder)

    log(f' sync: {countSync}; update: {updateFile}; delete: {deleteFile};')

    # sleep for the
    time.sleep(sync_time)


# ------------------------------------------------------------------

log('Start')
source = args.source_folder
replica = args.replica_folder
sync_interval = args.polling_time

# check if folder is exist
if not os.path.isdir(source):
    log(source + ' : NOT FOUND')
    exit()
# check if backup is exist
if not os.path.isdir(replica):
    log(replica + ' : NOT FOUND')
    exit()

# run loop with interval of seconds passed via cmd args
while True:
    # check if folder is same with backup
    if compare_folders(source, replica):
        log('file is up to date')
        # sleep for seconds passed via cmd args
        time.sleep(sync_interval)
        continue
    # check source folder
    check_folder(source)
    # check replica folder
    check_folder(replica)
    # check file hash in folder and compare with backup
    check_file_hash_source_backup(source, replica, sync_interval)
