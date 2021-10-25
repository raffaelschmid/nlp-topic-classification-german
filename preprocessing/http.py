import os
import wget

def download(url, filename):
    if os.path.exists(filename):
        os.remove(filename)
    wget.download(url, out=filename)