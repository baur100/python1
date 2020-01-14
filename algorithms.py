import random

# word1 = "night"
# word2 = "thing"
#
# def is_anagram(w1,w2):
#     if len(w1)!=len(w2):
#         return False
#     list1=sorted(w1)
#     list2 = sorted(w2)
#     for i in range(len(w1)):
#         if list1[i] != list2[i]:
#             return False
#     return True
#
#
# print(is_anagram(word1,word2))

number_of_dices = 3

def get_smallest_number_of_steps(number):
    list_dices = []
    for x in range(number):
        list_dices.append(random.randint(1,6))

    print(list_dices)
    count = [0,0,0,0,0,0]
    for x in range(1,7):
        for y in range(number):
            if x==list_dices[y]:
                count[x-1]=count[x-1]
            elif (x==1 and list_dices[y]==6) or \
                    (x==6 and list_dices[y]==1) or \
                    (x==2 and list_dices[y]==5) or \
                    (x==5 and list_dices[y]==2) or \
                    (x==3 and list_dices[y]==4) or \
                    (x==4 and list_dices[y]==3):
                count[x-1]+=2
            else:
                count[x-1]+=1
    print(count)

get_smallest_number_of_steps(number_of_dices)


# def is_prime(x):
#     for y in range(2,x-1):
#         if not x % y  :
#             return False
#     return True
# #
# #
# def prime_in_range(min,max):
#     for x in range(min,max):
#         if is_prime(x):
#             print(x)
#
#
# prime_in_range(1800,1900)
#

# a=5
# b=10
# a,b=b,a
# print(a)
# print(b)















