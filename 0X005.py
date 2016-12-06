#coding:utf-8
from PIL import Image
import argparse
import os
import time
import re  


gifFileName = 'test.gif'
ascii_char = list(r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
AMAX = 0
AMIN = 0
# def save_as_txtfile(txt):
#     with open('imgtochar.txt', 'wb') as f:
#         f.write(txt)
  
  
re_digits = re.compile(r'(\d+)')  
  
def emb_numbers(s):  
    pieces=re_digits.split(s)  
    pieces[1::2]=map(int,pieces[1::2])      
    return pieces

def get_evl(path):
    im = Image.open(path)
    a = output(im,120,50,1)
    amax = max(a)
    amin = min(a)
    return [amax,amin]

def gif2png(gifName):
    #使用Image模块的open()方法打开gif动态图像时，默认是第一帧
    im = Image.open(gifFileName)
    pngDir = gifFileName[:-4]
    #创建存放每帧图片的文件夹
    os.mkdir(pngDir)
    try:
        while True:

            #保存当前帧图片

            current = im.tell()

            jpg = im
            jpg = jpg.convert('RGB')
            jpg.save(pngDir+'\\'+str(current)+'.jpg')

            #获取下一帧图片

            im.seek(current+1)

    except EOFError:
        pass
    return pngDir

def get_gray(r, g, b):
    gray = int(0.299 * r + 0.587 * g + 0.114 * b)
    return gray

def select_ascii_char(r, g, b):
    gray = get_gray(r, g, b)  # ‘RGB－灰度值’转换公式
    # gray = int((gray-AMIN)/float(AMAX-AMIN)*AMAX)
    unit = 256.0/len(ascii_char)  # ascii_char中的一个字符所能表示的灰度值区间
    return ascii_char[int(gray/unit)-1]

def sort_strings_with_emb_numbers(alist):  
    aux = [(emb_numbers(s),s) for s in alist]  
    aux.sort()  
    return [s for __,s in aux]

def output(im, width=100, height=100,status=0):
    im = im.resize((width, height), Image.NEAREST)
    if status==0:
        txt = ""
        for h in xrange(height):
            for w in xrange(width):
                # print im.getpixel((w, h))
                txt += select_ascii_char(*im.getpixel((w, h))[:3])  # 此处请看详解（1)
        # txt += '\n'
        return txt
    else:
        a = []
        for h in xrange(height):
            for w in xrange(width):
                gray = get_gray(*im.getpixel((w, h))[:3])
                a.append(gray)
        return a

if __name__ == '__main__':
    path = gif2png(gifFileName)
    list = os.listdir(path)
    list = sort_strings_with_emb_numbers(list)
    while True:
        for i in os.listdir(path):
            a = get_evl(path+'/'+i)
            AMAX = a[0]
            AMIN = a[1]
            im = Image.open(path+'/'+i)
            print output(im, 200, 115)
            time.sleep(0.1)
            os.system('cls')
            # print ''
    # os.rmdir('*.jpg')