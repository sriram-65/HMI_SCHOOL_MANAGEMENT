let form = document.querySelector(".teacher-upload")

form.addEventListener("submit" , ()=>{
    form.action = "/upload-teachers-deatils"
    document.getElementById("sub").style.opacity = '0.4px'
    document.getElementById("sub").style.cursor = "not-allowed"
    document.getElementById("sub").innerHTML = "Uploading..."
})





