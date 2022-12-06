def chars_to_be_multiplyed(decode_str, starting_point: int, length_of_str: int, char_multiplyer: int) -> (str, int):
    length_of_str -= 1
    chars = ""
    result = ""
    result_of_recursion = ""
    i = starting_point
    while i <= length_of_str:
        # print(f'i - {i}')

        if decode_str[i].isdigit():
            char_multiplyer2 = int(decode_str[i]) - 1
            starting_point = i + 2
            result_of_recursion = str(
                chars_to_be_multiplyed(decode_str, starting_point, length_of_str, char_multiplyer2))
            # print(result_of_recursion)

        elif decode_str[i] == "]":
            print(result_of_recursion)
            result = (chars + result_of_recursion)
            result = result * char_multiplyer
            return result
        else:
            if decode_str[i] != "[":
                chars = chars + decode_str[i]

        i += 1


def decoding(decode_str: str):
    resulting = ""
    for i in range(len(decode_str)):
        if decode_str[i].isdigit():
            print(f"mylty - {decode_str[i]}")
            char_multiplyer = int(decode_str[i]) - 1
            starting_point = i + 2
            length_of_str = len(decode_str)
            resulting = resulting + str(
                chars_to_be_multiplyed(decode_str, starting_point, length_of_str, char_multiplyer))
        elif decode_str[i] != "[" and decode_str[i] != "]":
            resulting = resulting + decode_str[i]
    print(resulting)


decode_str = "3[b2[ca]]"
decoding(decode_str)
decode_str = "3[а]cf3[df]"
decoding(decode_str)
