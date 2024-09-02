def grade(score):
    if score > 0 and  score < 20:
        return "F"
    elif score < 40:
        return "D"
    elif score < 60:
        return "C"
    elif score < 80:
        return "B"
    elif score <= 100:
        return "A"
    else:
        return "out of range"

print(grade(70))