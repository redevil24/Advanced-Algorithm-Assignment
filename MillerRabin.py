import random
import time

# a^k mod n
def modPower(a,k,n):
    a = a % n
    res = 1 
    while(k>0):
        if(k&1):
            res = res * a % n
        a = a * a % n
        k >>= 1
    return res

# n-1 = 2^s.d -> (s,d)
def Decompose(n):
    s = 0
    d = n - 1
    while (d % 2 == 0):
        d = int(d/2)
        s += 1
    return (s,d)


def Witness(a, n):
    s,d = Decompose(n)
    x = modPower(a,d,n)   
    
    # (1)              
    if x == 1: return True
    # print("s,d,a,x=",s,d,a,x)

    # (2)
    for i in range(1,s+1):
        # Compute y ~ x^2 (mod n)
        y = x * x % n             
        # print("loop i:",i,"-> y,x=",y,x)     
        if y == 1:           # i is the smallest: a^{2^i.d} = 1 (mod n) 
            if x == n-1:        # a^{2^(i-1).d} = -1 (mod n)
                return True
            else: 
                return False
        x = y
            
    return False



def MillerRabin(n, k):
    # Check n is small prime
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    if n < 11: 
        return False

    # Check n is even
    if n % 2 == 0: return False
    
    # Repeat Witness() with a random base 
    for i in range(k):
        # Pick a random number in [2..n-2] 
        a = random.randint(2, n - 2)
        if not Witness(a,n):
            return False
    
    return True


if __name__ == "__main__":

    start_time = time.perf_counter()

    # lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    # Pick n and choose k
    Test_Number = 15485863
    repeatTime = 5

    # Execute Miller-Rabin 
    if MillerRabin(Test_Number,repeatTime): 
        print("Prime")
    else: print("Composite")

    # Compute calculation time
    end_time = time.perf_counter()
    exec_time = (end_time - start_time)*10**3
    print(f"Execution time: {exec_time:.3f}ms")


