"""
Utils functions for rename_seq
"""
import re

from rename_seq import rs_logging
LOGGER = rs_logging.Logger.get_logger("rename_seq")

# Regex constant to save processing time as it will be used multiple times
PATTERN = "\\.\\d*\\."
PROG = re.compile(PATTERN)


def _frame_key(name):
    """ Get the frame number for sorting

    Args:
        name (str): Name of the file

    Returns:
        int: The frame number in integer
    """
    match = PROG.search(name)
    if not match:
        return -1
    return int(match.group(0)[1:-1])


def group_files_in_seq(files):
    """ Group the files into respective sequences
        Example:
            Input: ["abc.10.jpg", "abc.23.jpg", "xyz.10.jpg"]
            Output: {"abcjpg": ["abc.10.jpg", "abc.23.jpg"]
                     "xyzjpg": ["xyz.10.jpg"]}
        Folders or files that does not contain a frame token will be discarded
    Args:
        files (list[str]): List of file names

    Returns:
        dict[str, list[str]]: Groups of files
    """
    result = dict()

    # Loop through the files and group them into respective sequences
    for f in files:
        match = PROG.search(f)
        if match:
            # Add any matches to the result dict.
            key = PROG.sub("", f)
            result.setdefault(key, []).append(f)
    return result


def get_rename_map(files, padding=0, start=1):
    """ Return the mapping

    Args:
        files (list[str]): List of file names
        padding (int): Number of digits for the frame number
        start (int): Frame number to start from

    Returns:
        list[tuple[str]]: List of tuples where the first item is the source
                          file name and second item is the new file name.

    """
    result = list()
    if not files:
        LOGGER.warning("No input files given")
        return result

    # sort the files so that the rename will be in the correct order
    files.sort(key=_frame_key)

    # Loop through the files and add the source and target as tuple into result
    for i, f in enumerate(files, start=start):
        new_file_name = PROG.sub(".{0}.".format(str(i).zfill(padding)), f)
        result.append((f, new_file_name))
    return result
