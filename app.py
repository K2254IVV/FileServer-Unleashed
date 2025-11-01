from flask import Flask, render_template, url_for, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Получаем список файлов из папки static
    static_dir = 'static'
    files = []
    for filename in os.listdir(static_dir):
        filepath = os.path.join(static_dir, filename)
        if os.path.isfile(filepath):
            files.append(filename)
    
    return render_template('index.html', files=files)

@app.route('/download/<path:filename>')
def download_file(filename):
    # Отправляем файл с заголовком, указывающим на скачивание
    file_path = os.path.join('static', filename)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)