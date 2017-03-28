def learn_zip():
    x = [1, 2, 3]
    y = [4, 5, 6]
    zipped = zip(x, y)
    print("x = {}".format(x))
    print("y = {}".format(y))
    print(list(zipped)) # [(1, 4), (2, 5), (3, 6)]
    print()

    z = [7, 8, 9]
    print("z = {}".format(z))
    zipped = zip(x, y, z) 
    print(list(zipped)) # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
    print()

    # iterator stops at the shortest input
    a = [100, 101]
    print("a = {}".format(a))
    zipped = zip(x, y, z, a)
    print(list(zipped)) # [(1, 4, 7, 100), (2, 5, 8, 101)]
    print()

    print(dict(zip(x,y)))

#learn_zip()

def test_zip():
    parsed_data = [
        ['Team', 'Games', 'Wins', 'Losses', 'Draws', 'Goals', 'Goals Allowed', 'Points'],
        ['Arsenal', '38', '26', '9', '3', '79', '36', '87'],
        ['Liverpool', '38', '24', '8', '6', '67', '30', '80']
    ]
    parsed_data.pop(0) # pop off the header
    print("parsed_data: {}".format(parsed_data))
    goals = [x[5] for x in parsed_data] # get all the 5th column and put in a new list
    goals_allowed = [x[6] for x in parsed_data] # get all the 6th column
    print("goals, goals_allowed: {}, {}".format(goals, goals_allowed))

    for x, y in zip(goals, goals_allowed):
        print("x, y: {}, {}".format(x, y))

    # difference list of goals - goals_allowed
    diffs = [float(x) - float(y) for x, y in zip(goals, goals_allowed)]
    print("list of diffs: {}".format(diffs))

    # return the minimum difference
    return min(diffs)

print(test_zip())
