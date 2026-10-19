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
    
def bubble_sort(records):
    top = len(records) - 1
    while top > 0:
        for i in range(top):
            if records[i][0] > records[i + 1][0]:
                temp = records[i]
                records[i] = records[i + 1]
                records[i + 1] = temp
        top -= 1

def is_sorted(records):
    for i in range(len(records) - 1):
        if records[i][0] > records[i + 1][0]:
            return False
    return True

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
bubble_sort(crime_data[0:100000])
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken to sort 100000 crime records: {elapsed_time:.6f} seconds")

start_time = time.time()
bubble_sort(vehicle_data[0:100000])
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken to sort 100000 vehicle records: {elapsed_time:.6f} seconds")