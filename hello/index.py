# largest_so_far = -1

# for i in [1,41,3,8,74,15]:
#     if i > largest_so_far:
#         largest_so_far = i
#         print (largest_so_far, i)
    
# print("After", largest_so_far)


# Counting 
# work = 0
# print('Before', work)
# for thing in  [9,42,12,3,74,15]:
#     work = work + 1
#     print(work , thing)
# print('After' ,work)


# count = 0
# sum = 0 
# print('Before', count , sum)
# for value in [9, 41, 12, 3, 74, 15]:
#     count = count + 1
#     sum = sum + value
#     print(count, sum, value)
# print('After', count , sum, sum/count)

# filtering in a loop
# print ('Before')
# for value in [3,41,13,3,74,15]:
#     if value > 20:
#         print('larger number',value)
# print('After')

# //searching











# strings
# str = 'IamwhoIamsaystheLord'
# print(len(str))

# fruit = 'banana'

# index = 0 
# while index < len(fruit):
#     letter = fruit[index]
#     print(letter)
#     index = index + 1

# strin = 'Monty Python'
# print(strin[0 : 5])
# print(strin[ : ])
# print(strin[ : 2])

# print ('word'< 'word')
# xfile = open('inbox.txt')
# for cheese in xfile:
#     print(cheese)

# fhand = open('inbox.txt')
# inp = fhand.read()
# print(len(inp))

# print((inp[:20]))




# fhand = open('inbox.txt')
# for line in fhand:
#     line = line.rstrip()
#     if line.startswith('f'):
#         print(line)

#list
friends = ['Joseph', 'Glenn', 'Sally']


# for i in range(len(friends)):
#     friend = friends[i]
#     print('Happy New Year', friend)

# # Concatenation
# a = [1, 2, 3]
# b = [4, 5, 6]
# print(a + b)

# t = [9,41, 12, 3, 74, 15]
# friends.sort()
# print(friends)

# abc = 'with         three words'
# stuff = abc.split()
# print (stuff)

# python dictionaries
# counts = dict()
# names = ['csev', 'cwen', 'zqian', 'cwen']

# for name in names:
#     counts[name] = counts.get(name, 0) + 1
# print(counts)


counts = dict()
print('Enter a line of text: ')
line = input('')
words  = line.split()
print('words :', words)
print('Counting...')
for word in words:
    counts [ word ] = counts.get(word, 0) + 1
print('Counts', counts)




























