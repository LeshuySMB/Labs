line = input().split()

ostring = ''

for i in range(len(line)):
  ostring += line[i]

string = ostring[::-1]
if (string==ostring):
  print("Это полиндром")
else:
  print("Не полиндром")
