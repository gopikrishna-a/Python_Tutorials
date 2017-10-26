def print_tree(num):
    cnt = 1
    inp = num
    for i in range(num,0,-1):
        print((" " * (i-1)) + ("#" * cnt))
        cnt += 2
        
print_tree(5)

"""
Out put:

    #
   ###
  #####
 #######
#########

"""
