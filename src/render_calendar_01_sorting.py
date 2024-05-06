# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")


# ----------------------------------------------------------------------------
# Render a Calendar:  Sorting
# ----------------------------------------------------------------------------

# sorting the endpoint array takes O(n * log(n)) time
# iterating through the sorted array takes O(n) time
# yielding an O(n * log(n)) time complexity

# space complexity = O(n), which is the size of the endpoint array


def find_max_simultaneous_events(A):

    # Builds an array of all endpoints.
    E = [p for event in A for p in (Endpoint(event.start, True), Endpoint(event.finish, False))]

    # Sorts the endpoint array according to the time, breaking ties by putting start times before end times
    E.sort(key=lambda e: (e.time, not e.is_start))
    print(E)

    # Track the number of simultaneous events, record the maximum number of simultaneous events.
    max_num_simultaneous_events, num_simultaneous_events = 0, 0

    for e in E:
        if e.is_start:
            num_simultaneous_events += 1
            max_num_simultaneous_events = \
                max(num_simultaneous_events, max_num_simultaneous_events)
        else:
            num_simultaneous_events -= 1

    return max_num_simultaneous_events


# ----------
import collections

Event = collections.namedtuple('Event', ('start', 'finish'))

Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))

event = [Event(s, f) for s, f in
         [(1, 5), (6, 10), (11, 13), (14, 15), (2, 7), (8, 9), (12, 15),
          (4, 5), (9, 17)]]

print(find_max_simultaneous_events(A=event))



