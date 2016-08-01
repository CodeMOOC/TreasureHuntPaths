
import csv


class FileUtils:

    @staticmethod
    def writePath(outfile, path, cost):

        with open(outfile, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
            writer.writerow(path + [cost])


