from flask import Flask
from routes.route import route_home
from datetime import timedelta
app = Flask(__name__ , template_folder="templ")

app.register_blueprint(route_home)

app.secret_key = "HMISCHOOL@2025_THIRULINGESHWAR_SRIRAM_DEVELOPERS"
app.permanent_session_lifetime = timedelta(days=1)

if __name__ == "__main__":
    app.run(debug=True)
