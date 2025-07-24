import cloudinary
import cloudinary.uploader

def GetCloud():
    cloudinary.config(
    cloud_name = "dgi871vwh", 
    api_key = "832462747986433",
    api_secret = "c3fUXW4xkKs7rcDVhoufhd0agqw"
)

def send_to_cloud(photo):
    send = cloudinary.uploader.upload(photo)
    get_url = send['secure_url']
    return get_url
