from utils import RemovingBakFilesUtil

if __name__ == "__main__":
    is_remove_empty_folders = True
    folder_path = "/test_folder"
    folder_util = RemovingBakFilesUtil(
        folder_path,
        is_remove_empty_folders
    )
    folder_util.execute()
