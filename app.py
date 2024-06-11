from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def get_traffic_flow_data(apiKey=None, bbox='13.4000,52.5200,13.4050,52.5250', locationReferencing='shape', responseattributes='sh,fc'):
    if apiKey is None or apiKey == '':
        apiKey = 'gvRSPonF26byQAweIqUpSo7gwafiJg0AwIWF3IZAT60'
    
    url = 'https://data.traffic.hereapi.com/v7/flow'
    params = {
        'apiKey': apiKey,
        'bbox': bbox,
        'locationReferencing': locationReferencing,
        'responseattributes': responseattributes
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        return {'error': f'HTTP error occurred: {http_err}'}
    except Exception as err:
        return {'error': f'Other error occurred: {err}'}

@app.route('/flow', methods=['GET'])
def traffic_flow():
    apiKey = request.args.get('apiKey')
    bbox = request.args.get('bbox', '13.4000,52.5200,13.4050,52.5250')
    locationReferencing = request.args.get('locationReferencing', 'shape')
    responseattributes = request.args.get('responseattributes', 'sh,fc')
    data = get_traffic_flow_data(apiKey, bbox, locationReferencing, responseattributes)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
