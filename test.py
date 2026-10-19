with open('Crime_Data_from_2020_to_2024.txt') as infile:
    data = infile.readline()
    print(repr(data))
    print("Number of tabs:", data.count('\t'))