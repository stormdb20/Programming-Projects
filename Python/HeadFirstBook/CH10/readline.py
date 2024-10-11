
my_file=open('lib.txt', 'r')

while True:
    line=my_file.readline()
    if line != '':
        print(line)
    else:
        break
my_file.close()
