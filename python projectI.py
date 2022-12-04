# import random
# print("                     MINI PROJECT - Group 21                       ")
# print("Here we have taken reference of cake as a whole value of 100 units.")
# print("This program will give you the cake when cut into peices in terms of angles and units.\n\n")
# n = int(input("Enter the number of peices of cake to cut into : "))

# print("\n")
# angle = 360     #The angle value is in degrees as a cake is a circle.

# #Case : 1
# #Cake into equal peices
# print("Case : 1")
# print()
# angle_1 = angle/n
# print("The cake will be cut at %.1f angle to get %d equal peices."%(angle_1, n),end=" ")
# print("i.e. %d peices of cake"%(angle_1/360*100))


# print()
# print()


# #Case : 2
# #Cake cut into N peices of any size

# print("Case : 2")
# print()
# l1 = []
# for i in range(1,n+1):
#         l1.append(random.randint(1,360))

# print("When cake is cut into N peices of any size")
# print()
# print("The cake is cut into different peices in terms of angle",end=" : ")
# a = sum(l1)
# for x in range(len(l1)):
#     l1[x] = (l1[x]/a)*360
#     l1[x] = round(l1[x],0)
# for i in range(len(l1)):
#     print(int(l1[i]),end=',')
# print()
# print()
# print("When cake is cutted in terms of percentage(%) and in reference of 100 units:",end=" ")
# for i in range(len(l1)):
#     print(round(int(l1[i])*100/360),end=',')


# print()
# print()
# print()


# #Case : 3
# print("Case : 3\n")
# print("When cake is cut into N peices and none of the peices are equal\n")
# for j in range(len(l1)):
#     if l1[j] not in l1:
#         l1[j] = (l1[j]/a) * 360
#         l1[j] = l1[j]




# print("When cake is cutted in terms of angle:",end=" ")
# for i in range(len(l1)):
#     print("%.0f"%(int(l1[i])),end=',')
# print("\n")



# print("When cake is cut in terms of percentage(%) and in reference of 100 units:",end=" ")
# for i in range(len(l1)):
#     print(round(int(l1[i])*100/360),end=',')


# print("\n\n\nSum of angles is",sum(l1))
