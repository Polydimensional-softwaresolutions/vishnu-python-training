# Version Control System (Inheritance, Encapsulation, List) 
# Challenge: Model file versions where the history is secured and shared across different file types.
# Requirements:
# Inheritance: Create a base class VersionedFile with a constructor that initializes a private list self.__history to track version numbers.
# Define a method add_version(version_id) in the base class to append to the history.
# Create a subclass CodeFile.
# Define a public method get_history() in the base class to provide read-only access to the version list (Encapsulation).
# Create a CodeFile object, add a few versions, and print the history via the public method.

class VersionedFile:
    def __init__(self):
        self.__history=[]
    def add_version(self,version_id):
        self.__history.append(version_id)
    def getter(self):
        return self.__history

class CodeFile(VersionedFile):
    def get_history(self):
        pass
obj= CodeFile()
obj.add_version("version 1")
obj.add_version("version 2")
obj.add_version(version_id="version 3")
print(obj.getter())