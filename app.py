from flask import Flask, render_template, jsonify
import os
import json
from pathlib import Path

app = Flask(__name__)

CONFIG_FILE = 'config/settings.json'
NOTEBOOKS_DIR = 'notebooks'

def load_config():
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)

@app.route('/')
def index():
    config = load_config()
    return render_template('index.html', app_name=config['app_name'])

@app.route('/api/notebooks')
def list_notebooks():
    notebooks = []
    if os.path.exists(NOTEBOOKS_DIR):
        for file in os.listdir(NOTEBOOKS_DIR):
            if file.endswith('.ipynb'):
                notebooks.append({
                    'name': file,
                    'path': f'/notebooks/{file}'
                })
    return jsonify({'notebooks': sorted(notebooks)})

@app.route('/api/notebook/<path:filename>')
def get_notebook(filename):
    notebook_path = os.path.join(NOTEBOOKS_DIR, filename)
    if os.path.exists(notebook_path) and notebook_path.endswith('.ipynb'):
        with open(notebook_path, 'r') as f:
            return jsonify(json.load(f))
    return jsonify({'error': 'Notebook not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
