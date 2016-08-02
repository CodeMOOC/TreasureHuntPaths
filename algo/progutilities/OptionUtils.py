
import getopt
import sys


class OptionUtils:

    @staticmethod
    def __printHelpThenExit():
        print("Script usage:")
        print("{0} [-i <inputfile>] [-o <outputfile>] [-c <runcount>] [-m <metafile>] [-p <plotfile>]".format(sys.argv[0]))
        sys.exit(2)

    @staticmethod
    def getOptions( argv, options):

        try:
            opts, args = getopt.getopt(argv,"hi:o:c:m:p:",["inputfile=","outputfile=","runcount=", "metafile=", "plotfile="])
        except getopt.GetoptError:
            OptionUtils.__printHelpThenExit()

        for opt, arg in opts:
            if opt == '-h':
                OptionUtils.__printHelpThenExit()
            elif opt in ("-i", "--inputfile"):
                options['inputfile'] = arg
            elif opt in ("-o", "--outputfile"):
                options['outputfile'] = arg
            elif opt in ("-m", "--metafile"):
                options['metafile'] = arg
            elif opt in ("-p", "--plotfile"):
                options['plotfile'] = arg
            elif opt in ("-c", "--runcount"):
                options['runcount'] = int(arg)

        return options