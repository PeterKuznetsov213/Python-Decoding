def chars_to_be_multiplyed(decode_str, starting_point: int, length_of_str: int, char_multiplyer: int):
    length_of_str -= 1
    chars = ""
    result = ""
    result_of_recursion = ""
    i = starting_point
    while i <= length_of_str:
        print(f'i - {i}')
        if decode_str[i].isdigit():
            char_multiplyer = int(decode_str[i])
            starting_point = i + 2
            result_of_recursion = str(
                chars_to_be_multiplyed(decode_str, starting_point, length_of_str, char_multiplyer))
            i += 1
        elif decode_str[i] == "]":
            result = (chars + result_of_recursion) * char_multiplyer
            return result
        else:
            if decode_str[i] != "[":
                chars = chars + decode_str[i]

        i += 1


decode_str = "1[b]"


def decoding(decode_str: str):
    result = ""
    for i in range(len(decode_str)):
        if decode_str[i].isdigit():
            print(f"mylty - {decode_str[i]}")
            char_multiplyer = int(decode_str[i])
            starting_point = i + 2
            length_of_str = len(decode_str)
            result = result + str(chars_to_be_multiplyed(decode_str, starting_point, length_of_str, char_multiplyer))
        elif decode_str[i] != "[" and decode_str[i] != "]":
            result = result + decode_str[i]
    return result


print(decoding(decode_str))
