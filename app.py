from flask import Flask, render_template, request
from pymongo import MongoClient
import datetime

app = Flask(__name__)
client = MongoClient("mongodb+srv://buo:123@firstapp.vm7wb.mongodb.net/test")
db = client.projekt1
entries = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
        entry_content = request.form.get("content")
        entries.append((entry_content, formatted_date))
        db.entries.insert_one({"content": entry_content, "date": formatted_date})
        
    return render_template("page.html", entries=entries)

if __name__ == "__main__": 
    app.run()