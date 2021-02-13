# Neural Network Creator
> Create and generate Neural Networks without using heavy modules like Keras

## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Tutorial](#tutorial)
* [Status](#status)

## Screenshots
![Example screenshot](https://github.com/noel-friedrich/neural/blob/main/neural2884.PNG "Tkinter Visualization of Neural Network")

## Setup
> Download Python File/s  

> Installing them as Module using pip  
>> Tutorial: http://www.discoversdk.com/blog/how-to-create-a-new-python-module  

> Use as Class in your Project
>> Copy the File/s into your Project Folder  
>> Import the Class using `from neural import Neural`  
>> Create Neural Object using `yourObj = Neural(nodes) # see tutorial for closer description`

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
## Tutorial
```python
# setup network nodes with __init__(self, nodes)
# nodes has to be a two dimensional array, containing floats/integers, representing nodes  
> nodes = [[0,0],[0,0,0,0],[0,0,0]] # 2 input neurons, 1 hidden layer containing 4 neurons, 3 output neurons
> network1 = Neural(nodes)

# input values using  
> network1.input([1,2]) # pass 1D list

# show network (with Tkinter module, located in neuraldisplay.py) using  
> network1.show() # opens 1400px * 700px window
> network1.show(size = [x,y]) # modify window size

# update every weight to be random from -1 to 1  
> network1.shuffle()

# update every weight to be in range of +- amount of given weights (of another neural network)
> network1.shuffle_amount(amount) # amount will be devided by 100
> network1.shuffle_amount(50) # to achieve a learning rate of 0.5

# save network to file_name.txt to be loaded in later 
> network1.save(file_name) # file_name must be string ending in .txt (located in same directory)

# load network from file_name.txt to current network  
> network1.load(file_name) # file_name must be string ending in .txt (located in same directory)
```
## Status
Project is _IN PROGRESS_  
_todo list in PROJECT: __Neural Network maker___
