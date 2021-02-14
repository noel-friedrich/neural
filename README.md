# Neural Network Creator
> Create and generate Neural Networks without using heavy modules like Keras

## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Tutorial](#tutorial)
* [Status](#status)

## Example Code
```python
>>> from neural import Neural
>>> nodes = [[0,0], # 2 Input Neurons
>>>          [0,0,0,0,0,0], # 6 Hidden Neurons (Hidden Layer #1)
>>>          [0,0,0,0,0,0], # 6 Hidden Neurons (Hidden Layer #2)
>>>          [0,0,0,0]] # 4 Output Neurons
>>> n = Neural(nodes) # make Neural Object, __init__ requires nodes
>>> n.shuffle() # shuffle all weights to be random (using random module)
>>> print(n.input([1,2,3,4]) # print out output neurons with input list
>>> n.show() # visualize network using Tkinter
>>> n.save("my_neural_network.txt") # save network to file_name.txt
```

## Setup
1. Download Python File/s  

2. Installing them as Module using pip  
> Tutorial: http://www.discoversdk.com/blog/how-to-create-a-new-python-module  
> Exporting as a _Public Module_ soon!

2. Use as Class in your Project
> 1. Copy the File/s into your Project Folder  
> 2. Import the Class using `from neural import Neural`  
> 3. Create Neural Object using `yourObj = Neural(nodes) # see `[Tutorial](#tutorial)` for closer description`

## Tutorial
```python
# setup network nodes with __init__(self, nodes)
# nodes has to be a two dimensional array, containing floats/integers, representing nodes  
> nodes = [[0,0],[0,0,0,0],[0,0,0]] # 2 input neurons, 1 hidden layer containing 4 neurons, 3 output neurons
> network1 = Neural(nodes) # create Neural Object

# input values using  
> network1.input([1,2]) # pass 1D list, len must be equal to number of input neurons

# show network (with Tkinter module, located in neuraldisplay.py) using  
> network1.show() # opens 1400px * 700px window
> network1.show(size = [x,y]) # modify window size

# update every weight to be random from -1 to 1  
> network1.shuffle() # uses random module

# update every weight to be in range of +- amount of given weights (of another neural network)
> network1.shuffle_amount(amount) # amount will be devided by 100
> network1.shuffle_amount(50) # to achieve a learning rate of 0.5

# save network to file_name.txt to be loaded in later 
> network1.save(file_name) # file_name must be string ending in .txt (located in same directory)

# load network from file_name.txt to current network  
> network1.load(file_name) # file_name must be string ending in .txt (located in same directory)
```
### Training using Backpropagation
```python
# setup network nodes with __init__(self, nodes)
# nodes has to be a two dimensional array, containing floats/integers, representing nodes  
> nodes = [[0,0],[0,0,0,0],[0,0]] # 2 input neurons, 1 hidden layer containing 4 neurons, 2 output neurons
> network1 = Neural(nodes) # create Neural Object

# load the training data using (see Training Data Formating)
> inputs, outputs = network1.load_training_data("training_example.txt") # must be .txt file in the same directory

# train the network using
> network1.train(l_rate, # learning rate (e.g. 0.2)
                 cycles, # how many cycles (epochs) the network will train through (e.g. 1000)
                 inputs, # inputs set from loading the training data
                 outputs, # outputs set from loading the training data
                 print_status=True) # (optional) print progress into console (Default is False)

# get the total score using (how many of your training examples it passes)
> score, max_score = network1.get_total_score(inputs, outputs) # set score and max_score
> print(f"{score}/{max_score}") # python 3 (f-strings)
```
#### Training Data Formatting
> Training Data to be read must be located in yourfilename.txt file  
> Inputs must be seperated by Comma (e.g. ```1,2,3,4```)  
> Outputs must be seperated by Comma (e.g. ```0,1,0```)  
> Inputs and Outputs must be seperated by equal sign (e.g. ```1,2,3,4=0,1,0```) ending in line break ("\n")  
> see "training_example.txt"  

## Screenshots
![Example screenshot](https://github.com/noel-friedrich/neural/blob/main/neural2884.PNG "Tkinter Visualization of Neural Network")

## Status
Project is _IN PROGRESS_  
_todo list in PROJECT: __Neural Network maker___  
https://github.com/noel-friedrich/neural/projects/1
