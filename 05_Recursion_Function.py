
def getFibonacci(position):
    """
    Fibonacci Series     
    0, 1, 1, 2, 3, 5, 8, 13......
    
    Example:
    position  = 6
    return = 8
    """
    if (position == 0): 
        return 0
    if (position == 1):
        return 1
    first = 0
    second = 1
    nextt = first + second
    for _ in range(2, position):
        first = second;
        second = nextt;
        nextt = first + second;
    return nextt
    
    
def getFibonacciRecursion(position):
    """
    Fibonacci Series     
    0, 1, 1, 2, 3, 5, 8, 13......
    
    Example:
    position  = 6
    return = 8
    """
    if position == 0 or position == 1:
        return position
    return getFibonacciRecursion(position - 1) + getFibonacciRecursion(position - 2)
    
position = int(input())

for i in range(position):
    #Note - Comment one of them
    print(getFibonacci(i), end=" ")
    # print(getFibonacciRecursion(i), end=" ")

