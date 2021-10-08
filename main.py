#Use for, .split, and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
splitSt = st.split()
for word in splitSt:
    if word[0] == 's' or word[0]=='S':
        print(word)


#Use range() to print all the even numbers from 0 to 10
for i in range(0,11):
    if i%2 == 0:
        print(i)

#Use list comprehension to create a list of all numbers between 1 and 50 that are divisible by 3
newList = [num for num in range(0,51) if num%3==0]
print(newList)


#Go through the string below and if the length of a word is even print "even!"
st = "Print very word in this sentence that has an even number of letters"
splitSt2 = st.split()
for w in splitSt2:
    if len(w) % 2 == 0:
        print('"{}" is even!'.format(w))


#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the
#multiples  of five print "Buzz".  For numbers of both three and five print "FizzBuzz".
arr = []
for n in range(1,101):
    if n%3==0 and n%5==0:
        arr.append("FizzBuzz")
    elif n%3==0:
        arr.append("Fizz")
    elif n%5==0:
        arr.append("Buzz")
    else:
        arr.append(n)
print(arr)


#Use List Comprehension to create a list of the first letters of every word in the string below:
st="Create a list of the first letters of every word in this string"
newSt = st.split()
index = 0
for wd in newSt:
    newSt[newSt.index(wd)] = wd[0]
print(newSt)
