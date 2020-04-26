import os
from werkzeug.utils import secure_filename
from flask import Flask, request, redirect, url_for, send_from_directory, render_template,send_file
from flask import Flask


app = Flask(__name__)


ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])
IMAGE_SIZE = (224, 224)#150,150 old
UPLOAD_FOLDER = 'uploads'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def template_test():
    return render_template('upload1.html')
	

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
       
        if file and allowed_file(file.filename):
           filename = secure_filename(file.filename)
           file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
           file.save(file_path)

                   


        return render_template('download.html')



@app.route('/download')
def download_file():
	#path = "html2pdf.pdf"
	#path = "info.xlsx"
	path = "C:/Users/Ankita/Desktop/flask2working/masked_image.png"
	#path = "sample.txt"
	return send_file(path, as_attachment=True)

		
if __name__ == "__main__":
    app.run(debug=True, threaded=False)



           

	
	

	
