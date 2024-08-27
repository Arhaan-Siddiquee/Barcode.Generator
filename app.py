from flask import Flask, render_template, request, send_file
import barcode
from barcode.writer import ImageWriter
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_barcode():
    code = request.form['code']
    barcode_format = barcode.get_barcode_class('code128')
    generated_barcode = barcode_format(code, writer=ImageWriter())
    
    buffer = BytesIO()
    generated_barcode.write(buffer)
    buffer.seek(0)
    
    return send_file(buffer, mimetype='image/png', as_attachment=True, download_name='barcode.png')

if __name__ == '__main__':
    app.run(debug=True)
