def anagram(x,y):
  b = sorted(x):
  c = sorted(y):
  return c== b
lst1 = eval(input())
lst2 = eval(input())
c = 0
for i in lst1:
  for j in lst2:
    if anagram(i,j):
      c+=1
print(c)      
      
