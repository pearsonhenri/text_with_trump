import os
import re

corpus_dir = """/Users/phenri/Documents/pearsonal/text_with_trump_playground/corpi/speeches/raw/Clinton-Trump Corpus/Clinton/"""
cleaned_corpus_dir = """/Users/phenri/Documents/pearsonal/text_with_trump_playground/corpi/speeches/clean/Clinton-Trump Corpus/Clinton/"""


def clean_speech_file_text(filename):
    with open(corpus_dir + filename, 'r') as speech_file:
        speech_lines = speech_file.readlines()
    cleaned_speech_text = ""
    for line in speech_lines:
        if not (line.startswith("<title=") or line.startswith("<date")
                or not line.startswith("<CLINTON:>")):
            cleaned_speech_text += re.sub("[<(][^)>]*[)>]", "", line)

    return cleaned_speech_text


def write_cleaned_speech_file(filename, cleaned_speech_text):
    with open(cleaned_corpus_dir + filename, "w") as cleaned_speech_file:
        cleaned_speech_file.write(cleaned_speech_text)


for raw_speech in os.listdir(corpus_dir):
    if not (raw_speech.startswith(".DS_Store")):
        write_cleaned_speech_file(raw_speech, clean_speech_file_text(raw_speech))
