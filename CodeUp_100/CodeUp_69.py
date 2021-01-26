evaluation = input()
contents = {'A':'best!!!', 'B':'good!!', 'C': 'run!', 'D' : 'slowly~'}
print(contents.get(evaluation)) if evaluation in contents else print("what?")
