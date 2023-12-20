fruit={'Apple': 2, 'Orange': 14, 'Pineapple': 31, 'Watermelon': 61, 'Grapes': 10}
l=list(fruit)
print("before sorting:",l)
l.sort()
print("ascending order:",l)
l=list(fruit)
l.sort(reverse=True)
print("descending order:",l)
