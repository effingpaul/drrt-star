# let dRRT run 10 times on a given map

import numpy as np

from dRRT import drrt

n_trials = 10
map = "map3.txt"
times = []
successes = 0
start=[[3, 45], [97, 55]] #[[51, 71], [50, 33]]
end=[[95, 55],[4, 45]] #[[46, 30],[47, 64]]
#start = [[51, 71], [50, 33]]
#end = [[46, 30],[47, 64]]

for i in range(n_trials):

    time_needed, path_length = drrt(visuals=True, mapString=map, start=start, end=end)
    if time_needed >= 0:
        successes += 1
        times.append(time_needed)
    print(time_needed, "   ", path_length)
        

print("For map ", map, " dRRT needed on average ", np.average(times), " seconds with s.d. of ", np.std(times))
print("The success rate was ", (successes/n_trials))
