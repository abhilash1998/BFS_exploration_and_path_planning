The code is done on Anaconda  on Python 3.7 and recommended to perform on the same if possible
This code has been runned on 32 gb Ram pc


Libraries and command to install those:

    Virtual Evirobnment with Python 3.7 : conda create -n myenv python=3.7 
    Numpy : conda install -c anaconda numpy
    Matplotlib : conda install -c conda-forge matplotlib 
    Imutils : conda install -c conda-forge imutils
    Opencv : conda install -c conda-forge opencv=4.0.1

Instruction to run the code:

    1. Create a Virtual Environment for python 3.7
        conda create -n myenv python=3.7
    2. Activate the Virtual Environment
        conda activate myenv 
    3. Install the Libraries and dependency
        conda install -c anaconda numpy
        conda install -c conda-forge matplotlib 
        conda install -c conda-forge opencv=4.0.1
        conda install -c conda-forge imutils
    4. The file contaions 2 script BFS_point.py and exploration_r.py and video respectively
	      So exploration_r.py files is a file or class module that has all the function related
        to solving the path planning problem using BFS and BFS_point.py is the main file that 
        calls those function to solve the corresponding path planning problem
    5. The y and x coordinate are given from 0-299 and 0-399 respectively 
    6. Please enter the x coordinate y coordinate of the state and then x coordinate and y coordiante of the goal
    7.It shows when goal is reached and then prints the Path
    8. It explore little more states after reaching the goal. 

