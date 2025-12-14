🚦 AI TRAFFIC MONITORING SYSTEM
==============================

An AI-powered web application that detects and analyzes vehicles from
traffic videos using YOLOv8, OpenCV, Flask, and Pandas. The system allows
users to upload videos, run vehicle detection, view analytics, and track
traffic insights through an interactive dashboard.

✨ FEATURES (COMPLETED SO FAR)
-----------------------------

🎥 Upload Video
- Process traffic videos and detect vehicles in real-time.

🤖 Vehicle Detection
- YOLOv8 model detects cars, buses, trucks, and motorbikes.

📊 Analytics
- Generates charts:
  * Line chart - Vehicles over time (per frame)
  * Pie chart  - Distribution of vehicle types

🧠 Traffic Status
- Automatically classifies traffic as Light, Moderate, or Heavy.

🖥️ Dashboard UI
- Flask + Bootstrap based clean, dark-themed, and responsive dashboard.

📁 PROJECT STRUCTURE
--------------------
<img width="571" height="327" alt="image" src="https://github.com/user-attachments/assets/977ce42b-c631-4ef5-a612-57238ef53c5b" />




📝 ABOUT PAGE
-------------

- Displays project details, contributors, and libraries
- Content rendered dynamically using backend data

🔮 UPCOMING IMPROVEMENTS (PLANNED)
---------------------------------

📈 Interactive dashboard visualization using Chart.js or Plotly  
🗄️ Store multiple analytics runs using SQLite  
⚡ Improved error handling and validation  
⏳ Background processing with progress indicator  
☁️ Deployment on Heroku, AWS, or Railway using Gunicorn  
🔐 Authentication system for admin dashboard  
📑 Export analytics reports as PDF or CSV  

⚙️ TECH STACK
-------------

Backend:
- Flask (Python)

ML Model:
- YOLOv8 (Ultralytics)

Computer Vision:
- OpenCV

Data Analysis:
- Pandas
- Matplotlib

Frontend:
- HTML
- CSS (Bootstrap)
- Jinja2

Database (Planned):
- SQLite / PostgreSQL

🚀 HOW TO RUN LOCALLY
--------------------

1. Clone the repository:

   git clone https://github.com/yourusername/ai_traffic_system.git
   cd AI_TRAFFIC_SYSTEM

2. Create and activate virtual environment:

   python -m venv venv
   venv\Scripts\activate   (Windows)

3. Install dependencies:

   pip install -r requirements.txt

4. Run the application:

   python app.py

5. Open in browser:

   http://127.0.0.1:5000

👨‍💻 CONTRIBUTOR
----------------

Shweta Kharat  
( Project Lead and Developer )
