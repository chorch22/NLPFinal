import os
import sys
import json
import jiwer

actual_file = sys.argv[1]
hypothesis_file = sys.argv[2]

#open the actual transcription file
with open(actual_file, "r") as actual:
    ground_truth = actual.read()
    actual.close()

#print(ground_truth)

#Open the files transcribed by model
with open(hypothesis_file, "r") as hypotheses:
    hypothesis_string = hypotheses.read()
    hypotheses.close()

all_hypotheses = json.loads(hypothesis_string)

print("{")
for key in all_hypotheses.keys():
    hypothesis = all_hypotheses[key]
    #print(text)
    measures = jiwer.compute_measures(ground_truth, hypothesis)
    wer = measures['wer']
    print('"'+key +'": "' + str(wer)+'",')

print("}")