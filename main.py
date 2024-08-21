#memoziation - storing the computed values
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n<=1:
        return n 
    memo[n] = fibonacci(n-1,memo) + fibonacci(n-2,memo)
    return memo[n]

memory = {}
number = 10
print(f"The fibonacci series till {number} is")
for i in range(number):
     print(fibonacci(i, memory) , end="  ")



#time complexity: 0(n) - linear
