szelso = (min,max)
t = [2,5,6,9,10,12,4]
maxElem = t[0]
for elem in t:
    if elem > maxElem:
        maxElem = elem
print(maxElem)

minElem = t[0]
for elem in t:
    if elem < minElem:
        minElem = elem
print(minElem)
