from tkinter import *

class NeuralDisplay:

    def show(self, nodes, links, size):
        root  = Tk()

        canvas = Canvas(root, width=size[0], height=size[1])
        canvas.pack()

        max_link = self.get_max(links)
        for i in range(len(links)):
            for node in range(len(nodes[i])):
                for next_node in range(len(nodes[i + 1])): 
                    pos1 = self.get_node_coords(nodes, i, node, size)
                    pos2 = self.get_node_coords(nodes, i + 1, next_node, size)
                    hex_color, w = self.get_color(i, node, links, next_node, max_link)
                    canvas.create_line(pos1[0], pos1[1], pos2[0], pos2[1], fill=hex_color, width=w)

        for node, x_pos in zip(nodes, self.get_layer_pos(nodes, size[0])):
            for y_pos in self.get_layer_pos(node, size[1]):
                self.circle(canvas, x_pos, y_pos, 30)

        mainloop()

    def get_max(self, links):
        maximal = 0
        for layer in list(links.keys()): 
            for link in list(links[layer].keys()):
                if abs(links[layer][link]) > maximal:
                    maximal = abs(links[layer][link])
        return maximal

    def get_color(self, i, node, links, next_node, max_link):
        value = abs(links["l" + str(i)][str(next_node) + "-" + str(node)])
        if max_link == 0: max_link = 1
        percent = 100 * value / max_link
        out = "#0000" + format(int(percent)*2, '#04x')[2:]
        return out, percent / 15

    def get_node_coords(self, nodes, i, node, size):
        x = (i + 1) * (size[0] // (len(nodes) + 1))
        y = (node + 1) * (size[1] // (len(nodes[i]) + 1))
        return [x,y]

    def circle(self, canvas,x,y, r):
        id = canvas.create_oval(x-r,y-r,x+r,y+r, width=3)
        return id

    def get_layer_pos(self, nodes, size):
        step = size // (len(nodes) + 1)
        output_layer_pos = []
        for i in range(len(nodes)):
            output_layer_pos.append(step * (i + 1))
        return output_layer_pos
