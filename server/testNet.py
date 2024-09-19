import requests
# 用来测试，需要修改主机地址
url = 'http://172.30.235.50:5000/upload/'
with open('img.png', 'rb') as f:
    files = {'image': f}  # 注意这里使用的是 'image' 作为键，与服务器端代码中的 'request.files['image']' 对应
    res = requests.post(url, files=files)
    with open('resimg.jpeg', 'wb') as f:
        f.write(res.content)


# import cv2
# img = cv2.imread('resimg.jpeg')
# res = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cv2.imwrite('resimg1.jpeg', res)