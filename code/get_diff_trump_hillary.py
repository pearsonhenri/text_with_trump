import csv
from operator import itemgetter
import os

csv_dir = "/Users/phenri/personal-github/text_with_trump/data/wordcounts/"


# read each csv into a dictionary
with open(os.path.join(csv_dir, 'trump.csv')) as csv_in:
    reader = csv.DictReader(csv_in)
    first_line = reader.next()
    trump_data = {first_line['word']:[first_line['count'], first_line['relative_use']]}
    for line in reader:
        trump_data[line['word']]=[line['count'], float(line['relative_use'])]

with open(os.path.join(csv_dir, 'hclinton.csv')) as csv_in:
    reader = csv.DictReader(csv_in)
    first_line = reader.next()
    hillary_data = {first_line['word']:[first_line['count'], first_line['relative_use']]}
    for line in reader:
        hillary_data[line['word']]=[line['count'], float(line['relative_use'])]

# trump_diff_array = []
# for k in set(trump_data.keys()):
#   if k in set(hillary_data.keys()):
#       trump_diff_array.append((k, trump_data[k][0], hillary_data[k][0], float(trump_data[k][1]) / float(hillary_data[k][1])))
# trump_diff_array = sorted(trump_diff_array, key=itemgetter(3), reverse=True)
# for i in range(0, 50):
#     print trump_diff_array[i][0] + "    frequency factor: " + str(trump_diff_array[i][3])

hillary_diff_array = []
for k in set(hillary_data.keys()):
  if k in set(trump_data.keys()):
      hillary_diff_array.append((k, hillary_data[k][0], trump_data[k][0], float(hillary_data[k][1]) / float(trump_data[k][1])))
hillary_diff_array = sorted(hillary_diff_array, key=itemgetter(3), reverse=True)
for i in range(0, 50):
    print hillary_diff_array[i][0] + "    frequency factor: " + str(hillary_diff_array[i][3])
