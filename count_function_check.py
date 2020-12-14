# This code is about
# generating random digit number of any length
# counting the occurence of a base in a sequence by 12 different ways,
# verifying our 12 counting function.


# function to generate random string
import random
def generate_string(N, alphabet='ACGT'):
    return ''.join([random.choice(alphabet) for i in range(N)])
    # below put in the number length that you want to generate
my_dna = generate_string(87050)


# Method--1.. List Iteration
def count_v1(dna, base):
    dna = list(dna) 
    i = 0             
    for c in dna:
        if c == base:
            i += 1
    return i
v1count = count_v1(my_dna,'A')
print('count_v1','=',v1count)


# Method--2.. String Iteration
def count_v2(dna, base):
    i = 0               #counter
    for c in dna:
        if c == base:
            i += 1
    return i
v2count = count_v2(my_dna,'A')
print('count_v2','=',v2count)


# Method--3.. Index Iteration
def count_v3(dna, base):
    i = 0 # counter
    for j in range(len(dna)):
        if dna[j] == base:
            i += 1
    return i
v3count = count_v3(my_dna,'A')
print('count_v3','=',v3count)


# Method--4.. While Loops
def count_v4(dna, base):
    i = 0 # counter
    j = 0 # string index
    while j < len(dna):
        if dna[j] == base:
            i += 1
        j += 1
    return i
v4count = count_v4(my_dna,'A')
print('count_v4','=',v4count)


# Method--5.. Using Boolean List
def count_v5(dna, base):
    m = []   # matches for base in dna: m[i]=True if dna[i]==base
    for c in dna:
        if c == base:
            m.append(True)
        else:
            m.append(False)
    return sum(m)
v5count = count_v5(my_dna,'A')
print('count_v5','=',v5count)


# Method--6.. Inline If Test
def count_v6(dna, base):
    m = []   # matches for base in dna: m[i]=True if dna[i]==base
    for c in dna:
        m.append(True if c == base else False)
    return sum(m)
v6count = count_v6(my_dna,'A')
print('count_v6','=',v6count)


# Method--7.. Using Boolean Values Directly
def count_v7(dna, base):
    m = []   # matches for base in dna: m[i]=True if dna[i]==base
    for c in dna:
        m.append(c == base)
    return sum(m)
v7count = count_v7(my_dna,'A')
print('count_v7','=',v7count)


# Method--8.. List Comprehensions of method--7
def count_v8(dna, base):
    m = [c == base for c in dna]
    return sum(m)
v8count = count_v8(my_dna,'A')
print('count_v8','=',v8count)


# Method--9.. Getting rid of m variable of method--8
def count_v9(dna, base):
    return sum([c == base for c in dna])
v9count = count_v9(my_dna,'A')
print('count_v9','=',v9count)


# Method--10.. Using Sum Iterator
def count_v10(dna, base):
    return sum(c == base for c in dna)
v10count = count_v10(my_dna,'A')
print('count_v10','=',v10count)


# Method--11.. Extracting Indices
def count_v11(dna, base):
    return len([i for i in range(len(dna)) if dna[i] == base])
v11count = count_v11(my_dna,'A')
print('count_v11','=',v11count)


# Method--12.. Using Python Library
def count_v12(dna, base):
    return dna.count(base)
v12count = count_v12(my_dna,'A')
print('count_v12','=',v12count)


# verifying the 12 functions
fun_list = (v1count,v2count,v3count,v4count,v5count,v6count,
            v7count,v8count,v9count,v10count,v11count,v12count)
for function in fun_list:
    if function == v12count:
        print('All function is correct')
    else:
        print('The function is incorrect')
    

