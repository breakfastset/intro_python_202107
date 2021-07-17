
# list of student scores
scores = [38, 58, 67, 23, 71, 91, 55, 66, 77, 80, 42, 21, 5, 99, 44, 66, 77, 50]

# len() to find the number of scores
number_of_scores = len(scores)
print("Number of scores: {}".format(number_of_scores))

# max() to find the highest score
highest_score = max(scores)
print("Highest score: {} ".format(highest_score))

# min() to find the lowest score
lowest_score = min(scores)
print("Lowest score: {} ".format(lowest_score))

# average score
average_score = sum(scores) / number_of_scores
print("Average score: {:.1f}".format(average_score))

