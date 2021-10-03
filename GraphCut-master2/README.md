# GraphCut

本项目参考了https://github.com/NathanZabriskie/GraphCut 
fix some bug due to the Qt4 and path
implement GUI in graphCut_new.py

## 运行环境
python3.6
Qt5
所需库函数：numpy,opencv-python,PyMaxflow     

## GraphCut_new代码运行步骤[recommend]
1. run GraphCut_new.py
2. use the GUI interface to make the frontground seed and background seed.

## GraphCut代码运行步骤
1.python -i [输入文件名] -o [输出文件名]  
2.使用鼠标进行前后背景标注  
3.功能：  
  （1）‘esc’：退出；  
  （2）‘c’：清除所有标注；  
  （3）‘g’：进行图片分割；  
  （4）‘t’：前后背景标准的切换；  
  （5）‘s’：将分割后的图片保存到输出文件。  
