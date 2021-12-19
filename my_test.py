#My modified version of test_ffmpeg
#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer, SetLogLevel
import sys
import os
import wave
import subprocess
import json

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


SetLogLevel(0)

if not os.path.exists("model"):
    print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit (1)

sample_rate=16000
model = Model("model")
rec = KaldiRecognizer(model, sample_rate)
#print(sys.argv[0])
#sys.exit()

dir = sys.argv[1]

files = os.listdir(dir)
Dict = {}

#Trying to create a dictionary with keys being the name of the audio file and values are the transcriptions
print('{')
#Loop through each audio file
for file in files:

    eprint('Processing file '+file)
    #running the model
    process = subprocess.Popen(['ffmpeg', '-loglevel', 'quiet', '-i',
                                dir+'/'+file,
                                '-ar', str(sample_rate), '-ac', '1', '-f', 's16le', '-'],
                               stdout=subprocess.PIPE)
    while True:
        data = process.stdout.read(10000)
        if len(data) == 0:
            break
        try:
            rec.AcceptWaveform(data)
        except:
            eprint('Found error in '+file)

    try:
        value = json.loads(rec.FinalResult())['text']
    except:
        value = 'Error'
#creating output file in a dictionary format
    print("'"+file + "': '" + value + "',")

print('}')


exit ()

