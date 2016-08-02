
from random import randint
import numpy as  np
from igraph import *

from progutilities.PathCostFinder import PathCostFinder
from progutilities.OptionUtils import OptionUtils
from progutilities.FileUtils import FileUtils


def main(argv):
    default_options = {'runcount'   : 1000,
               'inputfile'  : 'graph.csv',
               'outputfile' : 'out.csv',
               'metafile': 'meta.csv',
               'plotfile': 'plot.png'}


    options = OptionUtils.getOptions(argv, default_options)
    print (options)

    # load graph
    g = FileUtils.loadGraph(options['inputfile'], options['metafile'])

    # assign edge weights
    g.es["weight"] = [1 for e in g.es]

    # plot graph
    #FileUtils.plotGraph(options['plotfile'], g)

    # generate graph [REMOVE ME]
    #g = Graph.GRG(30, 0.5)
    #g.es["weight"] = [randint(1, 5) for e in g.es]

    # get vertexes list
    vts = [v.index for v in g.vs]

    # reset file state
    try:
        os.remove(options['outputfile'])
    except OSError:
        pass

    pcf = PathCostFinder()

    for i in range(options['runcount']):
        # generate random path
        np.random.shuffle(vts)

        #calculate the traversing cost
        cost = pcf.pathCost(g, vts)
        #print("total cost is {0}".format(cost))

        # log the entry
        FileUtils.writePath(options['outputfile'], vts, cost)



if __name__ == "__main__":
   main(sys.argv[1:])
