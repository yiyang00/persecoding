# PCTC Round 1 Demo 9

start = input()
dance = ['<', '+', '&', '>']
count = 0
dance_sequence = ""

if dance[0] == start:
  dance_sequence += dance[0]
  seq_count = 1
  count += 1 
elif dance[1] == start:
  dance_sequence += dance[1]
  seq_count = 2
  count += 1
elif dance[2] == start:
  dance_sequence += dance[2]
  seq_count = 3
  count += 1
else:
  dance_sequence += dance[3]
  seq_count = 4
  count += 1

while count < 8:
  if seq_count != 4:
    dance_sequence += dance[seq_count]
    seq_count += 1
    count += 1
  else:
    seq_count = 0 
    dance_sequence += dance[seq_count]
    seq_count += 1 
    count += 1

print(dance_sequence)
