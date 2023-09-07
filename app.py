# flask import and datetime
from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

# Dummy data for demonstration
oysters = [
    {"id": 0, "farm_name": "Oysther", "location": {"city":"Georgetown", "state":"Maine", "zipcode":"04903", "coordinates": {"lat": "0321", "long": "1230"}, "species": "the best", "description": "A delicious blend of sweetness and salinity", "tasting_notes": ["sweet", "salinity"], "size":"medium"}}
]

@app.route('/')
def index():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'time': timeString,
      }
    return render_template('index.html', **templateData)
    # visit flask docs to render other templates: https://flask.palletsprojects.com/en/2.3.x/tutorial/templates/



# complex logic will come later
# # Create
# @app.route('/oysters', methods=['POST'])
# def add_oyster():
#     new_oyster = request.get_json()
#     oysters.append(new_oyster)
#     return jsonify({"message": "oyster created"}), 201

# # Read (Get all oysters)
# @app.route('/oysters', methods=['GET'])
# def get_oysters():
#     return jsonify(oysters)

# # Read (Get a specific oyster by ID)
# @app.route('/oysters/<int:id>', methods=['GET'])
# def get_oyster(id):
#     oyster = next((oyster for oyster in oysters if oyster["id"] == id), None)
#     if oyster:
#         return jsonify(oyster)
#     return jsonify({"message": "oyster not found"}), 404

# # Update
# @app.route('/oysters/<int:id>', methods=['PUT'])
# def update_oyster(id):
#     oyster = next((oyster for oyster in oysters if oyster["id"] == id), None)
#     if oyster:
#         updated_data = request.get_json()
#         oyster.update(updated_data)
#         return jsonify({"message": "oyster updated"})
#     return jsonify({"message": "oyster not found"}), 404

# # Delete
# @app.route('/oysters/<int:id>', methods=['DELETE'])
# def delete_oyster(id):
#     oyster = next((oyster for oyster in oysters if oyster["id"] == id), None)
#     if oyster:
#         oysters.remove(oyster)
#         return jsonify({"message": "oyster deleted"})
#     return jsonify({"message": "oyster not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.124')