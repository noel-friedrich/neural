# neural
Neural Network Maker Class

HOW TO USE

> setup network nodes with __init__(self, nodes)
> nodes has to be a two dimensional array, containing floats/integers, representing nodes
>> nodes = [[0,0],[0,0,0,0],[0,0,0]] # 2 input neurons, 1 hidden layer containing 4 neurons, 3 output neurons 
>> network1 = Neural(nodes)

> input values using
>> network1.input([1,2]) # pass 1D list

> show network (with Tkinter module, located in neuraldisplay.py) using
>> network1.show() # opens 1400px * 700px window
>> network1.show(size = [x,y]) # modify window size

> update every weight to be random from -1 to 1
>> network1.shuffle()

> update every weight to be in range of +- amount of given weights (of another neural network)
>> network1.shuffle_amount(amount) # amount will be devided by 100
>> network1.shuffle_amount(50) # to achieve a learning rate of 0.5

> save network to file_name.txt to be loaded in later
>> network1.save(file_name) # file_name must be string ending in .txt (located in same directory)

> load network from file_name.txt to current network
>> network1.load(file_name) # file_name must be string ending in .txt (located in same directory)

EXAMPLE CODE

>>> from neural import Neural
>>> nodes = [[0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0]]
>>> n = Neural(nodes)
>>> n.shuffle()
>>> n.show()
>>> n.save("my_neural_network.txt")
