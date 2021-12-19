import json
import sys
#import numpy as np
import matplotlib.pyplot as plt

#file_to_sort = 'wer_scores.txt'
file_to_sort = sys.argv[1]

with open(file_to_sort, "r") as score:
    scores = score.read()
    score.close()

all_scores = json.loads(scores)

sort_orders = sorted(all_scores.items(), key=lambda x: x[1], reverse=True)

worst_100 = sort_orders[:100]
print(worst_100)


# labels = all_scores.keys()
# values = all_scores.values()
# plt.pie(values, labels=labels)
# plt.show()



# dict1 = json.loads(wer_scores)
# sorted_dict = {}
# sorted_keys = sorted(dict1, key=dict1.get)
#
# for w in sorted_keys:
#     sorted_dict[w] = dict1[w]
#
# print(sorted_dict)