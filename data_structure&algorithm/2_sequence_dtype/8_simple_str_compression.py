# my answer - It is more and less the same as the book answer,
# but mine used str, while the book version used list.
def str_compression_kp(s):
    pre_c = ""
    counter = 1
    result = ""
    for character in s:
        if pre_c != character:
            result += str(counter)
            counter = 1
            result += character
        else:
            counter += 1
        pre_c = character

    return result[1:] + str(counter)


# This is from the book
def str_compression(s):
    count, last = 1, ""
    list_aux = []
    for i, c in enumerate(s):
        if last == c:
            count += 1
        else:
            if i != 0:
                list_aux.append(str(count))
            list_aux.append(c)
            count = 1
            last = c
    list_aux.append(str(count))
    return "".join(list_aux)


if __name__ == "__main__":
    result = str_compression_kp("aabcccccaaa")
    result2 = str_compression("aabcccccaaa")
    print(result)
    print(result2)
