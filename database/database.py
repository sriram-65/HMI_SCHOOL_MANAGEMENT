from pymongo import MongoClient

client = MongoClient("mongodb+srv://sriram65raja:HMISCHOOL@cluster0.tzseakx.mongodb.net/")
db = client['HMI_SCHOOL']
MANAGEMENT_TEACHERS = db["MANAGEMENT_TEACHERS"]


def delete_all_records():
    MANAGEMENT_TEACHERS.delete_many({})
    return "Records Deleted Suessfully"