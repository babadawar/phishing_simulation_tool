# Phishing Simulation and Awareness Tool

## Project Description
This project is designed to simulate phishing attacks and educate users about recognizing phishing emails and scams. By sending simulated phishing emails, hosting a fake login page, and providing actionable feedback, the tool raises awareness and improves users' ability to identify and avoid phishing attempts in real-world scenarios.

---

## Features

1. **Email Automation**:
   - Sends phishing emails to targeted users with a crafted message and a link to a fake login page.
   - Uses the `smtplib` library to manage email automation securely.

2. **Web Development**:
   - Hosts a fake login page using Flask.
   - Captures and stores user credentials entered during the simulation.

3. **Data Logging**:
   - Stores user responses, including usernames, passwords, IP addresses, and timestamps, in an SQLite database.

4. **Educational Feedback**:
   - Redirects users to an educational page after interacting with the phishing simulation.
   - Provides tips and best practices for identifying phishing emails.

5. **Report Generation**:
   - Generates a PDF report summarizing user interactions during the simulation.
   - Includes details such as timestamps, IP addresses, and user credentials (if submitted).

---

## Technologies Used

- **Programming Language**: Python
- **Web Framework**: Flask
- **Email Automation**: `smtplib`, `email.mime`
- **Database**: SQLite
- **PDF Generation**: `reportlab`
- **Frontend**: HTML and CSS (for fake login and educational pages)

---

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/phishing-simulation-tool.git
   cd phishing-simulation-tool
   ```

2. **Install Dependencies**:
   - Ensure Python 3.x is installed.
   - Install the required Python libraries:
     ```bash
     pip install flask reportlab
     ```

3. **Configure Settings**:
   - Edit the `SMTP_SERVER`, `EMAIL_ADDRESS`, `EMAIL_PASSWORD`, `TARGET_EMAILS`, and `PHISHING_LINK` variables in the script.
   - Replace placeholders with your credentials and target email addresses.

4. **Set Up the Database**:
   - Run the script to initialize the SQLite database:
     ```bash
     python phishing_simulation_tool.py
     ```

5. **Run the Web Server**:
   - Start the Flask application:
     ```bash
     python phishing_simulation_tool.py
     ```
   - Access the fake login page at: [http://127.0.0.1:5000/login](http://127.0.0.1:5000/login)

---

## Project Structure

```
.
├── phishing_simulation_tool.py  # Main script
├── phishing_simulation.db       # SQLite database
├── Phishing_Report.pdf          # Generated report
├── templates/                   # HTML templates (if used)
└── static/                      # Static files (CSS, images, etc.)
```

---

## How It Works

1. **Send Emails**:
   - The script sends phishing emails to targets with a fake link.

2. **Fake Login**:
   - Targets clicking the link are redirected to a fake login page.
   - User inputs (username and password) are logged.

3. **Educational Feedback**:
   - After submission, users are shown tips to recognize phishing emails.

4. **Reporting**:
   - Administrators can generate a detailed PDF report summarizing responses.

---

## Security and Ethics
This tool is intended solely for educational purposes and internal training in phishing awareness. Misuse of this tool for malicious purposes is unethical and illegal. Use responsibly and only with explicit permission from participants.

---

## Future Enhancements
- Add multi-language support for educational feedback.
- Implement visualization of phishing simulation data (e.g., charts or graphs).
- Extend compatibility with other database systems like MySQL or PostgreSQL.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact
For questions or contributions, please contact:
- **Dawar Farooq**
- Email: [dawarbaba140@gmail.com](mailto:dawarbaba140@gmail.com)

