#dependencies
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patch

 

yellow=patch.Rectangle((0,5),width=10,height=4,facecolor='#ffff08')

red=patch.Rectangle((0,1),width=10,height=4,facecolor='#ff0000')
_,plot=plt.subplots()
plot.add_patch(yellow)
plot.add_patch(red)
#plot.plot() #plotting 
 

plt.title('Happy Karnataka Rajyotsava')
plot.plot()
plt.show()
