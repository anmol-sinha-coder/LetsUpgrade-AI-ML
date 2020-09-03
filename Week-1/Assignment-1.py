#!/usr/bin/env python
# coding: utf-8

# # <font color="blue">Question 1: </font>
# ## <font color="sky blue">Write a program to subtract two complex numbers in Python.</font>

# In[1]:


img1=complex(input("Enter 1st complex number: "))
img2=complex(input("Enter 2nd complex number: "))
print("\nSubtracting 2nd complex number from 1st complex number, we get",img1-img2)


# # <font color="green">Question 2: </font>
# ## <font color="chartreuse">Write a program to find the fourth root of a number.</font>

# In[2]:


num=float(input("Enter a real number: "))
print("\nFourth(4th) root of the number is",num**(1/4))


# # <font color="maroon">Question 3: </font>
# ## <font color="red">Write a program to swap two numbers in Python with the help of a temporary variable.</font>

# In[3]:


a=int(input("Enter value of 'a': "))
b=int(input("Enter value of 'b': "))
print("\nValue of a={}\t|\tValue of b={}".format(a,b))
t=a
a=b
b=t
print("\nAfter swap,\nValue of a={}\t|\tValue of b={}".format(a,b))


# # <font color="indigo">Question 4: </font>
# ## <font color="violet">Write a program to swap two numbers in Python without using a temporary variable.</font>

# In[4]:


a=int(input("Enter value of 'a': "))
b=int(input("Enter value of 'b': "))
print("\nValue of a={}\t|\tValue of b={}".format(a,b))
a=a+b
b=a-b
a=a-b
print("\nAfter swap,\nValue of a={}\t|\tValue of b={}".format(a,b))


# # <font color="Brown">Question 5: </font>
# ## <font color="Orange">Write a program to convert Fahrenheit to kelvin and celsius both.</font>

# In[5]:


fahr=float(input("Enter temperature in degrees Fahrenheit: "))
cels= 5/9*(fahr-32)
kelvin=cels+273.15
print("\nThe temperature in Kelvin is",round(kelvin,2))
print("The temperature in Celsius is",cels)


# # <font color="pink">Question 6: </font>
# ## <font color="gold">Write a program to demonstrate all the available data types in Python.</font>

# In[6]:


i=4
f=4.5
c=4+5j
b=True
word="Hello world"
l=[4,'five',6.7]
t=(4,"five",6.7)
s={4,'five',6.7}
d={"One":1, 2:'Two', 'Three':3}
print("\n\tDATA TYPES\nNumeric: ",type(i),type(f),type(c),"\nBoolean: ",type(b),"\nSequential:",type(word),type(l),type(t),"\nOther:",type(d),type(s),)

