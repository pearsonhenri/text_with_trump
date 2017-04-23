import csv
from operator import itemgetter
import os
import sys

csv_dir = os.path.join(os.getcwd(), "data/wordcounts")

def read_data(wordcount_file):
    with open(os.path.join(csv_dir, wordcount_file)) as csv_in:
        reader = csv.DictReader(csv_in)
        first_line = reader.next()
        data = {first_line['word']:[first_line['count'], first_line['relative_use']]}
        for line in reader:
            data[line['word']]=[line['count'], float(line['relative_use'])]
        return data


def main():
    if (len(sys.argv) < 2):
        print "error: enter a word to inspect"
    word = sys.argv[1]
    word_users = []
    for wordcount_file in os.listdir(csv_dir):
        data = read_data(wordcount_file)
        if word in data.keys():
            president = os.path.splitext(wordcount_file)[0]
            word_users.append((president, data[word]))
    sorted_word_users = sorted(word_users, key=lambda user: user[1][1], reverse=True)
    for user in sorted_word_users:
        print user

main()
