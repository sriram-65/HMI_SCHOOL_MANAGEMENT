import re
from email_validator import validate_email , EmailNotValidError

def validate_all(name, email, phoneno, what):
    name_check = validate_name(name)
    if name_check is not True:
        return name_check

    email_check = validate_User_email(email)
    if email_check is not True:
        return email_check

    phone_check = validate_phone_number(phoneno)
    if phone_check is not True:
        return phone_check

    subject_check = validate_what_they_teach(what)
    if subject_check is not True:
        return subject_check

    return True

    
    
def validate_phone_number(phone_no):
    if not phone_no:
        return "Pls Enter Phone Number"
    
    pattern = r'^[6-9]\d{9}$'
    v = re.match(pattern , phone_no)
    if v == None:
        return "Pls Enter Valid Phone Number"
    else:
        return True
    
def validate_User_email(email):
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return "Not Vaild Email Pls Enter Valid Email ID"
    
def validate_name(name):
    if ' ' in name:
        return "Error:  cannot contain spaces!"
    if not name.isalpha():
        return "Error: Only letters allowed!"
    return True


def validate_what_they_teach(teach):
    subjects = ['Tamil' , 'English' ,'Maths', "Science" , "SocialScience"]
    
    if teach in subjects:
        return True
    else:
        return "Only Valid Subjects Only Allowed"

