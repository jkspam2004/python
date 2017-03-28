import csv

def read_data(data):
    with open(data, 'r') as f:
        #data = [row for row in csv.reader(f)]
        data = [row for row in csv.reader(f.read().splitlines())]
    return data

def get_min_score_difference(parsed_data):
    parsed_data.pop(0) # pop off the header
    goals = [x[5] for x in parsed_data] # get all the 5th column and put in a new list
    goals_allowed = [x[6] for x in parsed_data] # get all the 6th column

    diffs = [float(x) - float(y) for x, y in zip(goals, goals_allowed)]
    return diffs.index(min(diffs)) # return the index of the minimum difference, to get winning team

def get_team(index, parsed_data):
    teams = [x[0] for x in parsed_data]
    return teams[index]

if __name__ == "__main__": 
    # only execute code if script run directly, not imported as a module by another file
    data = "/Users/eto/Git/python/Learn/tdd_package/src/football.csv"
    output =  read_data(data)
    for row in output:
        print row
    print

