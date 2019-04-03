import re
import pickle
import subprocess
from os import walk
from pathlib import Path
from SearchGUI import SearchGUI


class SearchForFile:

    def __init__(self):
        self.files_matching_search = {}
        self.file_database = Path("file_database")
        if self.file_database.is_file() is False:
            self.create_file_database()
        self.deserialized_files = {}
        with open(str(self.file_database), "rb") as database:
            self.deserialized_files = pickle.load(database)
        database.close()

    # Create a pickle of a dictionary for all files and their paths.
    def create_file_database(self):
        file_paths = {}
        for root, directories, files in walk("C:\\", topdown=True):
            for name in files:
                file_paths[name.lower()] = root
        file_database = open(self.file_database, "wb")
        pickle.dump(file_paths, file_database)
        file_database.close()

    # Command line version asks for user input
    def read_user_file_name(self):
        file_name = input("Search for file: ").lower()
        self.search(file_name)

    def search(self, file_name):
        found_files = {}
        for key in self.deserialized_files:
            if re.search(file_name, key):
                found_files[key] = self.deserialized_files[key]
        self.files_matching_search = found_files

    def print_matching_files(self):
        if len(self.files_matching_search) == 0:
            print("No matching files")
        for key in self.files_matching_search:
            print(key)

    def open_file(self):
        file_to_open = input("which file do you want to open: ").lower()
        for key in self.files_matching_search:
            if re.search(file_to_open, key):
                subprocess.call(self.files_matching_search[key] + "\\" + key, shell=True)


if __name__ == "__main__":
    search = SearchForFile()
    # search.read_user_file_name()
    # search.print_matching_files()
    gui = SearchGUI(search)
    # search.open_file()
