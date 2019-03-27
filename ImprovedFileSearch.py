import pickle
from pathlib import Path
from os import walk


class SearchForFile:

    def __init__(self):
        self.file_database = Path("file_database")
        if self.file_database.is_file() is False:
            self.create_file_database()

    def create_file_database(self):
        file_paths = {}
        for root, directories, files in walk("C:\\", topdown=True):
            for name in files:
                file_paths[name] = root
        file_database = open("file_database", "wb")
        pickle.dump(file_paths, file_database)
        file_database.close()

    def read_user_file_name(self):
        file_name = input("Search for file: ")
        self.search(file_name)

    def search(self, file_name):
        deserialized_files = None
        found_files = []
        with open(str(self.file_database), "rb") as database:
            deserialized_files = pickle.load(database)
        for key in deserialized_files:
            if file_name in key:
                found_files.append(key)
        self.print_path_name(found_files)

    def print_path_name(self, path_names):
        if len(path_names) == 0:
            print("No matching files")
        for path in path_names:
            print(path)


if __name__ == "__main__":
    search = SearchForFile()
    search.read_user_file_name()
