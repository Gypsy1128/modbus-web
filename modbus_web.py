from flask import Flask, jsonify, request, render_template
from datetime import datetime

app = Flask(__name__)
latest_data = {
    "timestamp": "--",
    "values": {}
}

registers = {
    'Coil': {f'Coil_{i:03d}': None for i in range(1, 17)},
    'Status': {f'Status_{i:03d}': None for i in range(1, 13)},
    'Input': {f'Input_{i:03d}': None for i in range(1, 20, 2)},
    'Hold': {
        'Hold_001': None, 'Hold_003': None, 'Hold_005': None, 'Hold_007': None, 'Hold_009': None,
        'Hold_011': None, 'Hold_013': None, 'Hold_015': None, 'Hold_017': None, 'Hold_019': None,
        'Hold_021': None, 'Hold_023': None, 'Hold_031': None, 'Hold_033': None, 'Hold_035': None,
        'Hold_037': None, 'Hold_039': None, 'Hold_041': None, 'Hold_043': None, 'Hold_045': None,
        'Hold_047': None, 'Hold_049': None, 'Hold_051': None, 'Hold_053': None, 'Hold_055': None,
        'Hold_057': None, 'Hold_059': None, 'Hold_061': None
    }
}

@app.route('/')
def index():
    return render_template('index.html', groups=registers)

@app.route('/data')
def get_data():
    return jsonify(latest_data)

@app.route('/upload', methods=['POST'])
def upload():
    global latest_data
    try:
        content = request.get_json()
        latest_data['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        latest_data['values'] = content['values']
        return 'OK', 200
    except Exception as e:
        return f'Upload error: {str(e)}', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
