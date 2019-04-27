from flask import Flask, request
from Notifications import Notifications
import Helpers
import requests


app = Flask(__name__)


#MySQL config
mysql_config = Helpers.read_json_from_file("config/mysql_config.json")

#Auth service
auth_service = Helpers.service("auth")

notifs = Notifications(mysql_config["host"], mysql_config["username"], mysql_config["password"], mysql_config["database"])



@app.route("/register", methods=["POST"])
def register():

    #Retrieve the token
    token = request.headers["Authorization"].replace("Bearer ", "")

    token_verification = Helpers.verify_token(token)

    if 'error' in token_verification:
        return token_verification

    uid = token_verification["uid"]
    
    return notifs.register_device( request.form["platform"], request.form["device_id"], uid )




@app.route("/send", methods=["POST"])
def send():

    device_filter = request.form.get("device_filter") or "."
    platform = request.form.get("platform") or 0
    random_drop = request.form.get("random_drop") or 0

    notifs.send_notification( request.form["title"], request.form["message"], device_filter=device_filter, platform=platform, random_drop=random_drop, admin_password=request.form["admin_password"] )

    return "request pending"