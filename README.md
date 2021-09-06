A python library for renaming (or copying) image sequence.

## Compatibility
This tool has been tested on Ubuntu python2 and python3

## Setup
Move the folder `rename_seq` into one of the folder specified in the PYTHONPATH
or add the path to rename_seq folder into PYTHONPATH.
Also add the path to PATH so that you can execute the rename_seq directly
```
export PYTHONPATH=$PYTHONPATH:/path/to/rename_seq
export PATH=$PATH:/path/to/rename_seq
```

## Example: Basic usage
Input:
```
/path/to/images/
|-img_a.01.jpg
|-img_a.21.jpg
|-img_a.44.jpg
|-img_a.47.jpg
|-img_b.03.png
|-img_b.10.png
|-img_b.54.png
```

Usage:
```
rename_seq /path/to/images
```

Result:
```
/path/to/images/
|-img_a.1.jpg
|-img_a.2.jpg
|-img_a.3.jpg
|-img_a.4.jpg
|-img_b.1.png
|-img_b.2.png
|-img_b.3.png
```

## Example: Rename with frame padding of 4 and start from 101
Usage:
```
rename_seq --padding 4 --start 101 /path/to/images
```

Result:
```
/path/to/images/
|-img_a.0101.jpg
|-img_a.0102.jpg
|-img_a.0103.jpg
|-img_a.0104.jpg
|-img_b.0101.png
|-img_b.0102.png
|-img_b.0103.png
```

## Example: Rename and copy the files to a new folder
Usage:
```
rename_seq --new_dir /path/to/new/folder /path/to/images
```

Result:
```
/path/to/new/folder
|-img_a.1.jpg
|-img_a.2.jpg
|-img_a.3.jpg
|-img_a.4.jpg
|-img_b.1.png
|-img_b.2.png
|-img_b.3.png
```