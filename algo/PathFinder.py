
from random import randint
import numpy as  np
from igraph import *

from progutilities.PathCostFinder import PathCostFinder
from progutilities.OptionUtils import OptionUtils
from progutilities.FileUtils import FileUtils




def main(argv):
    default_options = {'runcount'   : 1000,
               'inputfile'  : 'graph.csv',
               'outputfile' : 'out.csv'}
    

    options = OptionUtils.getOptions(argv, default_options)
    print (options)

    # generate graph [REMOVE ME]
    g = Graph.GRG(30, 0.5)
    g.es["weight"] = [randint(1, 5) for e in g.es]

    # get vertexes list
    vts = [v.index for v in g.vs]

    # reset file state
    os.remove(options['outputfile'])

    pcf = PathCostFinder()

    for i in range(options['runcount']):
        # generate random path
        np.random.shuffle(vts)

        #calculate the traversing cost
        cost = pcf.pathCost(g, vts)
        print("total cost is {0}".format(cost))

        # log the entry
        FileUtils.writePath(options['outputfile'], vts, cost)



if __name__ == "__main__":
   main(sys.argv[1:])
