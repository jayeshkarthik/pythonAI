"""
COMS W4701 Artificial Intelligence - Homework 0

In this assignment you will implement a few simple functions reviewing
basic Python operations and data structures.

@author: JAYESH KARTHIK VELLORE SURESH (jv2666)
"""

# Input: Two individual lists, each with at least two elements
def manip_list(list1, list2):
    list_length1=len(list1)
    list_length2=len(list2)

    print(list1[list_length1-1])
    del list2[list_length2-1]
    print(list2)
    #print last element of list1

    #remove last element of list1
    list2[1]=list1[0]
    #print(list2)
    #change second element of list2 to be identical to first element of list1
    list3=[]
    for item in list1:
        list3.append(item)
    for item in list2:
        list3.append(item)
    print(list3)
    #print concatenation of list1 and list2 without modifying them
    final_list=[]
    final_list.append(list1)
    final_list.append(list2)
    return final_list
    #return single list consisting of list1 and list2 as its two elements


# Input: Two individual object parameters
def manip_tuple(obj1, obj2):
    #create a tuple of the two object parameters
    temp = (obj1,obj2)
    temp[0]="yeehaw"

    #attempt to modify the tuple by reassigning first item (should throw exception)

    return None


# Input: Two lists and one object
def manip_set(list1, list2, obj):
    #create a set called set1 using list1
    set1 = set(list1)

    #create a set called set2 using list2
    set2 = set(list2)

    #add obj to set1
    set1.add(obj)

    #test if obj is in set2 (print True or False)
    print(obj in set2)

    #print the union of set1 and set2
    set3 = set1|set2
    print("Union of set 1 and set 2 is:", set3)

    #print the intersection of set1 and set2
    set4 = set1 & set2
    print("Intersection of set 1 and set 2 is:", set4)

    #remove obj from set1
    set1.remove(obj)

    return None

# Input: Two tuples and one object
def manip_dict(tuple1, tuple2, obj):
    #create a dictionary such that elements of tuple1 serve as keys for elements of tuple2
    dictionary = {tuple1:tuple2}

    #print value of dictionary mapped by obj

    #delete dictionary pairing with obj key

    #print length of dictionary

    #add new pairing to dictionary mapping from obj to the value 0

    #return a list in which each element is a two-tuple of the dictionary's key-value pairings
    return None # replace this


if __name__ == "__main__":
    #Test case
    print(manip_list(["artificial", "intelligence", "rocks"], [4701, "is", "fun"]))

    try: manip_tuple("oh", "no")
    except TypeError: print("Can't modify a tuple!")

    manip_set(["sets", "have", "no", "duplicates"], ["sets", "operations", "are", "useful"], "yeah!")

    print(manip_dict(("list", "tuple", "set"), ("ordered, mutable", "ordered, immutable", "non-ordered, mutable"), "tuple"))