
#0"{:02}".format(x)
#
# 05
# 04
# 03

#ctrl+alt+shift+select

# 01 02 03 04 05
# 05 04 03 02 01
# 02 04 06 08 10
# 10 08 06 04 02
# 03 06 09 12 15
# 15 12 09 06 03


# for i in range(1,4):
#     for j in range(1,6):
#         print("{:02}".format(i*j),end=" ")
#     print("")
#
#     for j in range(5, 0,-1):
#         print("{:02}".format(i * j), end=" ")
#     print("")

#------------------------------------------------------------------------------------

# x = '01'
# x = '02'+ x
# '02 01'

# for i in range(1,4):
#     reverse = ""
#     for j in range(1,6):
#         no = "{:02}".format(i*j)
#         print(no, end=' ')
#         reverse = F"{no} {reverse}"
#     print("")
#     print(reverse)

#-----------------------------------------------------------------------------------

#     1
#    1 1
#   1 1 1
#  1 1 1 1
# 1 1 1 1 1

# space=' '
# no_of_rows=5
# for i in range(0,no_of_rows):
#     print(space*(no_of_rows-i),end=' ')
#     for j in range(0,i+1):
#         print("1", end=' ')
#     print("")

#----------------------------------------------------------------------------

# for i in range(0,26):
#     print(chr(97+i))

#------------------------------------------------------------------------
