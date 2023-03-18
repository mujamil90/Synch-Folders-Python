# Sync in two folders (One way - Source to Replica)




**This script is helpful whenever you want to make automation in your offline backup for sync files.**


- Designed and written in **PYTHON 3**
- Files comparison with MD5 hash using **Hashlib**
- Passing commandline arguments with **Argparse**
- Config data i.e. log-file, source, replica and sync-interval provided via commandline
- Logging in console and log file
- Test data used doc file and pages (IOS)


---
### Platform Support
- Windows
- Macintosh

---
### Usage
```sh
$ python3 sync_files.py -log=log.txt -source=/../Source-Folder -replica=/../Replica-Folder -sync_interval=3
```
---
Note - Sync interval is in seconds.
