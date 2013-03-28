import re
str = "123 ,,,  123 , 3,123"

newstr = re.sub(',{1,}',',',str)
print(newstr)
newstr = re.sub(' {1,}','',newstr)
print(newstr)
arr = re.split(',',newstr)

print(arr)