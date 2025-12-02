#  Data Integrity Checker (List, Tuple, Error Handling, Loop) 
# Challenge: Validate the integrity of complex data structures before processing.
# Requirements:
# Create a class Validator.
# Implement a method check_records(record_list) where record_list is a list of tuples, e.g., [(ID, name, status), ...].
# Use a loop to iterate through the list.
# Inside the loop, use Error Handling (try...except) to check two conditions:
# The tuple must have exactly three elements. (Use a TypeError or IndexError check).
# The ID (first element) must be an integer (Use a TypeError check).
# If a record fails the check, print an error message; otherwise, print "Valid record."

class Validator:
    def check_records(self,record_list):
        self.record_list=list() 
        for i in record_list:
            try:
                if len(i)!=3:
                    raise IndexError
                record_id=i[0]
                if isinstance(record_id,int):
                    raise TypeError
            except:
                print("error in record")
            else:
                print("valid print")

valid=Validator()
records=[(100,"vishu","active"),("100","abcde","notactive")]
valid.check_records(records)

