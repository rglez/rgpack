# Created by rglez at 10/12/24
"""
General functions
"""
import fnmatch
import os
from collections import defaultdict


def recursive_defaultdict():
    """
    A recursive datastructure based on defaultdict

    Returns:
        a recursive defaultdict
    """
    return defaultdict(recursive_defaultdict)


def check_path(path, check_exist=True):
    """
    Check existence of a given path

    Args:
        path: path to check
        check_exist: check if path exists or not
    """
    path_exists = os.path.exists(path)
    if check_exist and path_exists:
        return path
    elif (not check_exist) and (not path_exists):
        return path
    elif (not check_exist) and path_exists:
        return path  # todo: check this behaviour
    elif check_exist and (not path_exists):
        raise ValueError(f'\nNo such file or directory: {path}')
    else:
        pass
        raise ValueError(
            f'\nPath already exists and will not be overwritten: {path}')


def recursive_finder(pattern, root=os.curdir):
    """
    Find files named following a pattern recursively from a root path

    Args:
        pattern: file name pattern
        root: start the search recursively from this path
    """
    for path, dirs, files in os.walk(os.path.abspath(root), followlinks=True):
        if dirs:
            for dir_ in dirs:
                recursive_finder(dir_)
        for filename in fnmatch.filter(files, pattern):
            yield os.path.join(path, filename)
