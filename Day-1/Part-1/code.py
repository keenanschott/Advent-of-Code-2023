with open('./Day-1/input.txt', 'r') as f:
    data = f.read().split('\n')

calibration_values = []
for string in data:
    current_cal = ''
    for char in string:
        if char.isnumeric():
            current_cal += char
            break
    for char in string[ : : -1]:
        if char.isnumeric():
            current_cal += char
            break
    calibration_values.append(int(current_cal))

print(sum(calibration_values))