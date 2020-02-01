from Fraction import Fraction

def main():
    print("Welcome to FracCalc by b0kch01!")
    print('Enter "quit" to leave')
    while (exp := input("Expression: ").lower()) != "quit":
        print(produce_answer(exp))
    print("\nBye!")

def produceAnswer(string):
    inputs = string.split("")
    operand = inputs[1]

    fraction1 = Fraction(inputs[0])
    fraction2 = Fraction(inputs[2])

    if (operand == "+"):
        fraction1.add(fraction2)
    else if (operand == "-"):
        fraction1.substract(fraction2)
    else if (operand == "*"):
        fraction1.multiply(fraction2)
    else:
        fraction.divide(fraction2)

    fraction1.reduceFraction()
    fraction1.toMixed()

    return fracion1.toString()