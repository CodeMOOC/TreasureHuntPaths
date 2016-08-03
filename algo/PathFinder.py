
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

    # plot graph
    FileUtils.plotGraph(options['plotfile'], g)



    # reset file state
    try:
        os.remove(options['outputfile'])
    except OSError:
        pass

    # get vertexes list
    vts = [v.index for v in g.vs if v['treasure']]

    #actual_vts = [64,65,66,69,82,79,107,135,133,111,116,119,124,152,130,131,149,145,141,156,162,161,163,38,31,25,2,1,11,13,15,18,52,50,44,96,101,102,139,99,98] #cost 246

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
