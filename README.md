# NLPFinal
Presentation Link: https://youtu.be/aOPqpGnejYM 


In this project I ran the Python module for Vosk. Vosk is an open source speech recognition toolkit. Vosk supports 18 natural languages and dialects, can be used offline and can be implemented in various programming languages (such as Python, Java, Node.JS, C#, C++ and others). 

I followed the installation and usage instructions found here: https://alphacephei.com/vosk/install   
Here are the steps when building on a mac:
< pip3 install vosk > (Note: up to date python and pip versions are needed)
Go to this repo, https://github.com/alphacep/vosk-api → python folder → example folder
I used test_ffmpeg because I had audio files I needed to convert 
I also ended up downloading ffmpeg separately (info here https://ffmpeg.org/), but I’m pretty sure this was unnecessary
Get test_ffmpeg file in local environment
Download model from https://alphacephei.com/vosk/models and unpack as ‘model’ in your current folder. (Note: I found that most of these did not download onto my computer vosk-model-en-us-daanzu-20200905-lgraph did, so that is the one I used. Supposedly there are newer and better ones, but they did not work for me)
To run use < python3 test_ffmpeg.py file.mp3>

For my code, I modified the test_ffmpeg code so I could process all of the mp3 audio files and then I printed to a new txt file
<  python3 my_test.py recordings > filename.txt > 

Important: If you’re running this for yourself I would strongly recommend doing a small sample instead of running the whole recordings folder. There are about 2100 files, and it took my computer around 8 or 10 hours.

To calculate metrics I have mer.py, wer.py and wil.py that use the JiWER package to calculate MER, WER and WIL. 

Here is the link to my dataset https://www.kaggle.com/rtatman/speech-accent-archive  
