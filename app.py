from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename
import os
import pandas as pd

# import the counting function you already wrote
from vehicle_count import count_vehicles

app = Flask(__name__)
app.secret_key = "dev-key"  # change for production

# folders
UPLOAD_FOLDER = "uploads"
DATA_FOLDER = "data"
STATIC_FOLDER = "static"

# allowed video types
ALLOWED_EXTENSIONS = {"mp4", "avi", "mov", "mkv"}

# ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DATA_FOLDER, exist_ok=True)
os.makedirs(STATIC_FOLDER, exist_ok=True)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def get_totals_dict():
    path = os.path.join(DATA_FOLDER, "vehicle_totals.csv")
    if os.path.exists(path) and os.path.getsize(path) > 0:
        try:
            rec = pd.read_csv(path).to_dict(orient="records")
            return rec[0] if rec else {}
        except Exception:
            return {}
    return {}

@app.route("/")
def dashboard():
    totals = get_totals_dict() or {}

    # ensure totals values are ints if possible
    cleaned = {}
    for k, v in totals.items():
        try:
            cleaned[k] = int(v)
        except Exception:
            try:
                cleaned[k] = int(float(v))
            except Exception:
                cleaned[k] = 0
    totals = cleaned

    total_count = sum(totals.values()) if totals else 0

    # default label + class
    status_label = "No Data"
    status_class = "status-none"

    if total_count > 0:
        if total_count >= 200:
            status_label, status_class = "Heavy", "status-heavy"
        elif total_count >= 80:
            status_label, status_class = "Moderate", "status-moderate"
        else:
            status_label, status_class = "Light", "status-light"

    # debug print (remove later if you want)
    print("DEBUG dashboard -> totals:", totals, "total_count:", total_count,
          "status_label:", status_label, "status_class:", status_class)

    charts = []
    for fn in ["vehicles_over_time.png", "vehicle_types.png", "vehicles_from_results.png"]:
        if os.path.exists(os.path.join(STATIC_FOLDER, fn)):
            charts.append(fn)

    return render_template(
        "dashboard.html",
        totals=totals,
        total_count=total_count,
        status_label=status_label,
        status_class=status_class,
        charts=charts,
    )



@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        if "video" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["video"]
        if file.filename == "":
            flash("No file selected")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(save_path)

            # Run analysis (synchronous, since you’re on local dev)
            flash("Processing video… this may take a bit depending on length.")
            count_vehicles(save_path)

            flash("Analysis complete. See Analytics page for outputs.")
            return redirect(url_for("analytics"))

        flash("Unsupported file type. Allowed: mp4, avi, mov, mkv")
        return redirect(request.url)

    return render_template("upload.html")

@app.route("/analytics")
def analytics():
    charts = []
    for fn in ["vehicles_over_time.png", "vehicle_types.png", "vehicles_from_results.png"]:
        if os.path.exists(os.path.join(STATIC_FOLDER, fn)):
            charts.append(fn)

    results_exists = os.path.exists(os.path.join(DATA_FOLDER, "results.csv")) and os.path.getsize(os.path.join(DATA_FOLDER, "results.csv")) > 0
    totals_exists = os.path.exists(os.path.join(DATA_FOLDER, "vehicle_totals.csv")) and os.path.getsize(os.path.join(DATA_FOLDER, "vehicle_totals.csv")) > 0

    return render_template(
        "analyze.html",
        charts=charts,
        results_exists=results_exists,
        totals_exists=totals_exists
    )

@app.route("/download/<path:filename>")
def download(filename):
    # download CSVs from /data
    return send_from_directory(DATA_FOLDER, filename, as_attachment=True)

@app.route("/about")
def about():
    project_info = {
        "name": "AI Traffic System",
        "version": "1.0.0",
        "contributors": ["Shweta Kharat",],
        "libraries": ["Flask", "OpenCV", "YOLOv8 (Ultralytics)", "Pandas", "Matplotlib"],
        "description": "An AI-powered traffic monitoring system that detects, counts, and analyzes vehicles in real-time from video feeds."
    }
    return render_template("about.html", project=project_info)


if __name__ == "__main__":
    app.run(debug=True)
