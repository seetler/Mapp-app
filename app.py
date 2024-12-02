from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)





#Global Variables
# Sample data to display on the map
locations = [
    {"name": "San Francisco", "lat": 37.7749, "lng": -122.4194},
    {"name": "Los Angeles", "lat": 34.0522, "lng": -118.2437},
    {"name": "Seattle", "lat": 39.6062, "lng": -122.3321},
]


#Base home page.
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def data():
    # Send JSON data to the frontend
    return jsonify(locations)


#When the route is /submit, it posts the information. It takes, input_user and category
@app.route('/submit', methods=['POST', 'GET'])
def submit():


    # Handle GET requests by redirecting to home
    if request.method == 'GET':
        return redirect(url_for('home'))




    #puts in prompts
    subm_prompt = request.form.get('form_prompt')
    if subm_prompt is None or subm_prompt.strip() == "":
        subm_prompt = "What is the fine for littering?"
    

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')



    # Logger 1
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')    
    output_0=f'{timestamp} - '
    with open('log.txt', 'a') as f:
        f.write(output_0)
    # Logger 1     


  



    return render_template('conversation.html')





#When the route is /conversation, on the followup
@app.route('/conversation', methods=['POST', 'GET'])
def conversation():

    # Handle GET requests by redirecting to home
    if request.method == 'GET':
        return redirect(url_for('home'))

    subm_prompt = request.form.get('form_prompt')
    if subm_prompt is None or subm_prompt.strip() == "":
        subm_prompt = "followup"

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')



    # Logger 1
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')    
    output_0=f'{timestamp} - '
    with open('log.txt', 'a') as f:
        f.write(output_0)
    # Logger 1   

    return render_template('conversation.html')



if __name__ == '__main__':
    # Run the Flask app on all available IP addresses
    app.run(host='0.0.0.0', port=5000, debug=True)
