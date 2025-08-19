from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from pymongo import MongoClient
from bson import ObjectId
import os
mongo_uri  = os.environ.get("MONGO_URI")
db_name    = os.environ.get("DB_NAME")
client = MongoClient(mongo_uri)
mydb = client[db_name]
mycol = mydb["router_info"]

sample = Flask(__name__)
data = []

@sample.route("/")
def main():
	return render_template("index.html", data=mycol.find())

@sample.route("/add", methods=["POST"])
def add_router():
    ip = request.form.get("ip_address")
    user = request.form.get("username")
    passw = request.form.get("password")

    if ip and user and passw:
        mydict = {"router_ip": ip , "router_user": user, "router_pass": passw}
        mycol.insert_one(mydict)
        data.append({"router_ip": ip , "router_user": user, "router_pass": passw})
    return redirect("/")

@sample.route("/delete/<idx>", methods=["POST"])
def delete_comment(idx):
    myquery = {'_id': ObjectId(idx)}
    mycol.delete_one(myquery)
    return redirect("/")

if __name__ == "__main__":
	sample.run(host="0.0.0.0", port=8080)
