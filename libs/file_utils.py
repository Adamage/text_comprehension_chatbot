import urllib.request
import os


class file_utils:
    @staticmethod
    def download_file(url, output_file_name):
        print("Downloading from url: {0}, to: {1}".format(url, output_file_name))

        try:
            urllib.request.urlretrieve(url, filename=output_file_name)
        except Exception as e:
            print("Failed to download file. Details: " + str(e))
            raise

    @staticmethod
    def ensure_folder_exists(dir_path):
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)
