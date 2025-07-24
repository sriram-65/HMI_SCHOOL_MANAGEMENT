from flask import Flask , Blueprint , render_template , request ,session , redirect ,  jsonify
from database.database import MANAGEMENT_TEACHERS , delete_all_records
from cloud.cloudi import GetCloud
from cloud.cloudi import send_to_cloud
from validators.vali import validate_all
from bson.objectid import ObjectId
import datetime

route_home = Blueprint("route_home" , __name__)


ADMIN_PASSWORD = "HMISCHOOL@2025"

GetCloud()

@route_home.route("/" , methods=["POST" , "GET"])
def set_password():
    if (request.method=="POST"):
        password = request.form.get("password")
        
        if password == ADMIN_PASSWORD:
            session['admin_enterd_pw'] = "YES"
            return redirect("/hmi-admin-school")
        else:
            return render_template("admin_main.html" , e="Invalid Password !")
        
    
    if session.get("admin_enterd_pw"):
        return redirect("/hmi-admin-school")
    else:
        return render_template("admin_main.html")
    
    
@route_home.route("/hmi-admin-school")
def home():
    if session.get("admin_enterd_pw"):
        
      return render_template("admin.html")
    else:
        return redirect("/")


@route_home.route("/upload-teachers-deatils" , methods=["POST"])
def Upload_teachers_deatils():
    try:
        name = request.form.get("name")
        email = request.form.get("email")
        phoneNo = request.form.get("phoneNo")
        what_Teach = request.form.get("whatTeach")
        photo = request.files.get("tphoto")
        
        v = validate_all(
            name,email,phoneNo,what_Teach
            )
        if v != True:
            print(v)
            return render_template("admin.html" , er=v)
        
        if photo == "":
            return jsonify({"Error":"Pls Upload File"})
        photo_cloud = send_to_cloud(photo)
        
        data = {
            "Teacher_name":name,
            "Teacher_email":email,
            "Teacher_phone_no":phoneNo,
            "Teacher_major_subject":what_Teach,
            "Teacher_photo":photo_cloud,
            "Created_at":datetime.datetime.now().strftime("%I:%M:%S %p")
        }
        
        MANAGEMENT_TEACHERS.insert_one(data)
        return render_template("admin.html" , Sucess="Teachers Data Uploaded..!")
        
    except Exception as e:
        print(e)
        return jsonify({"Error":"Internal Server Error"})
   
  
@route_home.route("/hmi-admin-school/teachers")
def List_Teachers():
    get_all = MANAGEMENT_TEACHERS.find({}).sort("_id" , -1)
    count_teachers = MANAGEMENT_TEACHERS.count_documents({})
    return render_template("teachers.html" , T = get_all , C=count_teachers)
 

@route_home.route("/delete/teacher/<id>" , methods=["POST"])
def Delete_teacher(id):
    try:
            MANAGEMENT_TEACHERS.find_one_and_delete({"_id":ObjectId(id)})
            return redirect("/hmi-admin-school/teachers")
          
    except:
        return jsonify({"Error":"Error on deleting the User Maybe Server Error Pls Try Again Later"})


@route_home.route("/edit/teacher/<id>" , methods=['POST' , "GET"])
def Edit_Teacher(id):
    try:
        if request.method=="POST":
            newtname = request.form.get("newtname")
            newtemail = request.form.get("newtemail")
            newphone = request.form.get("newphone")
            newwhat = request.form.get("newwhat")
            newphoto = request.files.get("newphoto")
            
            v = validate_all(newtname , newtemail , newphone , newwhat)
            T = MANAGEMENT_TEACHERS.find_one({"_id":ObjectId(id)})
            
            if v != True:
                return render_template("Edit.html" , er=v)
            
            def get_url():
                if not newphoto or newphoto.filename == "":
                    exting_img = T['Teacher_photo']
                    return exting_img
                else:
                    url = send_to_cloud(newphoto)
                    return url
            
            g = get_url()
            
            MANAGEMENT_TEACHERS.find_one_and_update({"_id":ObjectId(id)} , {"$set":{
            "Teacher_name":newtname,
            "Teacher_email":newtemail,
            "Teacher_phone_no":newphone,
            "Teacher_major_subject":newwhat,
            "Teacher_photo":g,
            "Updated_at":datetime.datetime.now().strftime("%I:%M:%S %p")
            }})
            
            return redirect("/")
        
        else:
            T = MANAGEMENT_TEACHERS.find_one({"_id":ObjectId(id)})
            
            if T:
                return render_template("Edit.html" , T=T) 
    except Exception as e:
        return jsonify({"Error":f"Error on Editing the User Maybe Server Error Pls Try Again Later , {e}"})   
    
@route_home.route("/del")
def deleete():
    d = delete_all_records()
    return jsonify({"msg":d})
    