import csv
import fileinput
import os

csv_dir = "/Users/phenri/personal-github/text_with_trump/data/wordcounts/"

for wordcounts in os.listdir(csv_dir):
    with open(os.path.join(csv_dir, wordcounts), 'r') as f:
        total_words = 0
        total_individual_words = 0
        rows = list(csv.reader(f))
        for row in rows:
            total_words += int(row[1])
            total_individual_words += 1
    new_file = fileinput.input(os.path.join(csv_dir, wordcounts), inplace=True)
    for line in new_file:
        word_count = line.split(",")[1]
        print line.rstrip() + ',' + str(float(word_count)/total_words)
    new_file.close()
