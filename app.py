from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

# -------------------------------
# Load environment variables
# -------------------------------
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "fallback_secret_key")

# -------------------------------
# (Optional) Mail Configuration
# If you don’t need email yet, remove MAIL_* envs from .env
# -------------------------------
app.config.update(
    MAIL_SERVER=os.getenv("MAIL_SERVER", "smtp.gmail.com"),
    MAIL_PORT=int(os.getenv("MAIL_PORT", 587)),
    MAIL_USE_TLS=os.getenv("MAIL_USE_TLS", "True").lower() in [
        "true", "1", "yes"],
    MAIL_USE_SSL=False,  # Explicitly set to False for Gmail with TLS
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
)
mail = Mail(app)

# -------------------------------
# Data (tailored to your resume: cybersecurity + Python focus)
# Note: PROJECTS data is now defined inside the projects() function.
# -------------------------------

EXPERIENCES = [
    {
        "company": "Google & Coursera",
        "role": "Professional Certificate",
        "period": "2024",
        "location": "Remote",
        "bullets": [
            "Earned the Google Professional Cybersecurity Certificate, demonstrating proficiency in foundational cybersecurity concepts.",
            "Acquired practical skills in Python, Linux, and SQL for security tasks.",
            "Studied security information and event management (SIEM) tools to detect and analyze threats."
        ],
        "skills": ["Python", "Linux", "SQL", "SIEM", "IDS"]
    },
    {
        "company": "3MTT Nigeria/Darey.io",
        "role": "Cybersecurity Trainee",
        "period": "2025",
        "location": "Hybrid",
        "bullets": [
            "Completed an extensive cybersecurity program covering foundational security principles, network defense, and ethical hacking.",
            "Gained hands-on experience with industry-standard tools for penetration testing and vulnerability analysis.",
            "Collaborated on a team project to design a secure network architecture for a small business."
        ],
        "skills": ["Network Security", "Ethical Hacking", "Vulnerability Analysis", "Digital Forensics"]
    },
    {
        "company": "Cybersecured India",
        "role": "Cybersecurity & Python Developer",
        "period": "2023 — 2024",
        "location": "Remote",
        "bullets": [
            "Developed Python tools for network monitoring and security.",
            "Conducted vulnerability assessments and penetration testing.",
            "Automated security workflows with Bash and SQL."
        ],
        "skills": ["Python", "Vulnerability Analysis", "Penetration Testing", "Bash", "SQL"]
    },
    {
        "company": "ALX Africa",
        "role": "Software Engineering",
        "period": "2022 — 2023",
        "location": "Hybrid",
        "bullets": [
            "Worked on collaborative projects, contributing to open-source initiatives.",
            "Specialized in backend and DevOps tasks, including server configuration, and automation scripts.",
            "Mentored junior cohorts and participated in regular knowledge-sharing sessions to foster a culture of continuous learning."
        ],
        "skills": ["Bash", "C", "Git", "Linux", "Python", "Flask"]
    },
    {
        "company": "Funtay Group",
        "role": "Conversion Engineer",
        "period": "2024 — Present",
        "location": "Onsite",
        "bullets": [
            "Leading technical teams in energy solutions.",
            "Implementing innovative strategies for operational efficiency.",
            "Ensuring compliance and safety in engineering projects."
        ],
        "skills": ["CNG", "AEB2001N IC Software", "Team Leadership"]
    },
    {
        "company": "Panafrican Equipment Nigeria Limited",
        "role": "Engineering Intern",
        "period": "Aug 2022 — Feb 2023",
        "location": "Onsite",
        "bullets": [
            "Conducted rigorous routine checks on diesel engines, monitoring performance parameters, fluid levels, and executing timely filter replacements to ensure operational integrity.",
            "Maintained comprehensive documentation of all engine room maintenance activities, meticulously logging irregularities and repairs for record-keeping and future reference.",
            "Collaborated effectively with senior engineers to diagnose and resolve complex mechanical and operational issues with diesel engines."
        ],
        "skills": ["Diesel Engines", "Maintenance", "Troubleshooting", "Technical Documentation"]
    }
]

EDUCATION = [
    {
        "school": "Nigeria Maritime University",
        "program": "B.Eng. Marine Engineering (First Class Honors)",
        "period": "2019 — 2024",
        "notes": ["Capstone: Ocean Thermal Energy Conversion(OTEC)", "Relevant Courses: Cybersecurity, Python Programming"]
    }
]

SOCIALS = {
    "github": "https://github.com/Osvic1",
    "linkedin": "https://www.linkedin.com/in/timothy-victor-a61421223/",
    "email": "mailto:Timothyv952@gmail.com",
    "resume": "/static/resume/resume.pdf",  # Place your resume.pdf here
}

# -------------------------------
# Routes
# -------------------------------


@app.route("/")
def home():
    return render_template("index.html", title="Home", socials=SOCIALS), 200, {'Content-Type': 'text/html; charset=utf-8'}


@app.route("/about")
def about():
    return render_template("about.html", title="About", socials=SOCIALS), 200, {'Content-Type': 'text/html; charset=utf-8'}


