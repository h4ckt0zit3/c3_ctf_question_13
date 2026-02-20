from flask import Flask, request, render_template_string
import hashlib

app = Flask(__name__)

# Weak hardcoded admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD_HASH = hashlib.md5("SecureBank@2026".encode()).hexdigest()

login_page = """
<h2>🏦 SecureBank Admin Login</h2>
<form method="POST">
    <input type="text" name="username" placeholder="Username"><br><br>
    <input type="password" name="password" placeholder="Password"><br><br>
    <button type="submit">Login</button>
</form>
<p style="color:red;">{{message}}</p>
"""

@app.route("/")
def home():
    return """
    <h2>🏦 SecureBank Portal</h2>
    <p>Only administrators can access the admin vault.</p>
    <a href="/admin">Go to Admin Login</a>
    """

@app.route("/admin", methods=["GET", "POST"])
def admin():
    message = ""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        password_hash = hashlib.md5(password.encode()).hexdigest()

        if username == ADMIN_USERNAME and password_hash == ADMIN_PASSWORD_HASH:
            return "<h1>🎉 flag{weak_passwords_are_dangerous}</h1>"
        else:
            message = "Invalid credentials."

    return render_template_string(login_page, message=message)


if __name__ == "__main__":
    app.run(debug=False)