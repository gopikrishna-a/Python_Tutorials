
"""
input: 5
out put:

      #
     ###
    #####
   #######
  #########
      #
"""






def print_tree(num):
    cnt = 1
    ln = num + 1

    for i in range(1,num+1):
        print(' ' * ln + cnt * '#')
        cnt += 2
        ln -= 1

    print(((num+1) * " ") +'#')
    
    
num = int(input())
print(print_tree(num))
