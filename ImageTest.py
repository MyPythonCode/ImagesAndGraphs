from scipy.misc import imread, imsave, imresize
import matplotlib.pyplot as plt
import numpy as np

img = imread("cat.jpg")

plt.imshow(img)
plt.show()

img2 = img * [1,0,0]
plt.imshow(img2)
plt.show()


x = np.arange(0,3*np.pi, 0.1)
y = np.sin(x)
plt.plot(x,y)
y1 = np.cos(x)
plt.plot(x,y1)
plt.xlabel('x')
plt.ylabel('y')
plt.title("first graph")
plt.legend(['sin', 'cos'])
plt.show()


plt.subplot(1,2,1)
plt.plot(x,y)
plt.subplot(1,2,2)
plt.plot(x,y1)
#plt.imshow..... if we want to add image insted of graphs
plt.show()







