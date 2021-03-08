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
