

peanuts = ["snoopy", "woodstock", "charlie brown", "lucy", "linus", "Sally", "marcie", "pigpen", "peppermint pattie"]
# S has a ASCII value of
sorted_peanuts = sorted(peanuts)  # sorted() produces a sorted copy of the original list

print(sorted_peanuts)
print(peanuts)  # original list is not sorted

peanuts.sort(reverse=True) # sorts the original list in reverse manner
print(peanuts)
