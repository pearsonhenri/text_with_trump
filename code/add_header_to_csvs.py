import os

csv_dir = os.path.join(os.getcwd(), "data/wordcounts")

header = 'word,count,relative_use'

for wordcount_file in os.listdir(csv_dir):
    with open(os.path.join(csv_dir, wordcount_file), 'r+') as csv_in:
        content = csv_in.read()
        csv_in.seek(0, 0)
        csv_in.write(header.rstrip('\r\n') + '\n' + content)
