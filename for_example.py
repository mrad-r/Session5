# Sessions 7 and 8

for i in range(1, 10):
    print(i)

# range() is a function that gives elements from the left and side to the right hand side. The first element is included
# However, the last element is not included.
# Therefore, in this specific case, 1 would be included while 10 is not.

range(1, 10, 2) # This includes all numbers from 1 to 10 except 10 and 2

s = 0
for i in range(1,11):
    s += i
# The above expression is equivalent to s = s + i
print(s)

# The main difference between FOR and WHILE is that FOR is used for a know number of iterations.
# WHILE is used for an unknown number of iterations.
# Moreover, WHILE can always be used instead of FOR. WHILE can do everything that FOR can.
# The opposite is not true.

i = 1
s = 0
while i <= 10:
    s += i  # This means that as long as i <= 10, s is going to increase by i
    i += 1  # This means that i is always going to increase by one unit each time. This will break the loop.
print("The sum of the first 10 numbers is ", s)

# When there is no break point, the code never stops running since it enters an infinite loop
# In the previous case, i += 1 breaks the loop since it will stop when i = 10 (i increases each iteration until 10)









