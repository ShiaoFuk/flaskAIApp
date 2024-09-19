from flask import Flask, request, send_file
import numpy
import io
from PIL import Image
import test
import time
from test import *
import cv2
app = Flask(__name__)

@app.route('/upload/', methods=['GET', 'POST'])
def recievePicture():
    try:
        img = request.files['image']
        img = img.read()
        img = io.BytesIO(img)
        img = Image.open(img)
        img = img.convert('RGB')
        img = np.array(img)
        # img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        #   处理开始-----------------------------------------------
        # detect_emotion是处理模型的函数
        img = detect_emotion(img)
        img = Image.fromarray(numpy.uint8(img))
        #   处理结束-----------------------------------------------

        imgio = io.BytesIO()
        img.save(imgio, 'JPEG')
        imgio.seek(0)
        return send_file(imgio, mimetype='image/jpeg')
    except Exception as e:
        # 防止出错崩溃，记录日志
        print(e)
        if imgio is not None:
            imgio.close()
        return '', 204

if __name__ == '__main__':
    # 可以自行修改端口
    app.run(host="0.0.0.0", port=5000)