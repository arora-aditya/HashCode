from solution import Solution

with open(argv[0], 'rb') as file:
    # Step 3
    solution = pickle.load(file)
    print(solution)