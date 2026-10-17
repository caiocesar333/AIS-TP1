

CONTRIBUTORS = ["Rovshana", "caioc333", "Bharat", "Lilia"]

def add(a, b):
    return a + b
 
def subtract(a, b):
    return a - b
 
def multiply(a, b):
    return a * b
 
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
 
if __name__ == "__main__":
    print(f"Welcome to the Group Calculator!, written by {CONTRIBUTORS}")
    print(divide(10,2))
    print(subtract(4,2))
    print(add(2, 2))
    print(multiply(2, 2))
