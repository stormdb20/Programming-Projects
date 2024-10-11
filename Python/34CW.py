
dict = {1:'50', 2:'yo', 3:'dictionary'}
print(dict)
print('========================')
for n in dict:
  print(dict[n])
  print('========================')
for x in dict:
  print(x)
  print('========================')
for x in dict.values():
  print(x)
  print('========================')
for x in dict.items():
  print(x)
  print('========================')
for x,y in dict.items():
  print(x,y)



 
a=int(input('Enter Number: '))
b=int(input('Enter Number: '))
c=str(input('Enter class: '))
d=str(input('Enter location: '))
dict={}
dict[a]=c
dict[b]=d
for n in dict.values():
  print(n)
  
 
a=int(input('Enter Number: '))
b=int(input('Enter Number: '))
c=str(input('Enter class: '))
d=str(input('Enter location: '))
dict={}
dict[a]=c
dict[b]=d
for n in dict.values():
  print(n)
  
for x,y in dict.items():
  print(x,y)

a=input('Enter Something:')
b=input('Enter Something:')
c=input('Enter Something:')
p= set()
p.add(a)
p.add(b)
p.add(c)
print(p)


