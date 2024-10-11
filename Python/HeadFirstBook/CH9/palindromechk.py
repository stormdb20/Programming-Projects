#My first program with only a little help on splitting a string!!!!!
palindrome='a nut for a jar of tuna'
def split(palindrome):
    return list(palindrome)
print(split(palindrome))
if palindrome[0] == palindrome[-1]:
    print("It's a drome alright!")
else:
    print('Aww shucks no drome')

    