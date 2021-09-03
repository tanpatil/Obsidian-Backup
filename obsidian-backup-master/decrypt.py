"""
Decrypts a folder of obsidian data for others to use.
"""


def decrypt_file(fern, filer):
    """
    Decrypt a given file with a fernet object and a path
    """
    with open(filer, 'rb') as f:
        enc = f.read()
    dec = fern.decrypt(enc)
    with open(filer, 'wb') as f:
        f.write(dec)