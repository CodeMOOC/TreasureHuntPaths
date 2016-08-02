

import csv
from igraph import *


class FileUtils:

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
             vertex_color='#ff3300', background=None)