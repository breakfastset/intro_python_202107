
###########################
# 85 <= score <= 100 -> HD
# 70 <= score < 85 -> D
# 50 <= score < 70 -> C
# 0 <= score < 50 -> F
# otherwise -> Invalid
##########################

score = 67   # this is the current score
grade = ""  # to store the grade

if 85 <= score <= 100:
    grade = "HD"
elif 70 <= score < 85:
    grade = "D"
elif 50 <= score < 70:
    grade = "C"
elif 0 <= score < 50:
    grade = "F"
else:
    grade = "Invalid"

print("Your grade for {} marks is {}".format(score, grade))

print("Your grade {1} and {0} marks will be recorded... {1} saved!".format(score, grade))