class Test:
    def __init__(self, a, b, string):
        self.a = a
        self.b = b
        self.string = string

    def operations(self):
        op = self.string.lower()

        if op == "add" or op == "+":
            return self.a + self.b
        elif op == "sub" or op == "-":
            return self.a - self.b
        elif op == "mul" or op == "*":
            return self.a * self.b
        elif op == "div" or op == "/":
            if self.b == 0:
                return "Error: Division by zero!"
            return self.a / self.b
        else:
            return "Invalid operation!"

a = float(input("Enter your a value: "))
b = float(input("Enter your b value: "))
string = input("Enter your operation (add/sub/mul/div): ")

result = Test(a, b, string)

print("Result:", result.operations())