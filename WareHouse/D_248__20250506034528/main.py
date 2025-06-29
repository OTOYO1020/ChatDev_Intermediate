'''
Main application for counting occurrences in a sequence.
'''
from flask import Flask, request, jsonify
from utils import count_occurrences
app = Flask(__name__)
@app.route('/count_occurrences', methods=['POST'])
def count_occurrences_route():
    data = request.json
    N = data['N']
    A = data['A']
    Q = data['Q']
    # Validate N and Q types
    if not isinstance(N, int) or not isinstance(Q, int):
        return jsonify({"error": "N and Q must be integers."}), 400
    # Check for empty array or no queries
    if not A or Q == 0:
        return jsonify({"error": "Input array A cannot be empty and there must be at least one query."}), 400
    # Check for the presence and type of queries
    if 'queries' not in data or not isinstance(data['queries'], list):
        return jsonify({"error": "Queries must be provided as a list."}), 400
    results = []
    for query in data['queries']:
        # Validate the presence of required fields
        if 'L' not in query or 'R' not in query or 'X' not in query:
            return jsonify({"error": "Each query must contain L, R, and X."}), 400
        # Validate the type of L, R, and X
        if not isinstance(query['L'], int) or not isinstance(query['R'], int) or not isinstance(query['X'], int):
            return jsonify({"error": "L, R, and X must be integers."}), 400
        L = query['L']
        R = query['R']
        X = query['X']
        # Validate the indices
        if L < 1 or R > len(A) or L > R:
            return jsonify({"error": "L and R must be within valid range and L must be less than or equal to R."}), 400
        # Count occurrences of X in the subarray A[L-1:R]
        count = count_occurrences(A, L, R, X)
        results.append({"count": count})
    return jsonify(results)
if __name__ == "__main__":
    app.run(debug=True)