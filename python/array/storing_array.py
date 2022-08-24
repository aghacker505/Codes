'''
A python program to storing student's marks into an array and finding total marks and percentage of marks 
'''

from array import *

name = input("Enter the name of the student: ")

#first we input the marks of the students in the list
lst = [int(i) for i in input('Enter marks of the student: ').split(',')]

#creating an integer array from the list
marks = array('i', lst)

#display marks and total marks
sum=0
for x in marks:
    print(x)
    sum+=x
print('Total marks of the',name,':', sum)

#display percentage
n = len(marks)
# print(n)
percent = (sum/n)
print('Percent of the',name,':', percent,'%')