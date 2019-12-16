from flask import Flask,render_template,request
import warnings
import tensorflow

with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=FutureWarning)
    import tensorflow as tf
    import load
    import re,base64,cv2
    import numpy as np
    from crop import borders
    

app = Flask(__name__)
model=load.init()


@app.route('/')
def index():
	return render_template("index.html")

def model_predict(img_path, model):
    img=cv2.imread(img_path,0)
    _,img=cv2.threshold(img,128,255,cv2.THRESH_BINARY_INV)
    img=cv2.resize(img,(32,32))
    top,bottom,b=borders(img,0)
    img=img[top:bottom]
    cv2.imwrite('abc.png',img)
    img=img.reshape(-1,32,32,1)/255
    preds = model.predict(img)
    print(preds)
    return preds


@app.route('/predict/',methods=['GET','POST'])
def predict():
    imgData = request.get_data()
    imgData=str((imgData), 'utf-8')
    imgstr = re.search(r'base64,(.*)',imgData).group(1)

    with open('output.png','wb') as output:
        output.write(np.fromstring(base64.b64decode(imgstr), np.uint8))
    file_path='output.png'
    result = model_predict(file_path, model)
    response=np.argmax(result)
    diction={10: 'क',
 21: 'ख',
 29: 'ग',
 30: 'घ',
 31: 'ङ',
 32: 'च',
 33: 'छ',
 34: 'ज',
 35: 'झ',
 0: 'ञ',
 1: 'ट',
 2: 'ठ',
 3: 'ड',
 4: 'ढ',
 5: 'ण',
 6: 'त',
 7: 'थ',
 8: 'द',
 9: 'ध',
 11: 'न',
 12: 'प',
 13: 'फ',
 14: 'ब',
 15: 'भ',
 16: 'म',
 17: 'य',
 18: 'र',
 19: 'ल',
 20: 'व',
 22: 'श',
 23: 'ष',
 24: 'स',
 25: 'ह',
 26: 'क्ष',
 27: 'त्र',
 28: 'ज्ञ',
 37: '०',
 38: '१',
 39: '२',
 40: '३',
 41: '४',
 42: '५',
 43: '६',
 44: '७',
 45: '८'}
    return diction[response]



if __name__ == "__main__":
    app.run(debug=True)
