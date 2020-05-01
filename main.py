## python -m http.server
## from the output folder to open http on 8000 port
from flask import Flask, render_template, request, Response
import os
import recog


app = Flask(__name__)
#NOTE:This one have yet nothing to do with pathing issue it is just configue for input and output image, work on it later
#this have something to do with the file recog.py
app.config['UPLOAD_FOLDER'] = r'/Users/nhatcao/Face-Recognition-WebApp/input_folder' #image will be pass into this folder
app.config['OUTPUT_FOLDER'] = r'/Users/nhatcao/Face-Recognition-WebApp/out_folder'

### front page
@app.route('/')
def front_page():
   return render_template('index1.html')


#These mine have something to do with file in templates
#TODO: Need to find way to solve this pathing issue here
### image processingcl
@app.route('/main1')
def main_page():
   return render_template('image_load1.html')

#TODO:Solve this pathing issue here
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
      return render_template('image_load.html',ident=name)


if __name__ == '__main__':
   app.run(debug=True)
   # app.run(host= '0.0.0.0', debug = True)
