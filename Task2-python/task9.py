#Write a function student_info(**kwargs) that prints all the details passed to it (like roll=1, grade='A').

def student_info(**kwargs):
    print("student details:")
    for key,value in kwargs.items():
        print(f"{key}={value}")
student_info(stdent_name="vishu",student_roll_no=1,grade_points="A")