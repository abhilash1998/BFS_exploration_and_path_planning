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
