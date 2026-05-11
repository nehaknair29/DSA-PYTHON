
def greet(name="User"):
    return f"Hello, {name}"
message=greet()
print(message)

def my_function(**kid):
    print("His last name is",kid["lname"])
my_function(fname="Arun",lname="Raj")    

