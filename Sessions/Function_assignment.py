# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# def pattern(k,l):
#     for i in range(0,k):
#         for j in range(0,l):
#             print("*",end=" ")
#         print("")
#
# pattern(5,5)

#----------------------------------------------------------
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1

# def pattern(k,l):
#     for i in range(0,k):
#         for j in range(0,l):
#             print("1",end=" ")
#         print("")
#
# pattern(5,5)

#------------------------------------------------------------------
# 1
# 1 0
# 1 0 1
# 1 0 1 0
# 1 0 1 0 1

# def pattern(m,l):
#     for i in range(1,m):
#         for j in range(1,i+1):
#             k=0
#             k=j%2
#             print(k,end=" ")
#         print("")
#
# pattern(6,6)

#--------------------------------------------------------------------------------------------

# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

# def pattern(a,b):
#     for i in range(0,a):
#         for j in range(0,b):
#             print(j+1, end=" ")
#         print("")
#
# pattern(5,5)

#-------------------------------------------------------
# 0 0 0 0 0
# 1 1 1 1 1
# 0 0 0 0 0
# 1 1 1 1 1
# 0 0 0 0 0

# def pattern(a,b):
#     for i in range(0,a):
#         for j in range(0,b):
#             print(i%2,end=" ")
#         print("")
# pattern(5,5)

#--------------------------------------------------------

# 0
# 1 0
# 0 1 0
# 1 0 1 0
# 0 1 0 1 0

# def pattern(a,b):
#     for i in range(0, a):
#         for j in range(0, i + 1):
#             print((i+j)%2, end=' ')
#         print("")
#
# pattern(5,5)

#-------------------------------------------------------------------------
# 1 0 1 0 1
# 0 1 0 1
# 1 0 1
# 0 1
# 1

def pattern(a,b):
    for i in range(a, 0, -1):
        for j in range(0, i):
            print((i+j)%2, end=' ')
        print("")
pattern(5,5)

#--------------------------------------------------------------------

