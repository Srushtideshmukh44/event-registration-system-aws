# Event Registration System on AWS



This project is a simple **Event Registration System** built using **AWS services** and a **Flask web application**.  

Users can register for an event using a web form, their data is stored in an AWS RDS MySQL database, and an email notification is sent using AWS SNS.



---



## 🚀 Features

\- Event registration form (Name, Email, Phone, Address)

\- Backend developed using Python Flask

\- Data stored in MySQL (AWS RDS)

\- Email notification using AWS SNS

\- Secure access using IAM Role (no hardcoded credentials)

\- Deployed on AWS EC2



---



## 🏗️ Architecture

User Browser

|

v

EC2 (Flask App)

|

v

RDS (MySQL Database)

|

v

SNS (Email Notification)



---



## 🛠️ Technologies Used

\- \*\*AWS EC2\*\* – Application hosting

\- \*\*AWS RDS (MySQL)\*\* – Database

\- \*\*AWS SNS\*\* – Email notifications

\- \*\*AWS IAM\*\* – Role-based access

\- \*\*Python Flask\*\* – Backend

\- \*\*HTML\*\* – Frontend

\- \*\*Git \& GitHub\*\* – Version control

---

## ⚙️ Setup \& Run (High Level)

1\. Launch EC2 instance

2\. Install Python, Flask, MySQL connector, boto3

3\. Create RDS MySQL database

4\. Configure Security Groups

5\. Create SNS topic and email subscription

6\. Attach IAM role to EC2

7\. Run Flask app on EC2



---



## 📧 Output

\- User submits registration form

\- Data saved in RDS database

\- Confirmation email sent via SNS



## 👩‍💻 Author

**Srushti Deshmukh**  

GitHub: https://github.com/Srushtideshmukh44



