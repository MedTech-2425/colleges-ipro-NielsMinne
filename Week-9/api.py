from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {'id': 1, 'name': 'Zohaib Shah', 'class': 'PbaMet-1'},
    {'id': 2, 'name': 'Erica Corthier', 'class': 'PbaMet-2'},
    {'id': 3, 'name': 'Aaron Clemmens', 'class': 'PbaMet-3'}
]

@app.route('/api/students', methods=['GET'])
def get_students():
    return jsonify({'students': students})

@app.route('/api/students/<int:id>', methods=['GET'])
def get_student(id):
    student = next((student for student in students if student['id'] == id), None)
    if student is None:
        return jsonify({'message': 'Student niet gevonden'}), 404
    
    return jsonify(student)



if __name__ == "__main__":
    app.run(debug=True)