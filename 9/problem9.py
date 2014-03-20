import time
tic = time.time()

#a = b = c = a_temp = b_temp = c_temp = 1

#while a_temp + b_temp + c_temp <= 1000:
#    while a_temp + b_temp + c_temp <= 1000:
#        while a_temp + b_temp + c_temp <= 1000:
#            if a_temp**2 + b_temp**2 == c_temp**2:
#                if a_temp + b_temp + c_temp == 1000:
#                    print a_temp,b_temp,c_temp
#                    break
#            a_temp += 1
#        a_temp = 1    
#        b_temp += 1
#    b_temp = 1
#h    c_temp += 1
    
    
toc = time.time()
print 'The result took ' + str(toc - tic) + ' seconds to compute'

# I got this from http://snippets.dzone.com/posts/show/753
def all_perms(perm_list):
    if len(perm_list) <=1:
        yield perm_list
    else:
        for perm in all_perms(perm_list[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + perm_list[0:1] + perm[i:]

