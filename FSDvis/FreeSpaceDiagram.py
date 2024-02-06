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

from Curve import Curve
from Cells import Cells
from FreeSpace import FreeSpace

class FreeSpaceDiagram:
    __C2: Curve
    __C1: Curve
    __cells: Cells
    __freespace: FreeSpace

    def __init__(self, C1, C2):
        self.__C1, self.__C2 = C1, C2

        logging.info("--------------- Graph Structure ---------------")
        for id, edge in self.__C1.edges.items():
            n1_id, n2_id = edge[0], edge[1]
            n1, n2 = self.__C1.nodes[n1_id], self.__C1.nodes[n2_id]
            logging.info(f"   E: {id}   V1: {n1_id} -> {n1}   V2: {n2_id} -> {n2}")

        logging.info("--------------- Curve Structure ---------------")
        for id, edge in self.__C2.edges.items():
            n1_id, n2_id = edge[0], edge[1]
            n1, n2 = self.__C2.nodes[n1_id], self.__C2.nodes[n2_id]
            logging.info(f"   E: {id}   V1: {n1_id} -> {n1}   V2: {n2_id} -> {n2}")

    # no. of cells = no. of G edges x no. of C edges
    def buildCells(self):
        self.__cells = Cells(self.__C1, self.__C2)

    # no of CBs in FreeSpace class = no. of cells * 4
    def buildFreeSpace(self, epsilon):
        self.__freespace = FreeSpace(self.__C1, self.__C2, epsilon=epsilon)

    def calculateArea(self):
        self.__freespace.calculateArea()
        return self.__freespace.free_space_area

    def plotFreeSpace(self, figue_filename=None):
        ax = plt.gca(projection = '3d')
        ax.grid(False)
        ax._axis3don = False

        for ids, cell in self.__cells.cells.items():
            ax.plot_surface(cell.x_proj, cell.y_proj, cell.z_proj, alpha=0.25, color='lightgray', edgecolor ='black')

        self.__freespace.build_cell_boundaries_3D()

        for cell_cb in self.__freespace.cell_boundaries_3D:
            verticies = [list(zip(cell_cb[0], cell_cb[1], cell_cb[2]))]
            poly_cell = Poly3DCollection(verticies, alpha=1.0, facecolor='dimgray')
            ax.add_collection3d(poly_cell)

        if figue_filename is None:
            plt.show()
        else:
            plt.savefig(figue_filename, format='svg')

