#had to process audio files in two batches, merging text files
filenames = ['filename.txt', 'extra_test_file.txt']

# Open new file in write mode
with open('allData.txt','w') as outfile:
    for names in filenames:
        # Open each file in read mode
        with open(names) as infile:
            outfile.write(infile.read())

        outfile.write("\n")

