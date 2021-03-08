#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 12:56:40 2021

@author: abhi
"""
import numpy as np
import cv2
class exploration_r:
    def __init__(self,start,goal):
        """
        Intializes variables for the class. Stores the goal state and
        start state


        Parameters
        ----------
        start : list
            Starting point coordinates
        goal : list
            Goal point coordinates

        """
        self.ground_truth={}

        self.obstacle=[]

        self.expanded=[]

        self.parent=[]
        self.parent_orignal_data={}

        self.start=start
        self.frontier=[self.start]

        self.frontier_string=[]

        self.cost=0
        self.goal=goal
        self.data_with_string={}

        self.current_score="00"

    def obstacle_prone_area(self,image):
        """
        Checks if the goal state or start state is in the obstacle area

        Parameters:
        -----------
        image : np.array
            Inputs image for adding obstacle

        Returns
        -------
        Boolean : Boolean
            Returns True if wither of goal or start is in obstacle space
            else returns False


        """

        start_x=self.start[0]
        start_y=self.start[1]
        goal_x=self.goal[0]
        goal_y=self.goal[1]
        if (np.array_equiv(image[299-goal_x,goal_y,:],np.array([0,0,0]))) or (np.array_equiv(image[299-start_x,start_y,:],np.array([0,0,0]))):
            #print(1)
            return False
        else:
            #print(2)
            return True


    def obstacles_form(self,image):
        """
        Create all obstacles in the images by calling various obstacle functions

        Parameters
        ----------
        image : np.array
            InputsImage for adding obstacle
        """
        major_axis=60
        minor_axis=30
        c_y=246
        c_x=145
        c_y1=90
        c_x1=70
        radius=35
        for i in range(len(image)):
            for  j in range(len(image[0])):

                self.ellipse(image,major_axis,minor_axis,i,j,c_x,c_y)
                self.circle(image,radius,i,j,c_x1,c_y1)
                self.slanted_rect(image,i,j)
                self.polygon(image,i,j)
                self.c_shape(image,i,j)
        #exploration.c_shape(image,i,j)
    def goal_reached(self):
        """
        Checks if the goal is reached or not if reached return True
        and if not reached continues exploring

        Parameters
        ----------

        Returns
        -------
        Boolean : bool
            True or False depending on the current state reached the goal or not

        """
        pos_0=self.goal[0]
        pos_1=self.goal[1]
        self.start_score=self.string(self.start[0],self.start[1])
        self.data_with_string[self.start_score]=self.start
        self.goal_score=self.string(pos_0,pos_1)
        if int(self.current_score) ==int(self.goal_score) :
            print("goal_reached")
            #print(len(self.expanded))
            #print("self.expanded",self.expanded)
            return True
        return False
    def string(self,pos_0,pos_1):
        """
        Converts the list of the state into string for easy comparison
        when further converted into integer

        Parameters
        ----------
        pos_0 : Int
            x-coordinate of current state
        pos_0 : Int
            y-coordinate of current state

        Returns
        -------
        c : str
            String of the state

        """

        if pos_0 <10:
            pos_0="00"+str(pos_0)
        elif pos_0<100:
            pos_0="0"+str(pos_0)


        if pos_1 <10:
            pos_1="00"+str(pos_1)
        elif pos_1<100:
            pos_1="0"+str(pos_1)


        #pos
        c=""

        c=str(pos_0)+str(pos_1)
        #print("c",c)
        return c

    def left_move(self,image,pos_0,pos_1,cost):
     """

     This function makes a move in the left direction returns or update the
     resultant node and checks if the move node is in the visited list
     or unvisited list

     Parameters
     ----------
     image: np.array
         It is a image of the  states from where in the exploration happens
     pos_0 : Int
         x_coordinate of the current node
     pos_1 : Int
         y_coordinate of the current node
     cost : Int
        It is cost for each step(Introduce to implement Djisktras in future)

     Returns
     -------
     image: np.array
         It is a image of the  states after left move
     pos_0 : Int
         x_coordinate of the  node after left move
     pos_1 : Int
         y_coordinate of the node after left move

     """
     if pos_1>0:
         #solve_t=solve_a
         #solve_t=deepcopy(list(solve_a))
         #temp1=deepcopy(list(solve_a))

         #temp=[pos_0,pos_1]
         parent=self.string(pos_0,pos_1)
             #temp.clear()
             #parent=score
         pos_1=pos_1-1



         score=self.string(pos_0,pos_1)


         if np.array_equiv(image[299-pos_0,pos_1,:],np.array([0,0,0])) or  np.array_equiv(image[299-pos_0,pos_1,:],np.array([200,200,0])):
             return image,pos_0,pos_1

         else:

            self.parent_orignal_data[score]=parent
            self.data_with_string[score]=[pos_0,pos_1]
            image[299-pos_0,pos_1,:]=200,200,0
            self.frontier.append([pos_0,pos_1])
            #self.frontier_string.append(int(score))
            image=image.astype(np.uint8)
     return image,pos_0,pos_1

    def right_move(self,image,pos_0,pos_1,cost):
         """
            This function makes a move in the right direction returns or update the
            resultant node and checks if the move node is in the visited list
            or unvisited list

            Parameters
            ----------
            image: np.array
                It is a image of the  states from where in the exploration happens
            pos_0 : Int
                x_coordinate of the current node
            pos_1 : Int
                y_coordinate of the current node
            cost : Int
               It is cost for each step(Introduce to implement Djisktras in future)

            Returns
            -------
            image: np.array
                It is a image of the  states after right move
            pos_0 : Int
                x_coordinate of the  node after right move
            pos_1 : Int
                y_coordinate of the node after right move
         """
         if pos_1<len(image[1])-1:


             parent=self.string(pos_0,pos_1)
              #parent=score
             pos_1=pos_1+1

             score=self.string(pos_0,pos_1)
             if np.array_equiv(image[299-pos_0,pos_1,:],np.array([0,0,0])) or  np.array_equiv(image[299-pos_0,pos_1,:],np.array([200,200,0])):
                 return image,pos_0,pos_1


             else:

                self.parent_orignal_data[score]=parent
                self.data_with_string[score]=[pos_0,pos_1]
                image[299-pos_0,pos_1,:]=200,200,0
                self.frontier.append([pos_0,pos_1])
                #self.frontier_string.append(int(score))
                image=image.astype(np.uint8)
         return image,pos_0,pos_1
    def down_move(self,image,pos_0,pos_1,cost):
          """
             This function makes a move in the down direction returns or update the
             resultant node and checks if the move node is in the visited list
             or unvisited list

             Parameters
             ----------
             image: np.array
                 It is a image of the  states from where in the exploration happens
             pos_0 : Int
                 x_coordinate of the current node
             pos_1 : Int
                 y_coordinate of the current node
             cost : Int
                It is cost for each step(Introduce to implement Djisktras in future)

             Returns
             -------
             image: np.array
                 It is a image of the  states after down move
             pos_0 : Int
                 x_coordinate of the  node after down move
             pos_1 : Int
                 y_coordinate of the node after down move
          """
          if pos_0<len(image)-1:
             parent=self.string(pos_0,pos_1)


             pos_0=pos_0+1


             score=self.string(pos_0,pos_1)

             if np.array_equiv(image[299-pos_0,pos_1,:],np.array([0,0,0])) or  np.array_equiv(image[299-pos_0,pos_1,:],np.array([200,200,0])):
                 return image,pos_0,pos_1

             else:

                self.parent_orignal_data[score]=parent
                self.data_with_string[score]=[pos_0,pos_1]
                image[299-pos_0,pos_1,:]=200,200,0
                self.frontier.append([pos_0,pos_1])
                #self.frontier_string.append(int(score))
                image=image.astype(np.uint8)
          return image,pos_0,pos_1

    def up_move(self,image,pos_0,pos_1,cost):
         """
             This function makes a move in the up direction returns or update the
             resultant node and checks if the move node is in the visited list
             or unvisited list

             Parameters
             ----------
             image: np.array
                 It is a image of the  states from where in the exploration happens
             pos_0 : Int
                 x_coordinate of the current node
             pos_1 : Int
                 y_coordinate of the current node
             cost : Int
                It is cost for each step(Introduce to implement Djisktras in future)

             Returns
             -------
             image: np.array
                 It is a image of the  states after up move
             pos_0 : Int
                 x_coordinate of the  node after up move
             pos_1 : Int
                 y_coordinate of the node after up move
         """
         if pos_0>0:


             temp=[pos_0,pos_1]

             parent=self.string(pos_0,pos_1)

             pos_0=pos_0-1



             score=self.string(pos_0,pos_1)
             if np.array_equiv(image[299-pos_0,pos_1,:],np.array([0,0,0])) or  np.array_equiv(image[299-pos_0,pos_1,:],np.array([200,200,0])):
                 return image,pos_0,pos_1

             else:

                self.parent_orignal_data[score]=parent
                self.data_with_string[score]=[pos_0,pos_1]
                image[299-pos_0,pos_1,:]=200,200,0
                self.frontier.append([pos_0,pos_1])
                #self.frontier_string.append(int(score))
                image=image.astype(np.uint8)
         return image,pos_0,pos_1

    def down_right_move(self,image,pos_0,pos_1,cost):
         """
             This function makes a move in the down right direction returns or update the
             resultant node and checks if the move node is in the visited list
             or unvisited list

             Parameters
             ----------
             image: np.array
                 It is a image of the  states from where in the exploration happens
             pos_0 : Int
                 x_coordinate of the current node
             pos_1 : Int
                 y_coordinate of the current node
             cost : Int
                It is cost for each step(Introduce to implement Djisktras in future)

             Returns
             -------
             image: np.array
                 It is a image of the  states after down right move
             pos_0 : Int
                 x_coordinate of the  node after down right move
             pos_1 : Int
                 y_coordinate of the node after down right move
         """
         if pos_0<len(image)-1 and pos_1<len(image[0])-1:


             parent=self.string(pos_0,pos_1)
             pos_0=pos_0+1
             pos_1=pos_1+1
             score=self.string(pos_0,pos_1)
             if np.array_equiv(image[299-pos_0,pos_1,:],np.array([0,0,0])) or np.array_equiv(image[299-pos_0,pos_1,:],np.array([200,200,0])):
                 return image,pos_0,pos_1

             else:

                self.parent_orignal_data[score]=parent
                self.data_with_string[score]=[pos_0,pos_1]
                image[299-pos_0,pos_1,:]=200,200,0
                self.frontier.append([pos_0,pos_1])
                #self.frontier_string.append(int(score))
                image=image.astype(np.uint8)
         return image,pos_0,pos_1


    def down_left_move(self,image,pos_0,pos_1,cost):
         """
             This function makes a move in the down left direction returns or update the
             resultant node and checks if the move node is in the visited list
             or unvisited list

             Parameters
             ----------
             image: np.array
                 It is a image of the  states from where in the exploration happens
             pos_0 : Int
                 x_coordinate of the current node
             pos_1 : Int
                 y_coordinate of the current node
             cost : Int
                It is cost for each step(Introduce to implement Djisktras in future)

             Returns
             -------
             image: np.array
                 It is a image of the  states after down left move
             pos_0 : Int
                 x_coordinate of the  node after down left move
             pos_1 : Int
                 y_coordinate of the node after down left move
         """
         if pos_0<(len(image)-1) and pos_1>0:



             parent=self.string(pos_0,pos_1)
             pos_0=pos_0+1
             pos_1=pos_1-1

             score=self.string(pos_0,pos_1)
             if np.array_equiv(image[299-pos_0,pos_1,:],np.array([0,0,0]))or np.array_equiv(image[299-pos_0,pos_1,:],np.array([200,200,0])):
                 return image,pos_0,pos_1

             else:

                self.parent_orignal_data[score]=parent
                self.data_with_string[score]=[pos_0,pos_1]
                image[299-pos_0,pos_1,:]=200,200,0
                self.frontier.append([pos_0,pos_1])
                #self.frontier_string.append(int(score))
                image=image.astype(np.uint8)
         return image,pos_0,pos_1


    def up_left_move(self,image,pos_0,pos_1,cost):
         """
             This function makes a move in the up left direction returns or update the
             resultant node and checks if the move node is in the visited list
             or unvisited list

             Parameters
             ----------
             image: np.array
                 It is a image of the  states from where in the exploration happens
             pos_0 : Int
                 x_coordinate of the current node
             pos_1 : Int
                 y_coordinate of the current node
             cost : Int
                It is cost for each step(Introduce to implement Djisktras in future)

             Returns
             -------
             image: np.array
                 It is a image of the  states after up left move
             pos_0 : Int
                 x_coordinate of the  node after up left move
             pos_1 : Int
                 y_coordinate of the node after up left move
         """
         if pos_0>0 and pos_1>0:


             parent=self.string(pos_0,pos_1)
             # parent=score
             pos_0=pos_0-1
             pos_1=pos_1-1


             score=self.string(pos_0,pos_1)


             if np.array_equiv(image[299-pos_0,pos_1,:],np.array([0,0,0])) or np.array_equiv(image[299-pos_0,pos_1,:],np.array([200,200,0])) :
                 return image,pos_0,pos_1

             else:

                self.parent_orignal_data[score]=parent
                self.data_with_string[score]=[pos_0,pos_1]
                image[299-pos_0,pos_1,:]=200,200,0
                self.frontier.append([pos_0,pos_1])
                #self.frontier_string.append(int(score))
                image=image.astype(np.uint8)

         return image,pos_0,pos_1

    def up_right_move(self,image,pos_0,pos_1,cost):
         """
             This function makes a move in the up right direction returns or update the
             resultant node and checks if the move node is in the visited list
             or unvisited list

             Parameters
             ----------
             image: np.array
                 It is a image of the  states from where in the exploration happens
             pos_0 : Int
                 x_coordinate of the current node
             pos_1 : Int
                 y_coordinate of the current node
             cost : Int
                It is cost for each step(Introduce to implement Djisktras in future)

             Returns
             -------
             image: np.array
                 It is a image of the  states after up right move
             pos_0 : Int
                 x_coordinate of the  node after up right move
             pos_1 : Int
                 y_coordinate of the node after up right move
         """
         if pos_0>0 and pos_1<len(image[1])-1:

             parent=self.string(pos_0,pos_1)

             pos_0=pos_0-1
             pos_1=pos_1+1

             score=self.string(pos_0,pos_1)




             if np.array_equiv(image[299-pos_0,pos_1,:],np.array([0,0,0]))or np.array_equiv(image[299-pos_0,pos_1,:],np.array([200,200,0])):
                 return image,pos_0,pos_1

             else:

                self.parent_orignal_data[score]=parent
                self.data_with_string[score]=[pos_0,pos_1]
                image[299-pos_0,pos_1,:]=200,200,0
                self.frontier.append([pos_0,pos_1])
                #self.frontier_string.append(int(score))
                image=image.astype(np.uint8)
         return image,pos_0,pos_1

    def expanding(self,pos_0,pos_1):
        """
            This function checks if the node is in expanded /visited list and
            if it not then appends in the expanded list


            Parameters
            ----------

            pos_0 : Int
                x_coordinate of the current node
            pos_1 : Int
                y_coordinate of the current node

            Returns
            -------

        """
        cnvt_front=self.string(pos_0,pos_1)
        if int(cnvt_front) in self.expanded:

            a=1
        else:
            self.expanded.append(int(cnvt_front))

    def frontier_list(self):
        """
            This function checks if the node is in expanded/visited list  and
            pops out untill it finds a node that has not been visited/expanded.


            Parameters
            ----------

            Returns
            -------

            pos_0 : Int
                x_coordinate of the current node
            pos_1 : Int
                y_coordinate of the current node



        """
        pos_0,pos_1=self.frontier.pop(0)
        self.current_score=self.string(pos_0,pos_1)
        if int(self.current_score) in self.expanded:

             self.frontier_list()
        elif int(self.current_score) in self.obstacle:
             self.frontier_list()
        #print("frontierlist",self.frontier)
        #print("expanded",self.expanded)
        return pos_0,pos_1

    def circle(self,image,radius,i,j,c_x,c_y):
        """
            This function give points that lies in circle.


            Parameters
            ----------
            image : np.array
                This is the image or state in which the location of obstacle is updated
            radius : Int
                Radius of the circle
            i : Int
                x_coordinate of point
            j : Int
                y coordinate of points
            c_x:Int
                x coordinate of center of the circle
            c_y:Int
                y coordinate of center of the circle
            Returns
            -------





        """
        major_axis=radius
        minor_axis=radius
        self.ellipse(image,major_axis,minor_axis,i,j,c_x,c_y)
    def ellipse(self,image,major_axis,minor_axis,i,j,c_x,c_y):
        """
            This function give points that lies in ellipse.


            Parameters
            ----------
            image : np.array
                This is the image or state in which the location of obstacle is updated
            radius : Int
                Radius of the circle
            major_axis: Int
                elongation of elipse across y axis
            minor_axis: Int
                elogation of ellipse across x axis
            i : Int
                x_coordinate of point
            j : Int
                y coordinate of points
            c_x:Int
                x coordinate of center of the circle
            c_y: Int
                y coordinate of center of the circle

            Returns
            -------





        """
        if (((i-c_x)/minor_axis)**2 + ((j-c_y)/major_axis)**2)<=1:
            #print("yes")
            image[299-i,j,:]=0,0,0
            #self.obstacle.append([i,j])
            self.obstacle.append(int(self.string(i,j)))
    def slanted_rect(self,image,i,j):
        """
            This function give points that lies in slanted rectangle.


            Parameters
            ----------
            image : np.array
                This is the image or state in which the location of obstacle is updated

            i : Int
                x_coordinate of point
            j : Int
                y coordinate of points


            Returns
            -------

        """
        if (-0.7*j+1*i)>=73.4 and (i+1.42814*j)>=172.55 and (-0.7*j+1*i)<=99.81 and (i+1.42814*j)<=429.07:
            image[299-i,j,:]=0,0,0
            self.obstacle.append(int(self.string(i,j)))
    def c_shape(self,image,i,j):
        """
            This function give points that lies in c shape.


            Parameters
            ----------
            image : np.array
                This is the image or state in which the location of obstacle is updated

            i : Int
                x_coordinate of point
            j : Int
                y coordinate of points


            Returns
            -------





        """

        if (j>=200  and j<=210 and i<=280 and i >=230) or (j>=200 and j<=230 and i<=280 and i>=270) or (j>=200 and j<=230 and i<=240 and i>=230):
            image[299-i,j,:]=0,0,0
            self.obstacle.append(int(self.string(i,j)))
    def polygon(self,image,i,j):
        """
            This function give points that lies in complex polygon.


            Parameters
            ----------
            image : np.array
                This is the image or state in which the location of obstacle is updated

            i : Int
                x_coordinate of point
            j : Int
                y coordinate of points


            Returns
            -------





        """
        if(i+j>=391 and j-i<=265 and i+0.81*j<=425.66 and  i+0.17*j<=200 and 0.89*j -i >=148.75) or   (13.5*j+i<=5256.72 and 1.43*j-i>=368.82 and i+0.81*j >=425.66):
            image[299-i,j,:]=0,0,0
            #print(2)
            self.obstacle.append(int(self.string(i,j)))
    def backtracking(self,image,out,image_list):
        """
            The function backtracks from goal to start node
            and gives an path


            Parameters
            ----------
            image : np.array
                This is the image or state in which the location of obstacle is updated
            out : np.array
                video writing array
            image_list:
                list of frames that have been saved  while exploring

            Returns
            -------
            path : list
                Returns the path that needs to be followed
            image_list : List
                Returns list of images/ frames used in exploration and backtracking




        """
        loop=self.parent_orignal_data[self.goal_score]


        path=[self.goal]

        while int(self.start_score)!=int(loop):
        #    pass

            #print("loop",loop)
            loop=self.parent_orignal_data[loop]
            index=self.data_with_string[loop]
            #print(index)
            path.append(index)
            image[299-index[0],index[1],:]=255,255,255
            image_list.append(image)

        return path,image_list
