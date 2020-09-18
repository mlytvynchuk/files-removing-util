from utils import RemovingFilesUtil

if __name__ == "__main__":
    is_remove_empty_folders = True
    folder_path = "/test_folder"
    folder_util = RemovingFilesUtil(
        folder_path,
        is_remove_empty_folders
    )
    folder_util.execute()
