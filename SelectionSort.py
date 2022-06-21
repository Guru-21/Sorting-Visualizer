import time # To help us visualize this algorithm step by step



def SelectionSort(data, drawDataArray, sortSpeedTime):
    # Traverse through all array elements
    for i in range(len(data)):
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element

        data[i], data[min_idx] = data[min_idx], data[i]

        # Reflect the swapped values using the drawDataArray function
        # Blue = Done with Sorted, Red = Unsorted, Purple = Being Swap / Being Sorted
        drawDataArray(data, ['purple' if x == min_idx or x == i else 'red' for x in range(len(data))])
        # Helps us determine how long this function should be asleep for once the user can see each step of this algorithm
        time.sleep(sortSpeedTime)