def Anagrams( li ):
  dictionary = {}
  for word in li:
    sortedWord = ''.join(sorted(word))
    if sortedWord not in dictionary:
      dictionary[sortedWord] = [word]
    else:
      dictionary[sortedWord] += [word]
  return [dictionary[i] for i in dictionary]

li =[]
r=int(input("Range : "))
for i in range (r):
  i=input("Enter : ")
  li.append(i)
print(Anagrams(li))
