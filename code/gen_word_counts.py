from collections import Counter
import csv
import os
import re
import tempfile

corpus_dir = os.path.join(os.getcwd(), "data/speeches/raw/Corpus of Presidential Speeches/")
csv_dir = os.path.join(os.getcwd(), "data/speeches/wordcounts")


def clean_speech_file_text(person, filename):
    with open(os.path.join(corpus_dir, person, filename), 'r') as speech_file:
        speech_lines = speech_file.readlines()
    matcher = re.compile("[<(][^)>]*[)>]|[(\.)+\",?!:;\d]")
    cleaned_speech_text = ""
    for line in speech_lines:
        if not (line.startswith("<title=") or line.startswith("<date")):
            cleaned_speech_text += re.sub(matcher, "", line).rstrip() + " "
    return cleaned_speech_text


def get_counts():
    for person in os.listdir(corpus_dir):
        speech_text = ""
        for raw_speech in os.listdir(os.path.join(corpus_dir, person)):
            if not (raw_speech.startswith(".DS_Store")):
                speech_text += " " + clean_speech_file_text(person, raw_speech)
        speech_words = speech_text.lower().split(" ")
        word_counts = Counter(speech_words)
        csv_name = person.lower() + ".csv"
        writefile = open(os.path.join(csv_dir, csv_name), 'wb')
        writer = csv.writer(writefile)
        for key, count in word_counts.iteritems():
            writer.writerow([key, count])
        writefile.close()


def remove_null_count():
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


def add_frequency_to_csvs():
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


def add_header():
    header = 'word,count,relative_use'
    for wordcount_file in os.listdir(csv_dir):
        with open(os.path.join(csv_dir, wordcount_file), 'r+') as csv_in:
            content = csv_in.read()
            csv_in.seek(0, 0)
            csv_in.write(header.rstrip('\r\n') + '\n' + content)

def main():
    get_counts()
    remove_null_count()
    add_frequency_to_csvs()


main()
