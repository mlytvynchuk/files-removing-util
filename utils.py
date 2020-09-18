import os
from os import listdir, walk
from queue import Queue


class RemovingBakFilesUtil:
    """
        Util that removes all .bak files from the given folder.
    """

    def __init__(self, dir_path: str, is_delete_empty_folders: bool):
        """
            :param dir_path: a root folder path where we want to delete .bak files.
            :param is_delete_empty_folders: If true -> removes all empty folders, if not -> does not remove.
        """
        self.dir_path = dir_path
        self.is_delete_empty_folders = is_delete_empty_folders

    def set_dir_path(self, dir_path: str):
        self.dir_path = dir_path

    def set_delete_empty_folders(self, is_delete_empty_folders):
        self.is_delete_empty_folders = is_delete_empty_folders

    def execute(self):
        """ Removes .bak files and empty folders if is_delete_empty_folders is true. """
        for (dirpath, _, file_names) in walk(self.dir_path, topdown=False):
            for f_name in file_names:
                if str.endswith(f_name, ".bak"):
                    # Removing a file from the directory.
                    os.remove(dirpath + "/" + f_name)

            # Removing empty folders if delete_empty_folders is true.
            if self.is_delete_empty_folders and not os.listdir(dirpath):
                os.rmdir(dirpath)
