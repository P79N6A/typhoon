import numpy as np
def iou(box1,box2):
　　  assert box1.size()==4 and box2.size()==4,"bounding box coordinate size must be 4"
      bxmin = np.max(box1[0],box2[0])
      bymin = np.max(box1[1],box2[1])
      bxmax = np.min(box1[2],box2[2])
      bymax = np.min(box1[3],box2[3])
      bwidth = bxmax-bxmin
      bhight = bymax-bxmin
      inter = bwidth*bhight
      union = (box1[2]-box1[0])*(box1[3]-box1[1])+(box2[2]-box2[0])*(box2[3]-box2[1])-inter
      return inter/union