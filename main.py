from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload_csv():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    separator = ","
    if 'sep' in request.form:
        separator = request.form.get('sep')
    else:
        print("default sep ,")

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    try:
        df = pd.read_csv(file, sep=separator)
        header = list(df.columns)
        preview_rows = df.head().to_dict(orient='records')

        return jsonify({'header': header, 'preview_rows': preview_rows})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == "__main__":
    app.run(debug=True)
