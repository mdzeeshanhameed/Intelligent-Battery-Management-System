from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB configuration
client = MongoClient("mongodb://localhost:27017/")
db = client["battery_management"]  # Replace with your database name
collection = db["battery"]  # Replace with your collection name

@app.route("/")
def index():
    # Fetch SoC, SoH, and status from MongoDB
    data = list(collection.find({}, {"_id": 0, "soc": 1, "soh": 1, "timestamp": 1}))
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
