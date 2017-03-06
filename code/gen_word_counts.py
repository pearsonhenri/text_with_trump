from collections import Counter
import csv
import os
import re
import tempfile

corpus_dir = "/Users/phenri/personal-github/text_with_trump/corpora/speeches/raw/Corpus of Presidential Speeches/"
csv_dir = "/Users/phenri/personal-github/text_with_trump/corpora/speeches/wordcounts/"


def clean_speech_file_text(person, filename):
    with open(os.path.join(corpus_dir, person, filename), 'r') as speech_file:
        speech_lines = speech_file.readlines()
    matcher = re.compile("[<(][^)>]*[)>]|[(\.)+\",?!:;\d]")
    cleaned_speech_text = ""
    for line in speech_lines:
        if not (line.startswith("<title=") or line.startswith("<date")):
            cleaned_speech_text += re.sub(matcher, "", line).rstrip() + " "
    return cleaned_speech_text

for person in os.listdir(corpus_dir):
    speech_text = ""
    for raw_speech in os.listdir(os.path.join(corpus_dir, person)):
        if not (raw_speech.startswith(".DS_Store")):
            speech_text += " " + clean_speech_file_text(person, raw_speech)
    speech_words = speech_text.lower().split(" ")
    word_counts = Counter(speech_words)
    print person
    print word_counts.most_common(100)
    csv_name = person.lower() + ".csv"
    writefile = open(os.path.join(csv_dir, csv_name), 'wb')
    writer = csv.writer(writefile)
    for key, count in word_counts.iteritems():
        writer.writerow([key, count])
    writefile.close()

# remove first line, which counts nulls
for csv in os.listdir(csv_dir):
    tmp = tempfile.NamedTemporaryFile(mode='r+')
    with open(os.path.join(csv_dir, csv), 'r') as i:
        i.next()
        for line in i:
           tmp.write(line.rstrip()+"\n")
    tmp.seek(0)
    with open(os.path.join(csv_dir, csv), 'w') as o:
        for line in tmp:
            o.write(line)
