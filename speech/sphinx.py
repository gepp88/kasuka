#!/usr/bin/env python
import sys

try:
import pocketsphinx
except:
import pocketsphinx

# the hmdir,lmdirn and dictd variables hold the path of HMM,LM,dictionary of pocketsphinx
if __name__ == "__main__":
hmdir = "/usr/share/pocketsphinx/model/hmm/en_US/hub4wsj_sc_8k"
lmdir = "/usr/share/pocketsphinx/model/lm/en_US/hub4.5000.DMP"
dictd = "/usr/share/pocketsphinx/model/lm/en_US/cmu07a.dic"a

#Receiving wave file name from command line argument
wavfile = sys.argv[1]

speechRec = pocketsphinx.Decoder(hmm = hmdir, lm = lmdir,
dict = dictd)
wavFile = file(wavfile,'rb')
speechRec.decode_raw(wavFile)
result = speechRec.get_hyp()
print "\n\n\nDetected text:>",result
print "\n\n\n"
