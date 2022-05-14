import csv

with open("data.csv",newline= "") as f:
    read = csv.reader(f)
    file_data=list(read)
    
print(file_data)
data=file_data[0]
print(data)

# finding mean
def calculate_mean(data):
    n =len(data)
    total = 0
    for i in data:
        total += int(i)
    m= total/n
    return m

squaredlist = []
for i in data :
    a = int(i)-calculate_mean(data)
    a = a**2
    squaredlist.append(a)
    
    
sum = 0
for i in squaredlist:
    sum += i
    
result = sum/(len(data) - 1)

import math
std_dev = math.sqrt(result)

print(f"the standard derivation of data is : {std_dev}")

import statistics
d = [60,61,65,63,98,99,90,95,91,96]
#s  = statistics.stdev(d)
#print(s)
print(f"the standard derivation of data is : {statistics.stdev(d)}")