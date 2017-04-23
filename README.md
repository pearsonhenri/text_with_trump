# text_with_trump
Playground for textual data exploration

## What's in this repository
* A number of [transcripts](https://github.com/pearsonhenri/text_with_trump/tree/master/data/speeches/raw) from presidential speeches, as well as Hillary Clinton and Donald Trump's 2016 campaign speeches [(source)](http://www.thegrammarlab.com/?nor-portfolio=corpus-of-presidential-speeches-cops-and-a-clintontrump-corpus)
* [CSV files](https://github.com/pearsonhenri/text_with_trump/tree/master/data/wordcounts) for each politician containing the word count and frequency for every word used
* A [script](https://github.com/pearsonhenri/text_with_trump/blob/master/code/get_frequency_diff.py) that calculates the difference in word usage frequency for any two politicians with output that looks like this:

```
$ python code/get_frequency_diff.py trump hclinton


Top 20 words that trump used more frequently than hclinton:

hillary     wordcount: 1459    frequency factor: 94.7915044251
illegal     wordcount: 240    frequency factor: 62.3713805675
politicians     wordcount: 216    frequency factor: 56.1342425108
clinton     wordcount: 1142    frequency factor: 49.4639698667
trillion     wordcount: 136    frequency factor: 35.3437823216
border     wordcount: 250    frequency factor: 32.4850940455
badly     wordcount: 116    frequency factor: 30.1461672743
radical     wordcount: 114    frequency factor: 29.6264057695
unbelievable     wordcount: 193    frequency factor: 25.0784926031
mosul     wordcount: 95    frequency factor: 24.6886714746
incredible     wordcount: 259    frequency factor: 22.4363716209
guys     wordcount: 86    frequency factor: 22.3497447033
hispanic     wordcount: 85    frequency factor: 22.0898639509
tremendous     wordcount: 248    frequency factor: 21.4834755288
destroyed     wordcount: 80    frequency factor: 20.7904601892
islamic     wordcount: 79    frequency factor: 20.5305794367
cases     wordcount: 78    frequency factor: 20.2706986845
judgment     wordcount: 71    frequency factor: 18.4515334179
total     wordcount: 142    frequency factor: 18.4515334178
justices     wordcount: 66    frequency factor: 17.1521296561
```

* A [script] that determines the most frequent users of a word
