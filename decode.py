import numpy as np
import matplotlib.pyplot as plt
import IPython.display as ipd
import soundfile as sf
from scipy.signal import butter, filtfilt

audio, Fe = sf.read('mess_difficile.wav')
print('Fe =',Fe,'Hz')
print('Le message est composé de', len(audio), 'points. Soit', len(audio)/2500, 'caractères.')

plt.figure(figsize=(10, 4))
plt.plot(audio)

precision=8 #on va concatener notre symbole de 2000 points avec 8000 fois 2 puissance la précision (moins 2000) zéros. Cela correspond à une présion de l'ordre 1/M

alphabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
frequences = [501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526] 

def decode(audio):
    message = ''
    while len(audio)>499:
        x=audio[:2000]
        if np.all(int(x)==0):
            message+=' '
        else:
            new_x = np.concatenate((x, np.zeros(8000*(2**precision)-len(x))))
            new_hanning = np.concatenate((np.hanning(len(x)), np.zeros(8000*(2**precision)-len(x))))
            X = np.fft.fft(new_x*new_hanning)
            borneinf = 501*(2**precision)
            bornesup = 526*(2**precision)+1
            max = np.argmax(np.abs(X[borneinf:bornesup]))/(2**precision)
            freq = np.round(max+501)
            #print('La fréquence dominante est', max+501, 'Hz')
            #print('La fréquence dominante est', freq, 'Hz')
            if (500<=freq<=526):
                index = frequences.index(int(freq))
                print('Lettre :', alphabet[index])
                message+=alphabet[index]
        audio=audio[2500:]
    return message

print(decode(audio))