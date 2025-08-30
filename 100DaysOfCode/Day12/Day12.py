# Local and GLobal Scope
# local is when we have variables defined in a fucntuion, they are only seen by ither code within the same block of code
# global any variable not defined in a function, but are available to use inside and outside of functions

def is_prime(num):
    if num == 1:
        return False
    if num not in [2,3] and (num % 2 == 0 or num % 3 == 0):
        return False
    else:
        return True
    
num = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]

# for i in num:
#     print(is_prime(i))


#-----------------------------------------------------
# how to modify a global variable 

enemies = 1

def inc_enemies():
    global enemies # dont really want to do this, can be usefull, but dont throw them around, only use when we want to have some constant that never changes, the
    enemies += 1
    

inc_enemies()
print(enemies)