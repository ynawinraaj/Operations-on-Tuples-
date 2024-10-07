# empty tuple
my_tuple = ()
print(my_tuple)

# tuple with integers
my_tuple=(1,2,4,7,9,90,2435)
print(my_tuple)

# tuple with mixed datatype
my_tuple=("good morning",25,4.5670)
print(my_tuple)

# nested tuple
my_tuple=("codingal",[345678,45678,5678],(1000,2000,100000,200000))
print(my_tuple)

# exes tuple elements using indexing
my_tuple=('c','o','d','i','n','g','a','l')
print(my_tuple[0])
print(my_tuple[5])

# nested tuple
my_tuple=("codingal",[345678,45678,5678],(1000,2000,100000,200000))
print(my_tuple[0][3])
print(my_tuple[1][1])
print("sliced: ",my_tuple[1:4])

# iterating tuple
for letter in (my_tuple):
    print("hello",letter)