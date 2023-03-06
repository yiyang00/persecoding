# PCTC Round 1 Demo 9

start = input()
dance = ['<', '+', '&', '>']
count = 0
dance_sequence = ""
sequence = 0

for i in range(len(dance)):
  if dance[i] == start:
    sequence = i

while count < 8:
  if sequence != 4:
    dance_sequence += dance[sequence]
    sequence += 1
    count += 1
  else:
    sequence = 0 
    dance_sequence += dance[sequence]
    sequence += 1 
    count += 1

print(dance_sequence)
