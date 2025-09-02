# 🌐 My Portfolio

This is my personal portfolio website built with **Flask**, featuring sections about me, my skills, education, projects, and contact information.
It is designed to be **responsive, modern, and professional**.

---

## 🚀 Features

- 📄 About, Education, Experience, and Projects sections
- 🎨 Responsive design with custom CSS and animations
- 🖼️ Project image slider with navigation controls
- 📬 Contact form integration (**Flask-Mail** with Gmail or Brevo)
- ⚡ Deployed using **Render** for free hosting

---

## 📂 Project Structure

```
MYPORTFOLIO/
│── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   ├── images/        # Portfolio images
│   └── resume/        # Resume files
│
│── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── education.html
│   ├── experience.html
│   ├── projects.html
│   └── contact.html
│
│── app.py             # Flask application entry point
│── requirements.txt   # Python dependencies
│── runtime.txt        # Python version for deployment
│── Procfile           # Deployment process for Render
│── .env               # Environment variables (not in Git)
│── README.md          # Project documentation
```

---

## 🛠️ Installation & Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/Osvic1/Portfolio.git
   cd Portfolio
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Mac/Linux
   venv\Scripts\activate      # On Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application locally:

   ```bash
   flask run
   ```

   or

   ```bash
   python app.py
   ```

---

## 🚀 Deployment on Render

This portfolio is configured to deploy on **Render**:

- Uses `Procfile` for Gunicorn
- Uses `runtime.txt` for Python version
- Auto-deploys from GitHub when new commits are pushed

Steps:

1. Push your code to GitHub
2. Create a free Render account
3. Create a new **Web Service**, connect your GitHub repo
4. Render will build and deploy automatically 🎉

---

## 📧 Contact Me

I’d love to connect! Feel free to reach out through any of the platforms below:

- 📩 **Email:** [timothyv952@gmail.com](mailto:timothyv952@gmail.com)
- 💼 **LinkedIn:** [Timothy Victor](https://www.linkedin.com/in/timothy-victor-a61421223/)
- 💻 **GitHub:** [Osvic1](https://github.com/Osvic1/Portfolio)
