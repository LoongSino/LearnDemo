import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

# 生成数据
x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# 绘制图形
plt.plot(x, y1, label="sin")
plt.plot(x, y2, label="cos", linestyle="--")
plt.xlabel("x")     # x轴标签
plt.ylabel("y")     # y轴标签
plt.title('sin & cos')  # 标题
plt.legend(loc="upper right")   # 添加图例
plt.show()

# 显示图像
img = imread('../dataset/logo.png')
plt.imshow(img)
plt.show()




