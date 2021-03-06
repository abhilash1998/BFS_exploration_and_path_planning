#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 19:15:58 2021

@author: abhi
"""



from exploration_r import exploration_r
import numpy as np
import cv2

image=255*np.ones((300,400,3))
#print(image)
parent_orignal_data=[]



#Inputting coordinates
print(" Start coordinates ")
s_y=input(" x_coordinate : ")
s_x=input(" y_coordinate : ")
print(" Goal coordinates ")
g_y=input(" x_coordinate : ")
g_x=input(" y_coordinate : ")
#print(s_x,s_y,g_x,g_y)
start=[int(s_x),int(s_y)]
goal=[int(g_x),int(g_y)]
i=0
image=image.astype(np.uint8)



# object of class
exploration=exploration_r(start,goal)

exploration.obstacles_form(image)




out = cv2.VideoWriter('BFS_exploration.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 60, (400,300))


image_list=[]
state=exploration.obstacle_prone_area(image)
counter=1

while state:
    i=i+1
    counter=2

    pos_0,pos_1=exploration.frontier_list()


    image_list.append(image) #appending all image frames in list
    # calls all moves
    image,pos_r_0,pos_r_1=exploration.left_move(image,pos_0,pos_1,i)
    image,pos_r_0,pos_r_1=exploration.right_move(image,pos_0,pos_1,i)
    image,pos_u_0,pos_u_1=exploration.up_move(image,pos_0,pos_1,i)
    image,pos_d_0,pos_d_1=exploration.down_move(image,pos_0,pos_1,i)
    image,pos_ul_0,pos_ul_1=exploration.up_left_move(image,pos_0,pos_1,i)
    image,pos_ur_0,pos_ur_1=exploration.up_right_move(image,pos_0,pos_1,i)
    image,pos_dl_0,pos_dl_1=exploration.down_left_move(image,pos_0,pos_1,i)

    image,pos_dr_0,pos_dr_1=exploration.down_right_move(image,pos_0,pos_1,i)
    if exploration.goal_reached():
        break




    exploration.expanding(pos_0,pos_1)# checks if node has been expanded/visited or not or not


if counter ==2:
    path,image_list=exploration.backtracking(image,out,image_list)
    print(path)
    for img in image_list:
        cv2.imshow("img",img)
        out.write(img)
        if cv2.waitKey(1) & 0xFF==ord('q'):


            break
else:
    print("Goal or start point in the obstacle prone area")
out.release()
cv2.destroyAllWindows()
