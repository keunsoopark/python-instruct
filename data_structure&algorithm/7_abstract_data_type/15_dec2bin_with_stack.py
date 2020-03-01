# Convert decimal to binary number

from stack import Stack

def dec2bin_with_stack(decnum):
    s = Stack()
    str_aux = ""

    while decnum > 0:
        s.push(decnum % 2)
        decnum = decnum // 2

    while not s.isEmpty():
        str_aux += str(s.pop())

    return int(str_aux)


if __name__ == "__main__":
    decnum = 9
    print(dec2bin_with_stack(decnum))
