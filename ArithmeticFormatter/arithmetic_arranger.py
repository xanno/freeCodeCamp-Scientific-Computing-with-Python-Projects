def arithmetic_arranger(problems, with_solution=False):
    """
    Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged
    vertically and side-by-side. The function should optionally take a second argument. When the second argument is set
    to True, the answers should be displayed.
    """
    eq_row1 = []
    eq_row2 = []
    eq_row3 = []
    eq_row4 = []

    """
    Situations that will return an error:
    * If there are too many problems supplied to the function. The limit is five, anything more will return: 
    Error: Too many problems.
    
    * The appropriate operators the function will accept are addition and subtraction. 
    Multiplication and division will return an error. Other operators not mentioned in this bullet point 
    will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.
    
    * Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers 
    must only contain digits.
    
    * Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error 
    string returned will be: Error: Numbers cannot be more than four digits.
    """
    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        equation = problem.split()

        if len(equation) < 3:
            return "Error: Numbers must only contain digits."
        if not equation[0].isdigit() or not equation[2].isdigit():
            return "Error: Numbers must only contain digits."
        if equation[1] != '+' and equation[1] != '-':
            return "Error: Operator must be '+' or '-'."
        if len(equation[2]) > 4 or len(equation[0]) > 4:
            return "Error: Numbers cannot be more than four digits."

        if equation[1] == "+":
            res = int(equation[0]) + int(equation[2])
        else:
            res = int(equation[0]) - int(equation[2])

        w_length = max(len(equation[0]), len(equation[2])) + 2

        eq_row1.append(equation[0].rjust(w_length))
        eq_row2.append(f"{equation[1]}{equation[2].rjust(w_length - 1)}")
        eq_row3.append("-" * w_length)
        eq_row4.append(str(res).rjust(w_length))

    if not with_solution:
        arranged_problems = "    ".join(eq_row1) + "\n" + "    ".join(eq_row2) \
                            + "\n" + "    ".join(eq_row3)
    else:
        arranged_problems = "    ".join(eq_row1) + "\n" + "    ".join(eq_row2) \
                            + "\n" + "    ".join(eq_row3) + "\n" + "    ".join(eq_row4)
    return "" if arranged_problems is None else arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))

