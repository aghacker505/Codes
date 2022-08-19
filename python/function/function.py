def percent(line):
    p = ((line[0] + line[1] + line[2] + line[3] + line[4])/500)*100
    return p


marks1 = [75, 45, 80, 95, 76]
percentage1 = percent(marks1)

marks2 = [75, 96, 45, 99, 97]
percentage2 = percent(marks2)

print(percentage1, percentage2)
