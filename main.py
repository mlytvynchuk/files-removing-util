from utils import RemovingBakFilesUtil

if __name__ == "__main__":
    is_remove_empty_folders = True
    folder_util = RemovingBakFilesUtil(
        "/Users/max22111/mydev/bakfoldrs/test_folder",
        is_remove_empty_folders
    )
    folder_util.execute()
