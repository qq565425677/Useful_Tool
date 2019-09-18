import numpy as np 
from matplotlib import pyplot as plt 
import matplotlib
 
# fname 为 你下载的字体库路径，注意 SimHei.ttf 字体的路径
zhfont1 = matplotlib.font_manager.FontProperties(fname=r"C:\Windows\Fonts\simfang.ttf") 
 
x = np.arange(1,11) 
y =  2  * x +  5 
plt.title("菜鸟教程 - 测试", fontproperties=zhfont1) 
 
# fontproperties 设置中文显示，fontsize 设置字体大小
plt.xlabel("x轴", fontproperties=zhfont1)
plt.ylabel("y轴", fontproperties=zhfont1)
plt.xticks(fontstyle='italic',family='Times New Roman')
plt.yticks(fontstyle='italic',family='Times New Roman')
plt.plot(x,y) 
plt.show()