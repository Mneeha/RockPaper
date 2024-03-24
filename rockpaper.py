
import random
# p>r p<s r>s, r<p s<r s>p
r =  '\U0001F9F1'
p =  '\U0001F4C3'
s =  '\u2702'
print(r,p,s)
choices = [r,p,s]
computer = random.choice(choices)
x = str(input('press your item:  '))    
if x == str("r"):
     x = r
elif x == str("p"):
     x = p
elif x == str("s"):
     x = s
 #game
for i in range(3):         
 if x == computer:
  print('Computer=',computer,'you=',x)
  print("its a tie")
  break
 elif x== str(p) and computer== r:
  print('Computer=',computer,'you=',p)
  print('you won')
  break
 elif x== str(s) and computer== p:
   print('Computer=',computer,'you=',s)
   print('you won')
   break
 elif x== str(r) and computer== s:
   print('Computer=',computer,'you=',r)
   print('you won')
   break
 else:
  print('Computer=',computer, 'you=',x)
  print('you failed, try again')
  break