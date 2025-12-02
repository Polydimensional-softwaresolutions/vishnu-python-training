# 1. Secure Configuration Loader (File, Encapsulation, Dict, Error Handling) 
# Challenge: Create a class to securely load and manage settings from a file.
# Requirements:
# Create a class ConfigManager.
# Encapsulate a dictionary self.__settings to store configuration.
# Define a constructor that takes a filename. Inside the constructor, call a method _load_config().
# Implement _load_config() to read the file line by line using a loop. Each line is "KEY=VALUE". Store these in self.__settings.
# Use Error Handling (try...except) to catch a FileNotFoundError. If the file is not found, initialize self.__settings as an empty dictionary.
# Define a public method get_setting(key) that safely returns the value or "NOT FOUND" using dictionary methods to avoid a KeyError.

class ConfigueManager:
    def __init__(self,filename):
          self.filename=filename
          self.__settings={}
          self._load_config()
    def _load_config(self):
         try:
              with open (r"C:\Users\lenovo\Desktop\python training\text files\llll.txt","r") as file:
                   for i in file:
                        i=i.strip()
                        if "=" in i:
                             key,value = i.split("=",1)
                             self.__settings[key.strip()]=value.strip() 
         except:
              self.__settings={}
    def get_settings(self,key):
         return self.__settings.get(key,"not found")
obj=ConfigueManager("my file")
print(obj.get_settings("helper"))
print(obj.get_settings("Python"))

                   
    
          