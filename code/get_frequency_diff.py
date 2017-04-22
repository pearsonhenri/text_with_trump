import csv
from operator import itemgetter
import os
import sys

csv_dir = os.path.join(os.getcwd(), "data/wordcounts")

def read_data(pres):
    csv_name = pres + '.csv'
    with open(os.path.join(csv_dir, csv_name)) as csv_in:
        reader = csv.DictReader(csv_in)
        first_line = reader.next()
        data = {first_line['word']:[first_line['count'], first_line['relative_use']]}
        for line in reader:
            data[line['word']]=[line['count'], float(line['relative_use'])]
    return data


def get_diff(pres1, pres2):
    pres1_data = read_data(pres1)
    pres2_data = read_data(pres2)
    NUM_WORDS = 20
    diff_array = []
    for k in set(pres1_data.keys()):
      if k in set(pres2_data.keys()):
          diff_array.append((k, pres1_data[k][0], pres2_data[k][0], float(pres1_data[k][1]) / float(pres2_data[k][1])))
    diff_array = sorted(diff_array, key=itemgetter(3), reverse=True)
    print "\n\nTop " + str(NUM_WORDS) + " words that " + pres1 + " used more frequently than " + pres2 + ":\n"
    for i in range(0, NUM_WORDS):
        print diff_array[i][0] + "     wordcount: " + str(diff_array[i][1]) + "    frequency factor: " + str(diff_array[i][3])

def main():
    if (len(sys.argv) < 3):
        print "error: list two presidents to compare"
    pres1 = sys.argv[1]
    pres2 = sys.argv[2]
    get_diff(pres1, pres2)

main()
