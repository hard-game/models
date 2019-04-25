# coding:utf-8
import os
from PIL import Image


# bmp 转换为jpg，灰度图转RGB
def bmpToJpg_grayToRGB(file_path,file_save_path):
   for fileName in os.listdir(file_path):
       print(fileName)
       newFileName = fileName[0:fileName.find(".bmp")]+".jpg"
       print(newFileName)
       im = Image.open(file_path+"\\"+fileName)
       rgb = im.convert('RGB')      #灰度转RGB
       rgb.save(file_save_path+"\\"+newFileName)

# 删除原来的位图
def deleteImages(file_path, imageFormat):
   command = "del "+file_path+"\\*."+imageFormat
   os.system(command)

def main():
   file_path = "D:\\L\\final\\result_bmp"
   file_save_path = "D:\\L\\final\\result_jpg"
   bmpToJpg_grayToRGB(file_path,file_save_path)
   #deleteImages(file_path, "bmp")

if __name__ == '__main__':
   main()
