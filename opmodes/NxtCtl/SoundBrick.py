import nxt
note_str = "la la# lb lc lc# ld ld# le lf lf# lg lg# a a# b c c# d d# e f f# g g# ha ha#"
note_arr = note_str.split(" ")
note_freq = {}
def getFreqFunc(x):
    return 220.0*(2.0**(1.0/12.0))**x
for num in range(len(note_arr)):
    note_freq[note_arr[num]] = getFreqFunc(num)



FREQ_E = 659
FREQ_C = 440
play_notes = []

import csv
import time
def csvToSong(filename):
    #batch is a 2d list that contains a list for each note [[le,2,0],[lf#,1,0]]
    f = filename#open(input('Enter file to open') + '.csv','r')
    c = csv.reader(open(f+".csv","r"))
    batch = []
    for row in c:
        batch.append(row)
    return batch
    #    print(row)

def playSound(b,batch,tempo):
    #tempo is a BPM number for the song
    #batch is a 2d list that contains a list for each note [[le,2,0],[lf#,1,0]]
    #f = open(input('Enter file to open') + '.csv','r')
    #c = csv.reader(f)
    #batch = []
    #for row in c:
    #    batch.append(row)
    #    print(row)
    raw = []
    for item in batch:
        raw.append([note_freq[item[0]],item[1],item[2]])
    print(raw)
    #tempo = 120#int(input('What tempo do you want to play this as in BPM'))
    cor_tempo = (1000/(tempo/60))/4
    #print('Milliseconds per semi-quaver is:' + str(cor_tempo))
    for item in raw:
        #print(item)
        b.play_tone_and_wait(int(item[0]), int(item[1]) * int(cor_tempo))
        time.sleep(float(item[2]) * cor_tempo/1000)

#SoundBrick.playSound(csvToSong("victory"),120)
