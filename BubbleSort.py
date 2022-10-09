def bubbleSort(numere):
  for i in range(len(numere)):
    for j in range(0, len(numere) - i - 1):
      if numere[j] > numere[j + 1]:
        aux = numere[j]
        numere[j] = numere[j+1]
        numere[j+1] = aux


v = [-6, 32, 0, 12, -3, 20.5]

bubbleSort(v)

print('Elementele vectorului in ordine crescatoare:')
print(v)
