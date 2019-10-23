#!/usr/bin/env python

import os

import networkx as nx

__author__ = "Alex Hoffman"
__copyright__ = "Copyright 2019, Alex Hoffman"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Alex Hoffman"
__email__ = "alex.hoffman@tum.de"
__status__ = "Beta"


class Grapher:
    """ A simple object to wrap a process tree generated by the energy debugger tool into a networkx A graph.
    """

    def __init__(self, process_tree, subdir):
        self.subdir = subdir
        self.pt = process_tree

    def draw_graph(self):
        a_graph = nx.nx_agraph.to_agraph(self.pt.graph)
        a_graph.graph_attr['splines'] = 'polyline'
        a_graph.graph_attr['packmode'] = 'node'
        a_graph.graph_attr['margin'] = 2

        file_path = "results/"

        if self.subdir:
            file_path += self.subdir + "/"

        a_graph.draw(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), file_path + self.pt.pidtracer.name) + ".xdot",
                     format='xdot', prog='dot')