@app.route("/education")
def education():
    return render_template("education.html", title="Education", items=EDUCATION, socials=SOCIALS), 200, {'Content-Type': 'text/html; charset=utf-8'}


@app.route("/experience")
def experience():
    return render_template("experience.html", title="Experience", items=EXPERIENCES, socials=SOCIALS), 200, {'Content-Type': 'text/html; charset=utf-8'}


@app.route("/projects")
def projects():
    # Define PROJECTS inside a function where the app context is available
    PROJECTS = [
        {
            "title": "🔒 Securing the Access Grid - Cybershield Corp",
            "description": "Simulated a phishing attack scenario and developed a mitigation strategy with user-awareness testing and secure email gateway configurations.",
            "images": [
                url_for('static', filename='images/sag1.png'),
                url_for('static', filename='images/sag2.png'),
                url_for('static', filename='images/sag3.png'),
            ],
            "tags": ["Cybersecurity", "Phishing", "Email Security"],
            "link": "https://docs.google.com/document/d/1QROBH9YugqsjiJk6TwuAu_v83KLJFgbdFxfc7rD3zr8/edit?usp=sharing"
        },
        {
            "title": "🛡️ Network Security Design",
            "description": "Designed and implemented a secure enterprise network using firewalls, VPNs, and IDS/IPS for threat prevention and monitoring.",
            "images": [
                url_for('static', filename='images/kaf1.png'),
                url_for('static', filename='images/kaf2.png'),
                url_for('static', filename='images/kaf3.png'),
            ],
            "tags": ["Network Security", "VPN", "IDS/IPS"],
            "link": "https://docs.google.com/document/d/12_VYLXBQT_RYP0M-Rv5GvNPCM_EJGJ-ElaM-EGFePJY/edit?usp=drive_link"
        },
        {
            "title": "🐍 Website Monitoring Tool (Python)",
            "description": "A Python-based monitoring tool that tracks website uptime/downtime and sends alerts when issues occur.",
            "images": [
                url_for('static', filename='images/wsmd1.png'),
                url_for('static', filename='images/wsmd2.png'),
                url_for('static', filename='images/wsmd3.png'),
            ],
            "tags": ["Python", "Automation", "Uptime Monitoring"],
            "link": "https://github.com/Osvic1/website-monitoring-dashboard"
        },
        {
            "title": "🧱 Host-Based Firewall Configuration (Windows)",
            "description": "Configured Windows Defender Firewall to block unauthorized access, allow trusted applications, and monitor activity. Rules were created for inbound/outbound traffic, and logs were analyzed to confirm enforcement.",
            "images": [
                url_for('static', filename='images/fw1.png'),
                url_for('static', filename='images/fw2.png'),
                url_for('static', filename='images/fw3.png'),
            ],
            "tags": ["Firewall", "Windows Security", "Access Control"],
            "link": "https://docs.google.com/document/d/1RqVK-ABCZ5TeWHGBxxU9JNE21n0S9w3w3ou5B3cgWss/edit?usp=sharing"
        },

        {
            "title": "🧪 Vulnerability Scan Using OpenVAS",
            "description": "Performed a full vulnerability assessment on ShieldGuard Inc.'s LAN using OpenVAS. Detected critical issues including unpatched software, weak SSH passwords, and exposed SMB services. Provided remediation steps and long-term security recommendations.",
            "images": [
                url_for('static', filename='images/opv1.png'),
                url_for('static', filename='images/opv2.png'),
                url_for('static', filename='images/opv3.png'),
            ],
            "tags": ["Vulnerability Assessment", "OpenVAS", "Network Security"],
            "link": "https://docs.google.com/document/d/1BTIynjtbc4gbitqLxSkFuyzXv82Q8dSxV537i3mCFbM/edit?usp=sharing"
        },

    ]
    return render_template("projects.html", title="Projects", projects=PROJECTS, socials=SOCIALS), 200, {'Content-Type': 'text/html; charset=utf-8'}


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "Anonymous")
        email = request.form.get("email", "No Email")
        message = request.form.get("message", "")

        # If MAIL_USERNAME or MAIL_PASSWORD isn’t set, just fake success
        if not (app.config.get("MAIL_USERNAME") and app.config.get("MAIL_PASSWORD")):
            flash("✅ Message received locally (email disabled).", "success")
            return redirect(url_for("contact"))

        try:
            msg = Message(
                subject=f"New Contact from {name}",
                sender=app.config["MAIL_USERNAME"],
                recipients=[app.config["MAIL_USERNAME"]],
                body=f"""
New message from your portfolio:

Name: {name}
Email: {email}

Message:
{message}
                """,
            )
            mail.send(msg)
            flash("✅ Your message has been sent successfully!", "success")
        except Exception as e:
            flash(f"❌ Error sending message: {e}", "danger")
        return redirect(url_for("contact"))

    return render_template("contact.html", title="Contact", socials=SOCIALS), 200, {'Content-Type': 'text/html; charset=utf-8'}


# -------------------------------
# Security and Performance Headers
# -------------------------------
@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    if 'static' in response.headers.get('Location', ''):
        response.headers['Cache-Control'] = 'public, max-age=31536000, immutable'
    return response


if __name__ == "__main__":
    app.run(debug=True)
