"""
A simple script to backup a folder to either git or a local folder or to a cloud service
"""


# IMPORTS
from dotenv import load_dotenv
from cryptography.fernet import Fernet
from os import listdir, write
from os.path import isfile, join
import os

# load env vars
load_dotenv()

        
def write_key():
    """
    write a new key to the key location when needed.
    """
    key = Fernet.generate_key()
    with open(os.getenv("KEY_PATH"), "wb+") as key_file:
        key_file.write(key)


def load_key():
    """
    Check whether a key exists, and if it does, go ahead and return it. Else, go ahead make a new key and write it down again.
    """
    k = os.getenv("KEY_PATH")
    if isfile(k):
        pass
    else:
        write_key()
    return open(k, "rb").read()


def encrypt_file(fern, filer):
    """
    Encrypt a given file with the fernet object and a path
    """
    with open(filer, 'rb') as f:
        o = f.read()
    enc = fern.encrypt(o)
    with open(filer, 'wb') as f:
        f.write(enc)
    return

def decrypt_file(fern, filer):
    """
    Decrypt a given file with a fernet object and a path
    """
    with open(filer, 'rb') as f:
        enc = f.read()
    dec = fern.decrypt(enc)
    with open(filer, 'wb') as f:
        f.write(dec)
    return

def encrypt():
    """
    In order to avoid messing with the main file system, we will not directly modify the files. Instead, we will make a copy of those files elsewhere, and start to modify those files. 

    Hence, the first process will be to copy the files to a backup path.
    """
    bck_path = os.getenv("TMP_PATH")
    # now we get al the files available
    onlyfiles = [f for f in listdir(bck_path) if isfile(join(bck_path, f))]
    fern = Fernet(load_key())
    # let us loop through the files and encrypt each induvidually
    for i in onlyfiles:
        encrypt_file(fern, join(bck_path, i))
    return

def folder_backup():
    """
    Copies all the files in the source directory to a specified backup directory
    """
    doc_path = os.getenv("OBSIDIAN_FOLDER")
    bck_path = os.getenv("TMP_PATH")
    os.system(f"cp -R {doc_path} {bck_path}")
    return

def folder_delete():
    """
    Deletes the tmp folder after completion
    """
    bck_path = os.getenv("TMP_PATH")
    os.system(f"rm -rf {bck_path}")
    return 

def final_copy():
    """
    Copies the temp to the specified folder location for cloud storage / local storage backup
    """
    bck_path = os.getenv("TMP_PATH")
    local_path = os.getenv("BACKUP_FOLDER")
    os.system(f"cp -R {bck_path} {local_path}")

def git_copy():
    bck_path = os.getenv("TMP_PATH")
    git_path = os.getenv("GIT_FOLDER")
    git_repo = os.getenv("GIT_REPO")
    if os.path.isdir(git_path):
        # mainly to get rid of any outliers or changes
        os.system(f'cd {git_path} && git add . && git commit -m "backup" && git pull && git push')
    else:
        os.system(f'git clone {git_repo} {git_path}')
    
    # now we will copy the folder path as a whole
    os.system(f"cp -R {bck_path} {git_path}")
    os.system(f'cd {git_path} && git add . && git commit -m "backup" && git pull && git push')

    
def backup_to_loc():
    """
    We will check the encrypt flag first.
    If true, we will be sure to perform encryption.
    Else, we will just go ahead normally.
    """
    folder_backup() # to create a temp folder
    if os.getenv("ENCRYPT") == "YES":
        # we need to proceed with encryption
        encrypt()
    else:
        pass
    if os.getenv("FOLDER_BACKUP").upper() in "YES":
        final_copy()
    if os.getenv("GIT_BACKUP").upper() in "YES":
        git_copy()
    # folder_delete()



backup_to_loc()

