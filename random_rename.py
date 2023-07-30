"""Random File Name Renamer.

Usage:
  random_rename.py [--length=<length>] [--extension=<extension>] <directory>

Options:
  -h, --help              Show this help message and exit.
  --length=<length>       The length of the random filename. Default is 10.
  --extension=<extension> The file extension to consider. Default is '.png'.
"""

import os
import random
import string
from docopt import docopt

def generate_random_filename(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def rename_files_with_random_names(directory, extension='.png', length=10):
    os.chdir(directory)
    files = [file for file in os.listdir('.') if file.endswith(extension)]

    for old_filename in files:
        new_filename = generate_random_filename(length) + extension
        os.rename(old_filename, new_filename)

def main():
    args = docopt(__doc__)

    directory_path = args['<directory>']
    length = int(args['--length'] or 10)
    extension = args['--extension'] or '.png'

    rename_files_with_random_names(directory_path, extension=extension, length=length)

if __name__ == "__main__":
    main()
