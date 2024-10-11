def main():
  L=[]
  L.append(1)
  L.append(2)
  L.insert(0, 4)
  print(L)
  L.sort()
  print(L)
  L.reverse()
  print(L)
main()

def main_2():
  a=str(input('What is your name?'))
  b=int(input('Are you male or female?'))
  m=('Mr. ')
  f=('Mrs. ')
  if b =='male':
    print(m+a)
  else:
    print(f+a)
main_2()
