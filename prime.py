# Write a Python program that takes a list of numbers and returns a new list 
# containing only the prime numbers from the original list.

def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

original_list = [54,25,63,31,53,57,69,85,88,91,2,4,5,1,0,3]
prime_list = filter_prime(original_list)

print("original list:",original_list)
print("prime no list:",prime_list)
# whyyyyyyyyyy