## python -m http.server
## from the output folder to open http on 8000 port
from flask import Flask, render_template, request, Response
import os
import recog


app = Flask(__name__)
#NOTE:This one have yet nothing to do with pathing issue it is just configue for input and output image, work on it later
#this have something to do with the file recog.py

#TODO: two path below you will need to adjust to work with your own computer system
app.config['UPLOAD_FOLDER'] = r'/Users/nhatcao/Face-Recognition-WebApp/input_folder' #the original image after upload will be store in this file
app.config['OUTPUT_FOLDER'] = r'/Users/nhatcao/Face-Recognition-WebApp/out_folder' #the output image after solving and recognizing will be in this file

###rendering front page
@app.route('/')
def front_page():
   return render_template('index1.html')

###redering image process image processing
@app.route('/main1')
def main_page():
   return render_template('image_load1.html')

#rendering upload page
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], 'inp.png')) #where it names image inp.png
      #name = os.system("python recog.py")
      name = recog.identify_face()
      print(name)
      if len(name)==0:
          name="Not Able to Recognize!!"
      else:
          name='Hi '+name[0].split(':')[0]+'!'
      #TODO: after you submit the image, this code will render 'html' page which have image with it
      #TODO: This page is now rendered succesfully but the image is not appearing due to path isse in the html page
      #TODO: Go to the html page to deal with it
      return render_template('image_load.html',ident=name)


if __name__ == '__main__':
   app.run(debug=True) #my path using local host
   # app.run(host= '0.0.0.0', debug = True) #original path I believe they use some kind of host , will not work
