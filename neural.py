import random as r
import ast as a
import math
import numpy as np
import copy
from statistics import mean
from neuraldisplay import NeuralDisplay

class Neural:

    def __init__(self, nodes):
        self.links = {}
        self.change = {}
        self.nodes = []
        for layer in nodes:
            new_layer = []
            for neuron in layer:
                new_layer.append({"output" : 0.0})
            self.nodes.append(new_layer)
            
        for i in range(len(nodes) - 1):
            self.generate_link(nodes[i], nodes[i + 1], i)

    def generate_link(self, s1, s2, num):
        self.links["l" + str(num)] = {}
        for i in range(len(s2)):
            for k in range(len(s1)):
                self.links["l" + str(num)][str(i) + "-" + str(k)] = 0

    def input(self, inputs):
        for i in range(len(self.nodes[0])):
            self.nodes[0][i]["output"] = float(inputs[i])
        self.calculate()
        out = list()
        for o in self.nodes[-1]:
            out.append(o["output"])
        return out

    def calculate(self):
        for i in range(len(self.nodes) - 1):
            for k in range(len(self.nodes[i + 1])):
                ergebnis = []
                for n in range(len(self.nodes[i])):
                    v = self.nodes[i][n]["output"] * (self.links["l" + str(i)][str(k) + "-" + str(n)])
                    ergebnis.append(v)
                if i == len(nodes) - 2:
                    self.nodes[i+1][k]["output"] = mean(ergebnis)
                else:
                    self.nodes[i+1][k]["output"] = self.sigmoid(mean(ergebnis))
                
    def sigmoid(self, x):
        if x < 0: return np.exp(x) / (1 + np.exp(x))
        else: return 1 / (1+ np.exp(-x))

    def shuffle(self):
        for layer in list(self.links.keys()): 
            for link in list(self.links[layer].keys()):
                rndm_int = r.randint(-100,100) / 100
                if rndm_int == 0: rndm_int = 0.00001
                self.links[layer][link] = rndm_int

    def show(self, size=[1400,700]):
        if type(size) != list or len(size) != 2:
            raise Exception("size expected to be list: (x,y)")
        display = NeuralDisplay()
        display.show(self.nodes, self.links, size)

    def save(self, file_name):
        with open(file_name, "w") as file:
            file.write(str(self.links))

    def load(self, file_name):
        with open(file_name) as file:
            self.links = a.literal_eval(file.read())

    def shuffle_amount(self, amount):
        for layer in list(self.links.keys()): 
            for link in list(self.links[layer].keys()):
                self.links[layer][link] += r.randint(-amount, amount) / 100
