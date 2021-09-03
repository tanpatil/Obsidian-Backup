# obsidian-backup
A simple solution for obsidian backups to GitHub and other cloud solutions in different formats


# Why is this necessary?

I wanted to backup all my Obsidian data to either OneDrive or Google Drive using the desktop backup and sync clients. However, the problem is that Obsidian saves data to the disk way too frequently, and as soon as the cloud solution sees the diff, it goes ahead and syncs it. This is an unnecessary process that causes problems with memory and also runs a higher risk of damaging the files itself in frequent R/W. 

This script essentially gets rid of that problem by only backing up whenever you want to. If you're working with extremely important data or just can't be bothered with manual backups, you could also set up a cron job to do it for you.

Another additional plus point is if you don't trust the cloud storage / git with your data, you can go ahead and encrypt your data locally before using a cloud solution. Whatever floats your boat.

## Why encrypt?

Even if you trust your cloud solution with everything, you absolutely should not trust it with this can contain some pretty private and damning information, if someone does pick it up. Simple AES encryption should do the trick.

# Why Python?

Python is the language that I understand well and is easily cross platform compatible. One only needs to change the shell script to ensure that it runs on their system.

# What does the script do?

Backs up all the `.md` files to GitHub and to a local folder on your computer. This could either be a folder that is in an external harddrive or a cloud backup solution. It also backs up PDF files for convenience.
