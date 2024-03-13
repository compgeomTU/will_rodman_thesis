# Author:
#   Will Rodman - Tulane University
#   wrodman@tulane.edu
#
# -----------------------------------------------------------------------------
#
# Source Repository:
#   GitHub.com compgeomTU/mapmatching GraphByCurve.py
#

import pkg_resources
pkg_resources.require("matplotlib==3.0.3")

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from shapely.ops import unary_union
import numpy as np
import time, logging
from matplotlib.patches import Polygon

from Curve import Curve
from Cells import Cells, Cells2D
from FreeSpace import FreeSpace
from NodeDistribution import curve_node_distribution


class FreeSpaceDiagram:
    __C2: Curve
    __C1: Curve
    
    __sigma_C1: Curve
    __sigma_C2: Curve
    
    
    __cells: Cells2D
    __freespace: FreeSpace

    def __init__(self, C1, C2, n_approximation=None):
        self.__C1, self.__C2 = C1, C2
        
        if n_approximation == None:
            self.__sigma_C1, self.__sigma_C2 = C1, C2
        else:
            self.__sigma_C1 = curve_node_distribution(C1, n_approximation)
            self.__sigma_C2 = curve_node_distribution(C2, n_approximation)
            
    # no. of cells = no. of G edges x no. of C edges
    def buildCells(self):
        self.__cells = Cells2D(self.__C1, self.__C2)

    # no of CBs in FreeSpace class = no. of cells * 4
    def buildFreeSpace(self, epsilon):
        self.__freespace = FreeSpace(self.__sigma_C1, self.__sigma_C2, epsilon=epsilon)
        
    def plotFreeSpace(self):
        fig, ax = plt.subplots()

        for ids, cell in self.__cells.cells.items():
            vertices = [(cell.x_proj[0], cell.y_proj[0]), 
                        (cell.x_proj[0], cell.y_proj[1]),
                        (cell.x_proj[1], cell.y_proj[1]),
                        (cell.x_proj[1], cell.y_proj[0])]
            
            cell = Polygon(vertices, closed=True, edgecolor='black', facecolor='darkgrey')
            ax.add_patch(cell)

        self.__freespace.build_cell_boundaries_2D()

        for cell_cb in self.__freespace.cell_boundaries_2D:
            vertices = list(zip(cell_cb[0], cell_cb[1]))
            
            poly_cell = Polygon(vertices, closed=True, edgecolor='white', facecolor='white', alpha=1.0)

            ax.add_patch(poly_cell)
            
        ax.set_xlim([0, self.__C1.vertex_dists[-1]])
        ax.set_ylim([0, self.__C2.vertex_dists[-1]])
        
        return fig, ax

