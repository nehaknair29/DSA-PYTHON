#sets

#empty set creation
my_set = set()
print(my_set)  # Output: set()

set={}
print(set)  # Output: {}
#for an empty set we have to use set() function, using {} will create an empty dictionary instead of a set. 

s1={1, 2, 3, 4, 5}
s2={4, 5, 6, 7, 8}

#joining sets
#union and update
#union rerurns a new set that contains all the elements from both set
#while update modifies the original set by adding elements from another set. 
union_set = s1.union(s2)
print(union_set)  # Output: {1, 2, 3,   4, 5, 6, 7, 8}      
s1.update(s2)
print(s1)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

#symmetric differemce and symmetric_difference_update
#symmetric difference returns a new set that contains elements that are in either of the sets but not in both.
#while symmetric_difference_update modifies the original set by keeping only the elements that are unique to each
symmetric_diff_set = s1.symmetric_difference(s2)
print(symmetric_diff_set)  # Output: {1, 2, 3} 
symmetric_diff_set = s1.symmetric_difference_update(s2)
print(s1)  # Output: {1, 2, 3}

#difference and difference_update
#difference returns a new set that contains elements that are in the first set but not in the second set.
#while difference_update modifies the original set by removing elements that are also present in the second set
difference_set = s1.difference(s2)
print(difference_set)  # Output: {1, 2, 3}
s1.difference_update(s2)
print(s1)  # Output: set()

#disjoint sets
#two sets are disjoint if they have no elements in common.
cities={"New York", "Los Angeles", "Chicago", "Houston", "Phoenix"}
countries={"USA", "Canada", "Mexico", "Brazil", "Argentina"}
print(cities.isdisjoint(countries))  # Output: True
print(cities.issuperset(countries))  # Output: False
print(countries.issuperset(cities))  # Output: False
c1={1, 2, 3,4,5,6,7,8}
c2={4, 5, 6, 7, 8}
print(c1.isdisjoint(c2))  # Output: False 
print(c1.issuperset(c2))  # Output: True 

#issubset
#A set A is a subset of set B if all elements of A are also present in B.
c1={1, 2, 3}
c2={1, 2, 3, 4, 5}
print(c1.issubset(c2))  # Output: True
print(c2.issubset(c1))  # Output: False 

#adding a sinlge element to a set
set1={"apple", "banana", "cherry"}
set1.add("orange")
print(set1)
#adding multiple elements to a set
set1.update(["grape", "kiwi", "melon"]) 
print(set1)
#remove() method removes a specific element from the set. 
# If the element is not found, it raises a KeyError.
set1.remove("banana")
print(set1)
#discard() method also removes a specific element from the set.
# However, if the element is not found, it does not raise an error and simply does nothing.
set1.discard("kiwi")
print(set1)
set1.discard("kiwi")  # No error, does nothing
#pop() method removes and returns an arbitrary element from the set. 
# If the set is empty, it raises a KeyError.
popped_element = set1.pop()
print(popped_element)
print(set1)
#clear() method removes all elements from the set, leaving it empty.
set1.clear()
print(set1)
