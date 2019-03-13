class Greeter():
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)


class WalmartGreeter(Greeter):
    def greet():
        print("Well, hello, my name is")


greeter = Greeter("Person") # greeter.name = "Person"
greeter2 = Greeter("Test")  # greeter2.name = "Test"

greeter.greet()
greeter2.greet()
