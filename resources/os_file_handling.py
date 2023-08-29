import os


class FileHandling:

    def __init__(self, root_path):
        self.root = root_path

    def create_folder(self):
        try:
            os.mkdir(self.root)
        except FileExistsError:
            print('Folder already present')