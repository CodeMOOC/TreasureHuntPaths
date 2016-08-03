

import csv

import numpy
from igraph import *
import math


class FileUtils:

    @staticmethod
    def __distance(x1,x2, y1, y2):
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)


    @staticmethod
    def __calculateWeightsOnDistance(g):

        distance = [FileUtils.__distance(g.vs[e.source]['x'],
                                         g.vs[e.target]['x'],
                                         g.vs[e.source]['y'],
                                         g.vs[e.target]['y']) for e in g.es]

        freq, bins = numpy.histogram(distance, bins=4)
        g.es["weight"] = numpy.digitize(distance, bins)

        return g

    @staticmethod
    def loadGraph(inputfile, metafile):

        g = Graph.Read_Ncol(inputfile, directed=False)

        g.vs["label"] = [v.index + 1 for v in g.vs]

        columns = defaultdict(list)  # each value in each column is appended to a list

        with open(metafile) as f:
            reader = csv.DictReader(f)  # read rows into a dictionary format
            for row in reader:  # read a row as {column1: value1, column2: value2,...}
                for (k, v) in row.items():  # go over each column name and value
                    columns[k].append(float(v))  # append the value into the appropriate list
                    # based on column name k

        g.vs['y'] = list(map((lambda x: x * -1), columns['Lat']))
        g.vs['x'] = columns['Long']
        g.vs['treasure'] = [True if v > 0 else False for v in columns['Treasure']]

        g = FileUtils.__calculateWeightsOnDistance(g)

        return g

    @staticmethod
    def writePath(outfile, path, cost):

        with open(outfile, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
            writer.writerow(path + [cost])



    @staticmethod
    def plotGraph(plotfile, graph):

        coords = zip(graph.vs['x'], graph.vs['y'])

        # layout = g1.layout("kk")
        plot(graph, "../plots/coords-graph-plot.png", layout=coords, bbox=(403, 832), vertex_size=22,
             vertex_color='#ff3300', background=None) #, edge_width=graph.es['weight']