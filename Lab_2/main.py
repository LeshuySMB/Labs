import math

xy = []

n = int(input("Введите количество точек: "))

def length(a,b):
  return(math.sqrt(((a[0]-a[1])**2)+(b[0]-b[1])**2))

xy = [[float(j) for j in input().split()] for i in range(n)]

p = -1

for ia in range(n-2):
  for ib in range(ia+1, n-1):
    for ic in range(ib+1, n):
      ab = length(xy[ia],xy[ib])
      bc = length(xy[ib],xy[ic])
      ac = length(xy[ia],xy[ic])

      if(ab+bc+ac)>p:
        p = ab+bc+ac
        a = xy[ia]
        b = xy[ib]
        c = xy[ic]

print("Координаты А: ", a)
print("Координаты B: ", b)
print("Координаты C: ", c)
