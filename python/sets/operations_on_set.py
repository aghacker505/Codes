s = {29, 10.76, 'Abhay', 'jonny'}

#addding an element
#element i9s added at the random index in the set
s.add("sins")
print(s)

#removing an element
s.remove('Abhay')
print(s)

#updating set with list of multiple elements
#here also elements are adde at the random index in the set

s.update([29, 1, 4, 12])
print(s)

'''function of sets'''

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

#uninon of the elemnents of the sets
s3 = s1.union(s2)
print("union of sets", s3)

#intersection of the sets
s3= s1.intersection(s2)
print("intersection of the sets", s3)

#union of the sets
