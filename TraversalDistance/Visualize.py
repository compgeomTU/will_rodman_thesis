from .FreeSpaceGraph import FreeSpaceGraph
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np 
import math
class Visualize(FreeSpaceGraph):

    def __init__(self, g1, g2, epsilon=1000, log=False, g1_color='mediumblue', g2_color='firebrick', fill_color='lightgreen'):
        super().__init__(g1, g2, epsilon, log)
        
        self.g1_color = g1_color
        self.g2_color = g2_color
        self.fill_color = fill_color

    @staticmethod
    def __calculate_cell_area(points):
        n, area = len(points), 0.0
        
        if n < 3: return 0.0

        for i in range(n):
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % n]
            area += (x1 * y2) - (x2 * y1)
            
        area = 0.5 * abs(area)
        return area

    def __build_graphs(self, ax, legend_fontsize):
        g1_n, g2_n = list(), list()

        for id, edge in self.g1.edges.items():
            n1_id, n2_id = edge[0], edge[1]
            n1, n2 = self.g1.nodes[n1_id], self.g1.nodes[n2_id]

            if n1 not in g1_n: g1_n.append(n1)
            if n2 not in g1_n: g1_n.append(n2)

            ax.plot([n1[0], n2[0]], [n1[1], n2[1]], color=self.g1_color, linewidth=1.5)

        lons, lats = map(list, zip(*g1_n))
        ax.scatter(lons, lats, s=15, c=self.g1_color)

        for id, edge in self.g2.edges.items():
            n1_id, n2_id = edge[0], edge[1]
            n1, n2 = self.g2.nodes[n1_id], self.g2.nodes[n2_id]
            
            if n1 not in g2_n: g2_n.append(n1)
            if n2 not in g2_n: g2_n.append(n2)
            
            ax.plot([n1[0], n2[0]], [n1[1], n2[1]], color=self.g2_color, linewidth=1.5)
            
        lons, lats = map(list, zip(*g2_n))
        ax.scatter(lons, lats, s=15, c=self.g2_color)
            
        g1_label = mpatches.Patch(color=self.g1_color, label=f"G1: {self.g1.name}")
        g2_label = mpatches.Patch(color=self.g2_color, label=f"G2: {self.g2.name}")

        ax.legend(handles=[g1_label, g2_label], loc='upper left', fontsize=legend_fontsize)
        ax.set_title(f"Epsilon: {self.epsilon}")

    def plot_graphs(self, legend_fontsize='medium'):
        fig, ax = plt.subplots()
        self.__build_graphs(ax, legend_fontsize)
        return fig, ax


    def plot_freespace(self, g1_ids=None, g2_ids=None, num=1, legend_fontsize='medium'):
        fig, ax = plt.subplots(1, 1, num=num)
        self.__build_graphs(ax, legend_fontsize)

        axs = plt.gca()
        axs.set_aspect('equal', 'datalim')

        if g1_ids is None and g1_ids is None:
            g1_edges, g2_edges = self.g1.edges, self.g2.edges
        else: 
            g1_edges = {id: self.g1.edges[id] for id in g1_ids}
            g2_edges = {id: self.g2.edges[id] for id in g2_ids}
        
        for g2_id, g2_edge in g2_edges.items():
            for g1_id, g1_edge in g1_edges.items():
                
                # horizonal lower CB
                cb_1 = self.get_cell_boundry(self.g2, g2_edge[0], self.g1, g1_id)

                # vertical right CB
                cb_2 = self.get_cell_boundry(self.g1, g1_edge[0], self.g2, g2_id)

                # horizonal upper CB
                cb_3 = self.get_cell_boundry(self.g2, g2_edge[1], self.g1, g1_id)

                # vetical left CB
                cb_4 = self.get_cell_boundry(self.g1, g1_edge[1], self.g2, g2_id)
                
                points = list()
                
                # collecting points from CB class
                if cb_1:
                    if cb_1.end_fs != -1.0: points.append((cb_1.end_fs, 0.0))
                    if cb_1.start_fs != -1.0: points.append((cb_1.start_fs, 0.0))

                if cb_2:
                    if cb_2.start_fs != -1.0: points.append((0.0, cb_2.start_fs))
                    if cb_2.end_fs != -1.0: points.append((0.0, cb_2.end_fs))

                if cb_3:
                    if cb_3.start_fs != -1.0: points.append((cb_3.start_fs, 1.0))
                    if cb_3.end_fs != -1.0: points.append((cb_3.end_fs, 1.0))

                if cb_4:
                    if cb_4.end_fs != -1.0: points.append((1.0, cb_4.end_fs))
                    if cb_4.start_fs != -1.0: points.append((1.0, cb_4.start_fs))
                    
                cell_area = self.__calculate_cell_area(points)

                # verify polygon (not line)
                if cell_area > 0:
                    g1_n1_id, g1_n2_id = g1_edge[0], g1_edge[1]
                    g1_n1_x, g1_n2_x = self.g1.nodes[g1_n1_id][0], self.g1.nodes[g1_n2_id][0]
                    g1_n1_y, g1_n2_y = self.g1.nodes[g1_n1_id][1], self.g1.nodes[g1_n2_id][1]

                    g2_n1_id, g2_n2_id = g2_edge[0], g2_edge[1]
                    g2_n1_x, g2_n2_x = self.g2.nodes[g2_n1_id][0], self.g2.nodes[g2_n2_id][0]
                    g2_n1_y, g2_n2_y = self.g2.nodes[g2_n1_id][1], self.g2.nodes[g2_n2_id][1]
                    
                    points = [(g1_n1_x, g1_n1_y),
                              (g1_n2_x, g1_n2_y),
                              (g2_n1_x, g2_n1_y),
                              (g2_n2_x, g2_n2_y)]

                    # sorting coords 
                    cent=(sum([p[0] for p in points])/len(points),sum([p[1] for p in points])/len(points))
                    points.sort(key=lambda p: math.atan2(p[1]-cent[1],p[0]-cent[0]))

                    xs, ys = list(zip(*points))  
                    axs.fill(xs, ys, alpha=cell_area, fc=self.fill_color, ec='none')
                    
        return fig, ax
