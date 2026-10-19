import time

def open_crime(filename='Crime_Data_from_2020_to_2024.txt'):
    infile = open(filename)
    table = list()
    for data in infile:
            fields = data.rstrip('\n').split('\t')
            fields[0:1] = fields[0].split(maxsplit=1)
            record = tuple(fields)
            table.append(record)
    infile.close()
    return table

def open_vehicle(filename='Electric_Vehicle_Population_Data.txt'):
    infile = open(filename)
    table = list()
    for data in infile:
            fields = data.rstrip('\n').split('\t')
            record = tuple(fields)
            table.append(record)
    infile.close()
    return table
    
def bubble_sort(list):
    top = len(list) - 1
    while top > 0:
        for i in range(top):
            if list[i][0] > list[i + 1][0]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
        top -= 1

crime_data = open_crime()
vehicle_data = open_vehicle()

start_time = time.time()
bubble_sort(crime_data[0:100])
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken to sort 100 crime records: {elapsed_time:.6f} seconds")

start_time = time.time()
bubble_sort(vehicle_data[0:100])
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken to sort 100 vehicle records: {elapsed_time:.6f} seconds")

start_time = time.time()
bubble_sort(crime_data)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken to sort all crime records: {elapsed_time:.6f} seconds")

start_time = time.time()
bubble_sort(vehicle_data)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken to sort all vehicle records: {elapsed_time:.6f} seconds")