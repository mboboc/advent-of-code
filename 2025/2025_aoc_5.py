
import re

# %%
def aoc_1():
    with open("inputs/2025_input_aoc_5.txt", "r", encoding="utf-8") as fd:
        intervals = []
        min_start = None
        max_end = None
        for line in fd:
            if line == "\n":
                break

            char1, char2 = line.strip("\n").split("-")
            start = int(char1)
            end = int(char2)

            if min_start is None or start < min_start:
                min_start = start

            if max_end is None or end > max_end:
                max_end = end

            intervals.append((start, end))

        sorted(intervals, key=lambda x: x[1])

        print(min_start, max_end)
        print(intervals)
        fresh = 0
        for line in fd:
            ingredient_id = int(line)
            if ingredient_id < min_start or ingredient_id > max_end:
                continue

            for interval in intervals:
                if ingredient_id > interval[1]:
                    continue
                else:
                    if ingredient_id < interval[0]:
                        continue

                fresh += 1
                break

        print(fresh)


aoc_1()

#%%

def is_overlap(interval1, interval2):
    x1, x2 = interval1
    y1, _ = interval2

    if y1 >= x1 and y1 <= x2:
        return True

    return False

def merge_intervals(interval1, interval2):
    return (interval1[0], max(interval1[1], interval2[1]))

def aoc_2():
    with open("inputs/2025_input_aoc_5.txt", "r", encoding="utf-8") as fd:
        intervals = []
        min_start = None
        max_end = None
        for line in fd:
            if line == "\n":
                break

            char1, char2 = line.strip("\n").split("-")
            start = int(char1)
            end = int(char2)

            if min_start is None or start < min_start:
                min_start = start

            if max_end is None or end > max_end:
                max_end = end

            intervals.append((start, end))

        intervals = sorted(intervals, key=lambda x:x[0])
        print(intervals)

        # Merge intervals
        idx = 0
        while(True):
            if idx + 1 >= len(intervals):
                break

            if is_overlap(intervals[idx], intervals[idx + 1]):
                interval = merge_intervals(intervals[idx], intervals[idx + 1])
                del intervals[idx + 1]
                del intervals[idx]
                intervals.insert(idx, interval)
            else:
                idx += 1

        print(intervals)

        result = 0
        for interval in intervals:
            start, end = interval
            result += (end - start) + 1

        print(result)
aoc_2()
