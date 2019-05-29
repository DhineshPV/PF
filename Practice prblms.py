#INFY_01
def addstring(str1):
    if(len(str1)>3):
        if str1.endswith ("ing"):
            str1=str1+"ly"
        else:
            str1=str1+"ing"
    return str1

str1=input()
print(addstring(str1))
        
  #INFY_03
  import ast
def create_new_dictionary(prices):
    n=ast.literal_eval(prices)
    new_dict={}
    for key,value in n.items():
        if value>200.0:
            new_dict[key]=value
    sorted_d=sorted(new_dict.items())
    return dict(sorted_d)

prices=input()
print(create_new_dictionary(prices))

#INFY_04
def find(num):
  #edit your code here
    for i in range(0,len(num)):
        if(num[i]==9 and i<4):
            return True
    return False    
num=list(map(int,input().split()))
print(find(num))

#INFY_05
def countdigits(s):
  #enter your code here
    l=[]
    c1=0
    c2=0
    for i in s:
        if i.isalpha():
            c1+=1
        elif i.isnumeric():           
            c2+=1
    l.append(c1)
    l.append(c2)
    return l
s=input()
print(countdigits(s))

#INFY_06
def check(l):
  #code here
    num=""
    for i in l:
        num=num+str(i)
    if "123" in num:
        return True
    else:
        return False
    
l=list(map(int,input().split()))
print(check(l))
