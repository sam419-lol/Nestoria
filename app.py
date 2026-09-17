from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# Required for local development, Vercel ignores this block
if __name__ == "__main__":
    app.run(debug=True)