#strings to demonstrate strip
hello= '!?are you ther?!'
goodbye= '?fine be that !way?!!'
#strip the characters from the beginning and the ending of the string
hello=hello.strip('!?')
goodbye=goodbye.strip('!?')

print(hello)
print(goodbye)