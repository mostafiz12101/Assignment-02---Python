#!/usr/bin/env python
# coding: utf-8

# # 1. Take values of the length & breadth of a rectangle from user input and check if it is square or not.

# In[2]:


values_of_the_length = int(input("Enter your length: "))
values_of_the_breadth = int(input("Enter your breadth: "))
if values_of_the_length == values_of_the_breadth:
    print("it is square ")
else:
    print("it is not square ")


# # 2. Take three integer values from the user and print the greatest among them.

# In[3]:


a = int(input("Enter your first value: "))
b = int(input( "Enter your second value: "))
c = int(input("Enter your third value: "))

if a >b and a >c:
    print("a is the  greatest number")
elif b>a and b>c:
    print(" b is the greatest number")
else:
    print("c is the greatest number")


# # 3. A student will not be allowed to sit in an exam if his/her attendance is less than 75%.

# In[2]:


a=int(input("Enter your attendance day : " ))
if a>= 75:
    print("Allowed to sit in an exam")
else:
    print(" Don't allowed to sit in an exam")


# # 4. A school has the following rules for the grading system:
# Below 25 – F, 25 to 44 – E, 45 to 49 – D, 50 to 59 – C, 60 to 79 – B, 80 to 89 - A, Above 90 - A+
# Now, Ask the user to enter marks and print the corresponding grade.

# In[12]:


marks = int(input("Enter your number: "))
if marks>=  90 :
    print("A+")
elif marks  >= 80 and marks <= 90:
    print("A")
elif marks >= 60 and marks <= 79:
    print("B")
elif marks >=  50 and marks <= 59:
    print("C")
elif marks >=  45 and marks  <= 49:
    print("D")
elif marks >= 25 and marks <= 44:
    print("E")
else:
    print("F")


# # 5. Print the following pattern using for and while loop.
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6
# 1 2 3 4 5
# 1 2 3 4

# In[12]:


a=7
while a>=4:
    print()
    b=1
    while b<=a:
        print(b, end=" ")
        b=b+1
    a=a-1


# # 6. Display numbers from -100 to -10 using for loop.

# In[14]:


for a in range(100,9,-1):
    print(a)


# # 7. Write a program to sum all prime numbers within a range of 10 to 1000.

# In[15]:


sum=0
for a in range(10,1000):
    sum=sum+a
print(sum)


# # 8. Find the factorial of an n! (Hint, n=7: 7*6*5*4*3*2*1).

# # 9. Reverse a given integer number 27956240710.

# In[16]:


a= [2,7,6,2,4,0,7,1,0]
a.reverse()
print(a)


# # 10. Print the following pattern using for and while loop.
# 
# # # #
# # # # #
# # # #
# # #

# In[ ]:





# # 11. Display the Fibonacci series of 15 elements using the for and while loop.

# In[ ]:





# # 12. Remove 2 and add 3 to the list and replace True with False.
# Li = [1,3,5, [2,3], True]
# Output = [1,3,5, [3,3], False]

# In[3]:


a=[1,3,5,[2,3],True]
a[-1]=[False]
a[-2]=[3,3]
print(a)


# # 13. Find the intersection (common) of two sets.
# S1 = {1,4,6,8}
# S2 = {True, 1,2,10}

# In[ ]:





# # 14. Input a list from the user then Remove duplicates from a list and create a set and find the max
# number. User_input = [1,9,3,4,5,200,54]

# In[ ]:





# # 15. Rename the key of a dictionary.
# Dict = { "name": "Shakil", "age":27, "city": “Berlin”, "country": "Germany" }
# Write a program to rename a key ‘country’ to a ‘region’ in the following dictionary.

# In[ ]:





# # 16. Creating a data frame using the list.
# num = [10,100,300] (column name is number)

# In[ ]:





# # 17. Change the value of a key in a given dictionary.
# Write a Python program to change ‘age’ to 28 in the following dictionary.
# Dict = { "name": "Shakil", "age":27, "city": “Berlin”, "country": "Germany" }

# In[ ]:




