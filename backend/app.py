from flask import Flask, jsonify, request
from flask_cors import CORS

import db

app = Flask(__name__)
CORS(app)

# Instructions:
# - Use the functions in backend/db.py in your implementation.
# - You are free to use additional data structures in your solution
# - You must define and tell your tutor one edge case you have devised and how you have addressed this

@app.route("/students")
def get_students():
    students = db.get_all_students()
    return jsonify(students), 200


@app.route("/students", methods=["POST"])
def create_student():
    data = request.get_json(force=True)

    try:
        db.insert_student(
            data["name"],
            data["course"],
            data["mark"]
        )
        return jsonify({}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    student = db.update_student(
        student_id,
        name=data.get("name"),
        course=data.get("course"),
        mark=data.get("mark"),
    )
    if student is None:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(student), 200



@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    student = db.delete_student(student_id)
    if student is None:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(student), 200


@app.route("/stats")
def get_stats():
    students = db.get_all_students()
    if not students:
        return jsonify({"count": 0, "average": None, "min": None, "max": None}), 200

    marks = [s["mark"] for s in students]
    stats = {
        "count": len(students),
        "average": sum(marks) / len(marks),
        "min": min(marks),
        "max": max(marks),
    }
    return jsonify(stats), 200


@app.route("/")
def health():
    """Health check."""
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
