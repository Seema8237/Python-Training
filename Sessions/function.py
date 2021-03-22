#function without arguments and return

# def greetings():
#     print("Hello world")
#
# greetings()

#----------------------------------------------------------

#function with arguments and without return
# def greetings(name,message='Hello'):
#     print(F"{message} {name}")

#greetings("{message} {name}")

# greetings(name='Pavan', message='Hi')
#
# greetings(name='Pavan')

#--------------------------------------------------------
#function with return and without argument

# def greetings():
#     var=1
#     return "Hello",var
# print(greetings())

#---------------------------------------------------------

#function with arguments and return
# def greetings(name, message="Hello"):
#     return F"{message} {name}"
#
#
# print(greetings(name='Jimmy', message='Bye'))
# print(greetings(name='Jimmy'))

#---------------------------------------------------------------
#function with function as argument
# print(type(greetings()))
# message, name = greetings()
#
# print(name, type(name))
# print(message, type(message))

#--------------------------------------
#function returns function


#--------------------------------------
#* args

# def greetings(*args):
#     if len(args) >= 2:
#         return F"{args[0]} {args[1]} {args[2]}"
#     elif len(args) == 1:
#         return f"Hello {args[0]}"
#     else:
#         return "Hi Jimmy"

#print(greetings())
#print(greetings(*['Jimmy']))
#print(greetings(*['Bye', 'Jimmy']))
#print(greetings(*['why', 'Jimmy', '?']))

#--------------------------------------------------------
def greetings(**kwargs):
    return F"{kwargs.get('message', 'Hi')} {kwargs.get('name', 'Jimmy')} {kwargs.get('garbage', '')}"


print(greetings())
print(greetings(**{'name': 'Jimmy'}))
print(greetings(**{'message': 'Bye', 'name': 'Jimmy'}))
print(greetings(**{'message': 'why', 'name': 'Jimmy', 'garbage': '?'}))






