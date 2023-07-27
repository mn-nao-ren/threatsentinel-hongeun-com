from flask import Flask, request, jsonify
from threading import Thread  # Import Thread from the 'threading' module
import numpy as np

app = Flask(__name__)

def check_security_status(has_vulnerabilities, has_intrusions):
    # Your Python logic from 'OutputRiskThenResponsePlan.py'
    # goes here. Implement the function to return the appropriate text
    if has_vulnerabilities and has_intrusions:
        return "High risk: Execute credential attack response plan."
    elif not has_vulnerabilities and has_intrusions:
        return "Potential risk: Conduct in-depth investigations and consider executing credential attack response plan."
    elif has_vulnerabilities and not has_intrusions:
        return "Potential risk: Patch vulnerabilities and monitor network."
    else:
        return "Low risk: Continue regular monitoring and security practices."

@app.route('/predict', methods=['POST'])
def predict():
    
    network_traffic_data = np.array([
        [0.003, 0.967, 0.012, 0.011],
        [0.989, 0.0, 0.008, 0.005],
        [0.505, 0.013, 0.021, 0.491],
    ])

    source_code_data = np.array([
        [1, 0],
        [1, 0]
    ])
   

    # Process 'network_traffic_data' to determine 'has_intrusion'
    has_intrusion = int(np.any(np.argmax(network_traffic_data[:, :3], axis=1) < 3))

    # Process 'source_code_data' to determine 'has_vuln'
    has_vuln = int(np.all(source_code_data[:, 1] != 0))

    # Call the 'check_security_status' function with the processed values
    result = check_security_status(has_vuln, has_intrusion)


    # Return the result back to the frontend
    return jsonify({'result': result})


if __name__ == "__main__":
    app.run(debug=True)
