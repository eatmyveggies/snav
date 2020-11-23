import os
from typing import List, Tuple

def discover(i) -> Tuple[List[os.DirEntry]]:
    """
    Process an iterable (result of scandir) into three
    separate lists of files, dirs and others.

    Args:
        i: a scandir iterable of os.DirEntry objects.

    Returns:
        A tuple of three items:
            dirs (list)
            files (list)
            others (list)

    """    
    # todo: potentially remove others or make it more fine grained
    files, dirs, others = list(), list(), list()
    for entry in i:
        if entry.is_file():
            files.append(entry)
        elif entry.is_dir():
            dirs.append(entry)
        else:
            others.append(entry)
    return dirs, files, others


class DirView:
    """
    A container for a scanned directory.

    Attributes:
        _path (str): the path to point to.
        _dirs, (list): list of directories in said path.
        _files, (list): list of files in said path.
        _others (list): list of other entities in said path.
    """
    def __init__(self, path: str):
        """
        Args:
            path (str): the path to point to.
        """
        self._path = path
        self._dirs, self._files, self._others = discover(os.scandir(path))

    def __iter__(self):
        return (_ for _ in self._dirs + self._files + self._others)
        