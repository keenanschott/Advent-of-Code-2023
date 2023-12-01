def is_substring_in_dict_keys(target_string, my_dict):
    for key in my_dict.keys():
        if key in target_string:
            return key
    return False

number_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six" : 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

with open('./Day-1/input.txt', 'r') as f:
    data = f.read().split('\n')

calibration_values = []
for string in data:
    current_cal = ''
    for i in range(len(string)):
        if string[i].isnumeric():
            current_cal += string[i]
            break
        elif string[i + 1].isnumeric():
            continue
        target_key = is_substring_in_dict_keys(string[i : min(i + 5, len(string))], number_dict)
        if target_key:
            current_cal += str(number_dict[target_key])
            break
    for i in range(len(string) - 1, -1, -1):
        if string[i].isnumeric():
            current_cal += string[i]
            break
        elif string[i - 1].isnumeric():
            continue
        target_key = is_substring_in_dict_keys(string[max(0, i - 4) : i + 1], number_dict)
        if target_key:
            current_cal += str(number_dict[target_key])
            break
    calibration_values.append(int(current_cal))

print(sum(calibration_values))