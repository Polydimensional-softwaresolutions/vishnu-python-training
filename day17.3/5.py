# Dynamic Data Processor (List, Dict, Tuple, Loop) 
# Challenge: Create a flexible class to process different data formats into a standardized dictionary.
# Requirements:
# Create a class Processor.
# Implement a method normalize_data(raw_data) that accepts raw_data, which can be one of three types:
# A list of tuples [(key, value), (key, value)].
# A dictionary {key: value, key: value}.
# A tuple containing two parallel lists ([keys], [values]).
# Use conditional logic (if/elif) to detect the input type.
# Use a loop to convert the data into a standard dictionary and return it.

class Processor:
    def normalized_data(self,raw_data):
        self.raw_data=raw_data
        dictionary={}
        if isinstance(raw_data,list):
            for key,value in raw_data:
                dictionary[key]=value
        
        elif isinstance(raw_data,tuple):
            keys, values = raw_data
            for i in range(len(keys)):
                dictionary[keys[i]] = values[i]

        elif isinstance(raw_data,dict):
            for key,value in raw_data.items():
                dictionary[key]=value
        else:
            print("data not supported")
        return dictionary

obj=Processor()
print(obj.normalized_data([("name","vishu"),("age",25)]))
print(obj.normalized_data({"vishu": 25}))
print(obj.normalized_data((["vishu"],[25])))



