import cv2
import os
if 'data' not in os.listdir('./result'):
    os.mkdir('./result') 
path = './data'
files = os.listdir(path)
for file in files:
    img = cv2.imread(path + '/' + file)
    x = img.shape[1]/4
    y = img.shape[0]/4
    img = cv2.resize(img, (int(x), int(y)),interpolation=cv2.INTER_CUBIC)
    cv2.imwrite('./data/' + file[:-4] + '.png', img)
    print(file[:-4] + '.png' + ' have been transformed!')
