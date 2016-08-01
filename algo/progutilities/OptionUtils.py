
import getopt
import sys


class OptionUtils:

    @staticmethod
    def __printHelpThenExit():
        print("Script usage:")
        print("{0} [-i <inputfile>] [-o <outputfile>] [-c <runcount>]".format(sys.argv[0]))
        sys.exit(2)

    @staticmethod
    def getOptions( argv, options):

        try:
            opts, args = getopt.getopt(argv,"hi:o:c:",["inputfile=","outputfile=","runcount="])
        except getopt.GetoptError:
            OptionUtils.__printHelpThenExit()

        for opt, arg in opts:
            if opt == '-h':
                OptionUtils.__printHelpThenExit()
            elif opt in ("-i", "--inputfile"):
                options['inputfile'] = arg
            elif opt in ("-o", "--outputfile"):
                options['outputfile'] = arg
            elif opt in ("-c", "--runcount"):
                options['runcount'] = int(arg)

        return options