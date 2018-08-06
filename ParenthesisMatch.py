def isValid(s):
    main_reference = {'(': ')', '{': '}', '[': ']'}
    checker = []
    if len(s) % 2 != 0:
        return False
    for parenthesis in s:
        if parenthesis in main_reference:
            checker.append(parenthesis)
            continue

        if parenthesis not in main_reference and (not checker or parenthesis != main_reference[checker[-1]]):
            return False
        else:
            checker.pop()
    return checker == []


if __name__ == "__main__":
   print(isValid("((())"))
   print(isValid("()[]{}"))
   print(isValid("()[{]}"))
   print(isValid("{}"))
