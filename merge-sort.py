import time

def open_crime(filename='Crime_Data_from_2020_to_2024(2).txt'):
    infile = open(filename)
    table = list()
    for data in infile:
            fields = data.rstrip('\n').split('\t')
            fields[0:1] = fields[0].split(maxsplit=1)
            record = tuple(fields)
            table.append(record)
    infile.close()
    return table

def open_vehicle(filename='Electric_Vehicle_Population_Data(2).txt'):
    infile = open(filename)
    table = list()
    for data in infile:
            fields = data.rstrip('\n').split('\t')
            record = tuple(fields)
            table.append(record)
    infile.close()
    return table
    
def merge_sort(records):
    if len(records) <= 1:
        return

    middle = len(records) // 2

    left = records[:middle]
    right = records[middle:]

    merge_sort(left)
    merge_sort(right)

    merge(records, left, right)


def merge(records, left, right):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            records[k] = left[i]
            i += 1
        else:
            records[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        records[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        records[k] = right[j]
        j += 1
        k += 1

def is_sorted(records):
    for i in range(len(records) - 1):
        if records[i][0] > records[i + 1][0]:
            return False
    return True

crime_data = open_crime()
vehicle_data = open_vehicle()

start_time = time.time()
merge_sort(crime_data[0:100])
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken to sort 100 crime records: {elapsed_time:.6f} seconds")

start_time = time.time()
merge_sort(vehicle_data[0:100])
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken to sort 100 vehicle records: {elapsed_time:.6f} seconds")

start_time = time.time()
merge_sort(crime_data)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken to sort all crime records: {elapsed_time:.6f} seconds")

start_time = time.time()
merge_sort(vehicle_data)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken to sort all vehicle records: {elapsed_time:.6f} seconds")