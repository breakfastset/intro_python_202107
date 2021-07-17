def main():  # main function

    # step 1 - welcome message
    print("Welcome to Scoring System version 99.9!")

    # step 2 - ask the user for an indeterminate number of scores
    scores = [38, 58, 67, 23, 71, 96, 55, 66, 77, 83, 42, 21, 5, 99, 44, 66, 77, 50, 27, 82]

    # step 3 - determine the top 3 scores and print the top 3 scores
    top_three_scores = get_top_three(scores) # [ 99, 91, 80 ]
    print("Top 3 scores are: ")
    print(top_three_scores)


def get_top_three(the_scores):
    sorted_scores = sorted(the_scores, reverse=True)
    results = [sorted_scores[0], sorted_scores[1], sorted_scores[2]]
    return results


# call main to run
main()
