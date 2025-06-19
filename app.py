# from flask import Flask, render_template, request
# import os
# import base64
# from datetime import datetime

# app = Flask(__name__)
# SAVE_DIR = 'photos'

# if not os.path.exists(SAVE_DIR):
#     os.makedirs(SAVE_DIR)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/capture', methods=['POST'])
# def capture():
#     img_data = request.form['image']
#     img_data = img_data.split(',')[1]
#     img_bytes = base64.b64decode(img_data)

#     timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M')
#     filename = f'img-{timestamp}.jpg'
#     filepath = os.path.join(SAVE_DIR, filename)

#     with open(filepath, 'wb') as f:
#         f.write(img_bytes)

#     return {'status': 'success', 'filename': filename}
from flask import Flask, render_template, request, jsonify
import os
import base64
from datetime import datetime
from pathlib import Path

app = Flask(__name__)

# 1️⃣ Get path to Desktop + Customer-Photo folder
desktop = Path.home() / "Desktop"
save_dir = desktop / "Customer-Photo"
os.makedirs(save_dir, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture', methods=['POST'])
def capture():
    data_url = request.form['image']
    header, encoded = data_url.split(",", 1)
    image_data = base64.b64decode(encoded)

    now = datetime.now().strftime("%Y-%m-%d-%H-%M")
    filename = f"img-{now}.jpg"
    filepath = save_dir / filename

    with open(filepath, "wb") as f:
        f.write(image_data)

    return jsonify({"status": "success", "filename": str(filename)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000)
