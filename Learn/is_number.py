def is_number(input_to_test):
    """
    Checks to see if input_to_test is a valid number. The parameters for a valid number are:
    - Numbers are in base 10
    - Leading sign ( - ) and a single decimal point ( . ) are allowed
    - Trailing zeroes are acceptable (1.0000), but leading zeroes are not (00001)
        - 0.01 and .01 are acceptable
    - Decimals can be the last character (0. is acceptable)
    - "-.", ".", etc are not acceptable
 
    :param input_to_test: string
    :return: boolean
    """

    print("\n {} ".format(input_to_test))

    has_non_zero_numeric_char = False
    has_decimal_char = False
    is_zero = False
    characters_in_input = list(input_to_test)
    print("characters_in_input", characters_in_input)
 
    for index, character in enumerate(characters_in_input):
        print("index={}, character={}".format(index, character))
        try:
            current_character_value = int(character)
        except ValueError:
            if character == '.':
                if has_decimal_char is False:
                    has_decimal_char = True
                    continue
                else:
                    # one decimal char allowed only
                    return False
            elif character == '-':
                if index != 0:
                    return False
                else:
                    continue

        if current_character_value == 0:
            if index == 0:
                # first character can be leading zero
                if len(characters_in_input) == 1:
                    is_zero = True
                continue
            elif has_decimal_char is True:
                # can have zero if a decimal number
                continue
            elif has_non_zero_numeric_char is True:
                # can be trailing zero after a numeric char
                continue
            #elif int(characters_in_input[index - 1]) != 0: # this condition unnecessary. caught by conditions above
            #    # no more than one leading zero
            #    print("char zero char_in_input {}, index={}".format(characters_in_input[index - 1], index))
            #    continue

            return False
        else:
            has_non_zero_numeric_char = True
            continue
 
    if has_non_zero_numeric_char is False:
        # has to have a non_zero character unless it's zero itself
        if not is_zero: 
            return False
 
    return True


output = is_number('')
print("test1={}, expected={}".format(output, 'False'))
# invalid

output = is_number('5')
print("test2={}, expected={}".format(output, 'True'))
# valid

output = is_number('-5')
print("test3={}, expected={}".format(output, 'True'))
# valid

output = is_number('5.0')
print("test4={}, expected={}".format(output, 'True'))
# valid

output = is_number('007')
print("test5={}, expected={}".format(output, 'False'))
# invalid

output = is_number('0.01')
print("test6={}, expected={}".format(output, 'True'))
# valid

output = is_number('.01')
print("test7={}, expected={}".format(output, 'True'))
# valid

output = is_number('0')
print("test8={}, expected={}".format(output, 'True'))
# valid

output = is_number('5.')
print("test9={}, expected={}".format(output, 'True'))
# valid

output = is_number('.')
print("test10={}, expected={}".format(output, 'False'))
# invalid

output = is_number('5..0')
print("test10={}, expected={}".format(output, 'False'))
# invalid

output = is_number('7000')
print("test11={}, expected={}".format(output, 'True'))
# valid


