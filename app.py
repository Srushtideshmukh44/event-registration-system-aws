from flask import Flask, render_template, request
import mysql.connector
import boto3

app = Flask(__name__)

# RDS connection
db = mysql.connector.connect(
    host="event-db.c8vs6qe0gj08.us-east-1.rds.amazonaws.com",
    user="admin",
    password="Srushti44",
    database="eventdb"
)
cursor = db.cursor()

# SNS client (region MUST match SNS topic)
sns = boto3.client("sns", region_name="us-east-1")

TOPIC_ARN = "arn:aws:sns:us-east-1:570959644631:event-registration-topic"
@app.route("/")
def home():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    address = request.form["address"]

    # Insert into DB
    sql = "INSERT INTO users (name, email, phone, address) VALUES (%s, %s, %s, %s)"
    values = (name, email, phone, address)
    cursor.execute(sql, values)
    db.commit()

    # SNS publish
    message = f"""
New Event Registration 🎉

Name: {name}
Email: {email}
Phone: {phone}
Address: {address}
"""
    sns.publish(
        TopicArn=TOPIC_ARN,
        Message=message,
        Subject="Event Registration Confirmation"
    )

    return "✅ Registration successful! Email notification sent."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
