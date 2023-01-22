
import pandas as pd
import math
z=[1,-1,2,-1]#sample
dis=20#sample
horizonatal_angle=20#sample
vertical_angle=20#sample
data1={'index':[1,2,3,4],'x1':[2,-3,-3,2],'y1':[4,5,-1,-1],'z1':[0,0,0,0],'x2':[4,-1,-1,4],'y2':[1,1,-4,-4],'z2':[2,-2,2,-2],'zone':["q1f","q2b","q3f","q4b"]}#sample
new1=pd.DataFrame.from_dict(data1)
for j in z:
    distance_object=dis-j
    teeta_H=math.tan(horizonatal_angle)
    teeta_V=math.tan(vertical_angle)

    a=teeta_H*distance_object
    b=teeta_V*distance_object
    
    for i in range(len(new1['index'])):
        if new1['x1'][i]< a <  new1['x2'][i]:
            if new1['y1'][i]< b <  new1['y2'][i]:
                if new1['z1'][i] < j < new1['z2'][i]:
                    print(new1['zone'][i])
                elif new1['z1'][i] > j > new1['z2'][i]:
                    print(new1['zone'][i])
            elif new1['y1'][i]> b >  new1['y2'][i]:
                if new1['z1'][i] < j < new1['z2'][i]:
                    print(new1['zone'][i])
                elif new1['z1'][i] > j > new1['z2'][i]:
                    print(new1['zone'][i])
    print(j)