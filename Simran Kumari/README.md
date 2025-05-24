# Simran Kumari – EmptyCup Full Stack Assignment

This project is a mobile-first interior designer listings page, built as part of the EmptyCup Full Stack Assignment. It includes a frontend (HTML/CSS/JS) and backend (Flask API with SQLite), fully containerized using Docker and deployed publicly.

---

## 🔗 Live Demo Links

- 🔸 **Frontend (Netlify)**: [https://6831ee4cf4b0a3d1219a5626--wonderful-moxie-91af4a.netlify.app/]

- 🔹 **Backend API (Render)**: (I Could not able to do with render so no link)

---

## 🖥️ Features

- Mobile-friendly design matching EmptyCup’s Figma spec
- Dynamic listing data loaded from backend API
- Shortlisting toggle with icon switch
- “Shortlisted” filter toggle to show only shortlisted designers
- Fully responsive layout
- API-powered backend using Flask
- Local development with Docker and Docker Compose
- Publicly deployed frontend and backend

---

## 📁 Folder Structure
Simran Kumari/
├── backend/
│ ├── app.py
│ ├── database.py
│ ├── listings.db
│ ├── Dockerfile
│ └── requirements.txt
├── frontend/
│ ├── index.html
│ ├── styles.css
│ ├── script.js
│ ├── Dockerfile
│ └── images/
├── docker-compose.yml
└── README.md


---

## 🚀 Getting Started Locally (Docker)

### 1. Clone the repository
```bash
git clone https://github.com/simran0323/emptycup-assignment.git
cd Simran\ Kumari/

### 2. Build and run using Docker Compose
docker-compose build
docker-compose up

3. Access the app
Frontend: http://localhost:3000
Backend API: http://localhost:5000/api/listings

🧪 API Details
GET /api/listings
Returns all designer listings:

.json file
[
  {
    "id": 1,
    "name": "Epic Designs",
    "description": "...",
    "projects": 57,
    "years": 8,
    "price": "$$",
    "contact": ["+91-123456789", "+91-987654321"]
  },
  ...
]

⚙️ Technologies Used
HTML5, CSS3, JavaScript
Python 3 + Flask
SQLite
Docker & Docker Compose
Render (for backend deployment)
Netlify (for frontend deployment)

📹 Loom Demo Video (my Project was working till before deployment so didn't make Loom video.)