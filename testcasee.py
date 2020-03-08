n = input()
for x in range(0,int(n)):
     input1= input()
     input2 = input()
     if input1 in input2 or "".join(reversed(input1)) in input2:
         print("YES")
     else:
         print("NO")