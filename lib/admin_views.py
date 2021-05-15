from lib import app

@app.route("/admin/dashboard")
def admin_dashboard():
    return "Admin dashboard"
