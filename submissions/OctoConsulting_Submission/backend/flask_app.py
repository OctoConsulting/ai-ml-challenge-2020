import os
from flask import Flask, flash, request, redirect, url_for
from flask_cors import CORS
from werkzeug.utils import secure_filename
# import doc_to_classifications
# import download_model

#path to local upload_folder
UPLOAD_FOLDER = './testdata/uploads/'
FINISHED_FOLDER = './testdata/finished/'
#Allows .pdf and .doc
ALLOWED_EXTENSIONS = {'.pdf','.docx'}

app = Flask(__name__)
CORS(app)
app.secret_key = 'some secret key'
app.config['UPLOAD_FOLDER']= UPLOAD_FOLDER

#Allowed file types
def allowed_file(filename):
    return True
    # return '.' in filename and \
    #        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.after_request
def after_request(response):
  response.headers['Access-Control-Allow-Origin'] = '*'
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Access-Control-Allow-Credentials', 'true')
  return response

@app.route("/upload", methods=['GET','POST','OPTIONS'])
def upload_file():   
    print("METHOD: " + request.method)
    if request.method == 'OPTIONS':
        print("returning 204 for options")
        return "204"
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return ""
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return ""
        print(allowed_file(file.filename))    
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return ""
    return ""
    
@app.route("/getjson")
def getjson():
    f = open("testdata/fakedata.json", "r")
    content = f.read()
    return content

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

from werkzeug.middleware.shared_data import SharedDataMiddleware
app.add_url_rule('/uploads/<filename>', 'uploaded_file',
                 build_only=True)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
    '/uploads':  app.config['UPLOAD_FOLDER']
})

def dwnld_model():
    download_model.download_model_fr_drive()

def run_classification(filename):
    return doc_to_classifications.main_pipeline(filename)

if __name__ == '__main__':
    app.run()