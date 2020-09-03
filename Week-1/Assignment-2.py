#!/usr/bin/env python
# coding: utf-8

# # <font color="blue">Question 1: </font>
# ## <font color="sky blue">Research on whether addition, subtraction, multiplication, division, floor division, and modulo operations be performed on complex numbers. Based on your study, implement a Python program to demonstrate these operations.</font>

# In[1]:


img1=complex(input("Enter 1st complex number: "))
img2=complex(input("Enter 2nd complex number: "))
print("\nAddition:",img1+img2)
print("Subtraction:",img1-img2)
print("Multiplication:",img1*img2)
print("Division:",img1/img2)
# print("Floor_Division:",img1//img2) """TypeError: can't take floor of complex number."""
# print("Modulo:",img1%img2) """TypeError: can't mod complex numbers."""


# # <font color="green">Question 2: </font>
# ## <font color="chartreuse">Research on range() functions and its parameters. Create a markdown cell and write in your own words (no copy-paste from google please) what you understand about it. Implement a small program of your choice on the same.</font>

# * Range function is in itself a python class created for the purpose of value set creation like in maps and generator class in python.
# 
# * Range prevents the explicit writing of list values, and generates required number patterns.
# 
# * Range provides an alternative to the 'for' loop to function like the while loop without declaration/initialization of new variables beforehand.
# 
# * It consists of 3 stages in itself, namely (start, stop, step), where default value of start and step are 0 and +1 respectively, and iteration takes place upto value of 'stop'-1.
# 
# * Besides the "start", "stop" and "step" parameters, count and index are other functions of range class.
# 
# The help() function shall provide a detailed analysis of implementation of range() and dir() will list all its magic methods.

# In[2]:


# help(range)
# print(dir(range),"\n\n")
list_1=list(range(0,10,2));
list_2=[x for x in range(0,10) if x%2==0]
print(list_1,type(list_1))
print(list_2,type(list_2))


# # <font color="maroon">Question 3: </font>
# ## <font color="red">Consider two numbers. Perform their subtraction and if the result of subtraction is greater than 25, print their multiplication result else print their division result.</font>

# In[3]:


a=float(input("Enter value of 'a': "))
b=float(input("Enter value of 'b': "))
print("\nValue of a={}\t|\tValue of b={}".format(a,b))
if (a-b>25):
    res=a*b
else:
    res=a/b
print("\nFinal Result is {}".format(res))


# # <font color="indigo">Question 4: </font>
# ## <font color="violet">Consider a list of 10 elements of integer values. If the number in the list is divisible by 2, print the result as "square of that number minus 2".</font>

# In[4]:


l1=[1,2,3,4,6,7,8,9,4,6]
print("Initially:",l1)
for num in l1:
    if(num%2==0):
        l1[l1.index(num)]=num**2-2 
print("After alteration:",l1)


# # <font color="Brown">Question 5: </font>
# ## <font color="Orange">Consider a list of 10 elements. Print all the elements in the list which are greater than 7 when that number is divided 2.</font>

# In[5]:


l2 = list(map(float, input("Enter 10 values: ").split()))
print("Required values:",end="  ")
for x in l2:
    if(x/2 > 7):
        print(x,end="  ")

