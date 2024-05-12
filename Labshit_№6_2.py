from math import *
from matplotlib.pyplot import *

text = open("Shield Hero.txt", 'r', encoding='utf-8').read().replace('\n', '')
alph, prob, dim = [], [], []

#   Creating an alphabet

for i in range(len(text)):
    if text[i] not in alph:
        alph.append(text[i])
alph = sorted(alph)

#   Message probability and proprietary information

for i in range(len(alph)):
    prob.append(round(text.count(alph[i])/len(text)*100, 4))
    dim.append(round(-log(text.count(alph[i])/len(text), 2), 3))

#   Entropy calculation

H = 0
Hm = log(len(alph), 2)
for i in range(len(alph)):
    H -= text.count(alph[i])/len(text) * log(text.count(alph[i])/len(text), 2)

#   Redundancy calculation

R = Hm - H
r = 1 - (H / Hm)

#   Output

print(f'Minimum dimension:')
for i in range(len(alph)):
    if dim[i] == min(dim):
        print(f'{alph[i]}: {dim[i]} bit')

print(f'Maximum dimension:')
for i in range(len(alph)):
    if dim[i] == max(dim):
        print(f'{alph[i]}: {dim[i]} bit')
     
print(f'Entropy max: {round(Hm, 2)} | Real entropy: {round(H, 3)}\nAbsolute red: {round(R, 3)} | Relative red: {round(r, 3)}')

#   Graph

bar(alph, prob, width=0.4, color = 'red')
grid()
show()