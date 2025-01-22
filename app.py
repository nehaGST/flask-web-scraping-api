from flask import Flask, jsonify
from scrape_data import scrape_data

app = Flask(__name__)

# API endpoint to scrape data
@app.route('/scrape', methods=['GET'])
def get_scraped_data():
    data = scrape_data()  # Call the scraping function
    return jsonify(data)  # Return data as JSON

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5001)

