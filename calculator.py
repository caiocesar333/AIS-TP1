 
CONTRIBUTORS = ["Bharat"] # Conflicts generator 1
 
def add(a, b):
    pass
 
def subtract(a, b):
    pass
 
def multiply(a, b):
    pass
 
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
 
if __name__ == "__main__":
    print(f"Welcome to the Group Calculator!, written by {CONTRIBUTORS}")
    print(divide(10,2)) # Conflicts generator 2