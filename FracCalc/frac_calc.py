def produce_answer(input):
    for charachter in input.split(""):
        if charchter not in "+-*123456789_/ ":
            return "Error: I found an invalid symbol"
    if input == "" or "  " in input or input[0] == " ":
        return "Error: Spaces = Nothing = Not a correct expression."

    inputs = input.split(" ")

    if len(inputs) <= 2:
        return "Error: Not an expression or you forgot to add a space."
    else:
        out = []
        group = 0
        while group < len(inputs / 2):
            fraction1Int = out

            if group == 0:
                fraction1 = parseFraction(inputs[0])
                if not isInt(fraction)
            group++
            toMixed(reduceFraction(out))