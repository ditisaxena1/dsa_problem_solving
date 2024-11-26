"""
you have to find the number of meeting room required when you are provided the start and end time of the meeting
in a list and multi dimensional array.
I/P - [[10,20],[20,30],[15,25],[40,50]] and so on
O/P - number of meeting room required so that more than one meeting can take place at a time if timings are like this
"""

lst = [[10,20],[20,30],[15,25],[40,50]]
start_time = []
end_time = []
for inner_ele in lst:
    start_time.append(inner_ele[0])
    end_time.append(inner_ele[1])

print(sorted(start_time))
print(sorted(end_time))

