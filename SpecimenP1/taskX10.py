# PCTC Round 1 Demo 10

milkshake_char = input()
I_requirement = 2
M_requirement = 1
C_requirement = 3
W_requirement = 1
missing = ""

for i in range(len(milkshake_char)):
  if milkshake_char[i] == "I":
    I_requirement -= 1
  elif milkshake_char[i] == "M":
    M_requirement -= 1
  elif milkshake_char[i] == "C":
    C_requirement -= 1
  else:
    W_requirement -= 1

if I_requirement != 0:
  print("I")
elif M_requirement != 0:
  print("M")
elif C_requirement != 0:
  print("C")
else:
  print("W")
