n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Part A

print(n, n[:])   #print the same number 1 1
print(n[0], n[-10])
print(n[9], n[-1])
print(n[3:])
print(n[:5])
print(n[-5:-1])
print(n[4:8])   #[5,6,7,8] starts at 5 to position 8-1 which is 8


#Part B

print(n[-1] + n[-2])  #10+9=19
print(n[9] - n[1])
print(n[2] * n[5])
print(n[8] / n[2])
print(len(n), n[:len(n)], sep = '\n')
print(min(n), max(n), type(n), sep = '\t')

#Part C

n.append(-11)
n.append("orange")
n[0], n[1] = n[-1], n[-2]
print(n+n)
print(n*2)  #repeats the list n two times, producing the same result as (n + n)


#Part D

item1 = n.pop(0)
print(f"{item1} is removed.")
item2 = n.pop()
print(f"{item2} is removed.")
print('n = ', n)
print(f'Removed items: {item1} & {item2}')  #removed item is 1 & 10

#Part E

n.insert(6, 'pear') #inserts 'pear' at index 6 in the list n, the list will be n = [2, 3, 4, 5, 6, 7, 'pear', 8, 9]
del n[0]
print(n)
n.remove("pear")
n.remove(6)
print('n = ', n)
n.clear()  #clears the list, making it an empty list []
print(f'n = {n}')


#Part F

fruits = ['kiwi', 'pear', 'orange', 'apple', 'cherry']
fruits.sort()  #After sorting the fruits list alphabetically, it will fruits = ['apple', 'cherry', 'kiwi', 'orange', 'pear']
print(fruits[0], fruits[-1])    #prints the first and last elements, so the output is: apple, pear
fruits.sort(reverse=True)
print(fruits[0], fruits[-1])


#Part G

fruits = ['kiwi', 'pear', 'orange', 'apple', 'cherry']
print(sorted(fruits)) #After sorting it will give a list same as Part F.
print(fruits[0], fruits[-1])
print(sorted(fruits, reverse=True))  #In reverse alphabetical order will be = ['pear', 'orange', 'kiwi', 'cherry', 'apple'] 
print(fruits[0], fruits[-1])




