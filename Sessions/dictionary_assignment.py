# print(F'Hello World')
#
# var_num=1
# print(F"var_num=)

var_dict={'key1': 'value1', 'key2': 'value2', 'key4': 'value4', 'key5': 'value5', 'key6': {'key7': [{'key8': 'value8'}]}}
print(var_dict)
print(var_dict.get('key8'))
print(var_dict['key6']['key7'][0]['key8'])
#-------------------------------------------------------------------------

var_number=1
# print(f"var_number:{var_number}:{id(var_number)}")
# print(f"{var_number}{id(var_number)}")
#var_sting='test'
#print(f"{var_sting}")
print("{:20}".format(2))
#var_string='This is a test string\nThis is another string'
#print(f"{var_string}")
#print(var_string)
#print(var_string.split("\n"))
# print(var_string.count(' is'))
# print(var_string.title())
#print(var_string.capitalize())
#print(var_string[0:10:3])
#print(var_string[::-1])

#----------------------------------------------------------------------

    # 1) find the union from 3 sets
    # 2) find the difference from 3 sets
    # 3) find the maximum number from 5 variables
    # 4) take input from user and if input is 'a' then print 'apple' like wise create a to g


var_set_1 = {1, 2, 3, 4, 5, 6, 7, 8, 1, 1, 2, 2, 2, 2, 3}
var_set_2 = {1, 66, 33, 22, 8, 9}
var_set_3 ={1,6,7,8,9,10,11}


print(sorted(var_set_2.union(var_set_1).union(var_set_3)))
print(var_set_1.intersection(var_set_2).intersection(var_set_3))
print(var_set_2.difference(var_set_1).difference(var_set_3))

#---------------------------------------------------------------------------------

# n1=11
# n2=11
# n3=11
# n4=11
# n5=11
#
# if(n1>n2) and (n1 > n3) and (n1>n4) and(n1>n5) :
#     print("N1 is largest no")
#
# elif(n2>n3) and (n2>n4) and (n2>n5):
#     print("N2 is largest")
#
#
# elif(n3>n4) and (n3>n5):
#     print("N3 is largest")
#
#
# elif(n4>n5):
#     print("N4 is largest")
#
#
# elif(n1==n2==n3==n4==n5):
#     print("All no.s are same")
#
# else:
#     print("N5 is largest")

#------------------------------------------------------------------------------------------------------------
n=input("Enter value : ").lower()
#print(n)

if(n=='a'):
    print("Apple")

elif(n=='b'):
    print("Bat")

elif(n=='c'):
    print("Cat")

elif(n=='d'):
    print("Dog")

elif(n=='e'):
    print("Elephant")

elif(n=='f'):
    print("Fish")

elif(n=='g'):
    print("Goat")

else:
    print("Invalid input")

