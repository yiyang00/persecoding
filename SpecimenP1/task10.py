# PCTC Round 1 Demo 10

milkshake_char = input()
I_count = 0
M_count = 0
C_count = 0
W_count = 0
for i in range(len(milkshake_char)):
  if milkshake_char[i] == "I":
    I_count += 1
  elif milkshake_char[i] == "M":
    M_count += 1
  elif milkshake_char[i] == "C":
    C_count += 1
  else:
    W_count += 1

missing = ""
if I_count != 2:
  more_I = 2 - I_count
  while more_I != 0:
    missing += "I"
    more_I -= 1
if M_count != 1:
  more_M = 1
  missing += "M"
if C_count != 3:
  more_C = 3 - C_count
  while more_C != 0:
    missing += "C"
    more_C -= 1
if W_count != 1:
  more_W = 1
  missing += "w"

print(missing)
