def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    top_line_parts = []
    bottom_line_parts = []
    dash_line_parts = []
    result_line_parts = []

    for item in problems:
        parts = item.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        left = parts[0]
        op = parts[1]
        right = parts[2]

        if op != "+" and op != "-":
            return "Error: Operator must be '+' or '-'."

        if not left.isdigit() or not right.isdigit():
            return "Error: Numbers must only contain digits."

        if len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."

       
        if len(left) >= len(right):
            width = len(left) + 2
        else:
            width = len(right) + 2

      
        top_line = " " * (width - len(left)) + left
        bottom_line = op + " " * (width - 1 - len(right)) + right
        dashes = "-" * width

        top_line_parts.append(top_line)
        bottom_line_parts.append(bottom_line)
        dash_line_parts.append(dashes)

        if show_answers:
            if op == "+":
                value = int(left) + int(right)
            else:
                value = int(left) - int(right)

            result_str = " " * (width - len(str(value))) + str(value)
            result_line_parts.append(result_str)

    gap = "    "
    arranged = gap.join(top_line_parts) + "\n" + gap.join(bottom_line_parts) + "\n" + gap.join(dash_line_parts)

    if show_answers:
        arranged = arranged + "\n" + gap.join(result_line_parts)

    return arranged



print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print()
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))

