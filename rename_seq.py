"""
Main function that calls the functions in utils to do the rename
"""
import os
import shutil

import exception as rs_exception
import rs_logging
import utils as rs_utils
LOGGER = rs_logging.Logger.get_logger("rename_seq")


def rename_seq(path, padding=1, start=1, new_dir=None, dryrun=False):
    """ The main function that calls the functions in utils to do the rename

    Args:
        path (str): Path to the folder of images
        padding (int, optional): Padding of the frame number. Defaults to 1.
        start (int, optional): Frame number to start. Defaults to 1.
        new_dir (str, optional): Directory to copy files to. Defaults to None.
        dryrun (bool, optional): Defaults to False.

    Raises:
        rs_exception.InvalidInputError: [description]
    """

    # Make sure the path exists
    if not os.path.exists(path) or not os.path.isdir(path):
        error_msg = "Input path is not valid: {0}\n".format(path)
        error_msg += "Please make sure path exists and is a folder"
        raise rs_exception.InvalidInputError(error_msg)

    # resolve the given path to realpath
    src_dir = os.path.realpath(path)
    dst_dir = os.path.realpath(new_dir or path)
    shutil_op = shutil.move if dst_dir == src_dir else shutil.copy2
    if not dryrun and not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    # Filter away items that are not files
    files = [f for f in os.listdir(src_dir) if
             os.path.isfile(os.path.join(src_dir, f))]
    if not files:
        msg = "There are no files in {0}".format(src_dir)
        raise rs_exception.InvalidInputError(msg)

    # Group the files into sequences
    # If sequence_dict is empty then there are no files with frame number
    # in the folder
    sequence_dict = rs_utils.group_files_in_seq(files)
    if not sequence_dict:
        msg = "There are no files with frame number in {0}".format(src_dir)
        raise rs_exception.InvalidInputError(msg)

    # For each of the sequence, get a mapping from source to new name
    for sequence in sequence_dict.values():
        mappings = rs_utils.get_rename_map(sequence,
                                           padding=padding,
                                           start=start)
        if dryrun:
            # Dryrun mode. Print out the src --> dst mapping
            for src, dst in mappings:
                LOGGER.info("{0} --> {1}".format(os.path.join(path, src),
                                                 os.path.join(dst_dir, dst)))
        else:
            TEMP_SUFFIX = ".temp"
            clashed_names = []
            for src, dst in mappings:
                src_full_path = os.path.join(path, src)
                # src in clashed names has been appended with TEMP_SUFFIX
                if src in clashed_names:
                    src_full_path = src_full_path + TEMP_SUFFIX

                dst_full_path = os.path.join(dst_dir, dst)

                # Before renaming, check that dst does not exist and move to a
                # temp filename. Assume temp file name does not exist.
                if os.path.exists(dst_full_path):
                    clashed_names.append(dst)
                    shutil.move(dst_full_path, dst_full_path + TEMP_SUFFIX)

                shutil_op(src_full_path, dst_full_path)

    LOGGER.info("Finished renaming files")
