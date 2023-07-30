# Random File Name Renamer

The **Random File Name Renamer** is a Python script that allows you to rename files in a directory with random filenames. This script provides the flexibility to specify the file extension and the length of the random filename.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Usage](#usage)
  - [Parameters](#parameters)
  - [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before using the **Random File Name Renamer**, ensure that you have the following:

1. Python installed on your system. If you don't have Python installed, you can download it from the official website: [Python Downloads](https://www.python.org/downloads/).

## Usage

### Parameters

To run the script, use the following command:

```bash
python random_rename.py [--length=<length>] [--extension=<extension>] <directory>
```

- `--length=<length>` (optional): The length of the random filename. Default is 10 characters.
- `--extension=<extension>` (optional): The file extension to consider. Default is '.png'.

### Examples

1. Rename all files in the current directory (denoted by `.`) with random filenames of 10 characters:

```bash
python random_rename.py .
```

2. Rename all files in a specific directory (e.g., `/path/to/your/files`) with random filenames of 15 characters:

```bash
python random_rename.py /path/to/your/files --length=15
```

3. Rename only files with extension '.jpg' in a specific directory (e.g., `/path/to/your/files`):

```bash
python random_rename.py /path/to/your/files --extension=.jpg
```

