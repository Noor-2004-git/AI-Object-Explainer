from gemini_helper import explain_object
from detector import detect_objects
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/detect", methods=["POST"])
def detect():

    data = request.json

    detected = detect_objects(data["image"])

    if not detected:
        return jsonify({
            "message": "No object detected."
        })

    # Take the first detected object
    object_name = detected[0]

    explanation = explain_object(object_name)

    return jsonify({
        "message": explanation
    })
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)