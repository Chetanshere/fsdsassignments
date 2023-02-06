#!/usr/bin/env python
# coding: utf-8

# 1) Write a Python program to check if the given number is a Disarium Number?

# In[1]:


def calculateLength(n):    
    length = 0;    
    while(n != 0):    
        length = length + 1;    
        n = n//10;    
    return length;    
     
num= 89;    
rem = sum = 0;    
len = calculateLength(num);    
      
n= num;

while(num > 0):    
        rem = num%10;    
        sum = sum + int(rem**len);    
        num = num//10;    
        len = len - 1;    
    
if(sum == n):    
    print(str(n) + " is a Disarium number");    
else:    
    print(str(n) + " is not a Disarium number");    


# 2) Write a Python program to print all disarium numbers between 1 to 100?

# In[3]:


def calculateLength(n):    
    length = 0;    
    while(n != 0):                    
        length = length + 1;    
        n = n//10;    
    return length;    
     
def sumdigit(num):    
    rem = sum = 0;    
    len = calculateLength(num);     
        
    while(num > 0):    
        rem = num;   
        sum = sum + (rem**len);    
        num = num//10;    
        len = len - 1;    
    return sum;    
      
result = 0;    
     

print("Disarium numbers between 1 and 100 are");    
for i in range(1, 101):           
    result = sumdigit(i);    
        
    if(result == i):    
        print(i),   


# 3) Write a Python program to check if the given number is Happy Number?

# In[6]:


def IsHappyNumber(num):    
    rem = sum = 0;    
        
    while(num > 0):    
        rem = num%10;    
        sum = sum + (rem*rem);    
        num = num//10;    
    return sum;    
        
num = 32;    
result = num;    
     
while(result != 1 and result != 4):    
    result = IsHappyNumber(result);    
       
if(result == 1):    
    print(str(num) + " is a happy number");    
    
elif(result == 4):    
    print(str(num) + " is not a happy number") 


# 4) Write a Python program to print all happy numbers between 1 and 100?

# In[7]:


def isHappyNumber(num):    
    rem = sum = 0;    
           
    while(num > 0):    
        rem = num%10;    
        sum = sum + (rem*rem);    
        num = num//10;    
    return sum;    
             
print("List of happy numbers between 1 and 100: ");    
for i in range(1, 101):    
    result = i;    
         
    while(result != 1 and result != 4):    
        result = isHappyNumber(result);    
        
    if(result == 1):    
        print(i),    
        print(" ")    


# 5) Write a Python program to determine whether the given number is a Harshad Number?

# In[19]:


def check_harshad(number):
      remainder = 0
      digit_sum = 0
      check = False
      n = number
      while(n > 0):
        remainder = n % 10
        digit_sum = digit_sum + remainder
        n = n//10
      if number % digit_sum == 0:
        check = True
      return check
lower = int(input("ENTER LOWEST NUMBER : "))
upper = int(input("ENTER HIGHEST NUMBER : "))
print("HARSHAD NUMBERS WITHIN RANGE({},{}) ARE -".format(lower,upper))
for i in range(lower,upper+1):
  if check_harshad(i):
    print(i,end = " ")


# 6) Write a Python program to print all pronic numbers between 1 and 100?

# In[21]:


def IsPronicNumber(num):    
    flag = False;    
        
    for j in range(1, num+1):    
        if((j*(j+1)) == num):    
            flag = True;    
            break;    
    return flag;    
     
print("Pronic numbers between 1 and 100: ");    
for i in range(1, 101):    
    if(IsPronicNumber(i)):    
        print(i),    
        print(" ")   


# In[ ]:




