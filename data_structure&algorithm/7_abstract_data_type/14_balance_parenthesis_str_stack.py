# Check if the pair of parenthesis is balanced or not by using stack
# but the given code does not work if there is something between ( and ).

from stack import Stack


def balance_per_str_with_stack_given(str1):
    s = Stack()
    balanced = True
    index = 0

    while index < len(str1) and balanced:
        symbol = str1[index]

        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index = index + 1

    if balanced and s.isEmpty():
        return True
    return False


def balance_per_str_with_stack_kp(str1):
    s = Stack()
    balanced = True
    index = 0

    while index < len(str1) and balanced:
        symbol = str1[index]

        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            elif str1[index] == ")":
                s.pop()
        index = index + 1

    if balanced and s.isEmpty():
        return True
    return False


if __name__ == "__main__":
    print(balance_per_str_with_stack_given("((()))"))
    print(balance_per_str_with_stack_given("(()"))
    print(balance_per_str_with_stack_given("())"))
    print(balance_per_str_with_stack_given("((a)"))     # This is wrong

    print("\noppa code")
    print(balance_per_str_with_stack_kp("((()))"))
    print(balance_per_str_with_stack_kp("(()"))
    print(balance_per_str_with_stack_kp("())"))
    print(balance_per_str_with_stack_kp("((a)"))
