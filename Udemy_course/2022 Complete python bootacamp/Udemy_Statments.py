st = 'Print only the words that start with s in this sentence'
st = st.split(" ")
for word in st:
    if word[0]=="s":
        print(word)


for number in range(0,10,2):
    print(number,end=" ")
print()

mylist = [x for x in range(1,50) if x%3==0]
print(mylist)

st = 'Print every word in this sentence that has an even number of letters'

for word in st.split(" "):
    if len(word)%2 ==0:
        print("Even",end=" ")


mylist = ["FizzBuzz" if x%3 ==0 and x%5==0 else "Buzz" if x % 5==0  else "Fizz" if x% 3 ==0 else x for x in range(1,100)]
print(mylist,end=" ")
print()
st = 'Create a list of the first letters of every word in this string'

mylist = [letter[0] for letter in st.split(" ")]
print(mylist,end=" ")