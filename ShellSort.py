import time # To help us visualize this algorithm step by step



def ShellSort(data, drawDataArray, sortSpeedTime):
    n = len(data)
    gap = n // 2
    while gap > 0:
        j = gap
        # Check the array in from left to right
        # Till the last possible index of j
        while j < n:
            i = j - gap  # This will keep help in maintain gap value
            while i >= 0:
                # If value on right side is already greater than left side value
                # We don't do swap else we swap
                if data[i + gap] > data[i]:
                    break
                else:
                    data[i + gap], data[i] = data[i], data[i + gap]
                    # Reflect the swapped values using the drawDataArray function
                    # Blue = Done with Sorted, Red = Unsorted, Purple = Being Swap / Being Sorted
                    drawDataArray(data, ['purple' if x == i + gap or x == i else 'red' for x in range(len(data))])
                    # Helps us determine how long this function should be asleep for once the user can see each step of this algorithm
                    time.sleep(sortSpeedTime)

                i = i - gap  # To check left side also
                # If the element present is greater than current element
            j += 1
        gap = gap // 2
