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

exit()
#wer_file = "wer-" + target_pred + ".txt"

# Calculate WER for the whole corpus
# wer_score = wer(refs, preds, standardize=True)    # "standardize" expands abbreviations
# print("WER Score:", wer_score)

    #json.loads(sys.argv[1]).keys()
#
# def eprint(*args, **kwargs):
#     print(*args, file=sys.stderr, **kwargs)
#
# print('{')
# for key in keys:
#     eprint('the key is ' + key)
#     transformation = jiwer.Compose([
#         jiwer.ToLowerCase(),
#         jiwer.RemoveWhiteSpace(replace_by_space=True),
#         jiwer.RemoveMultipleSpaces(),
#         jiwer.ReduceToListOfListOfWords(word_delimiter=" ")
#     ])
#
#     jiwer.wer(
#         key,
#         hypothesis,
#         truth_transform=transformation,
#         hypothesis_transform=transformation
#     )
#
#     measures = jiwer.compute_measures(key, hypothesis)
#     wer = measures['wer']
#     #mer = measures['mer']
#     #wil = measures['wil']
#     #cer = measures['cer']
#
#     print("'"+key + "': '" + wer+"'")
#
# print('}')


