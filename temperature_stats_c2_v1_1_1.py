def Mean_val(list_data):
    return sum(list_data)/len(list_data)

def Mode_val(list_data):
    #Step 1: Find the unique values of the list
    val_set = set(list_data)
    #Step 2: Conversion from set to list for computational purpose 
    val_list = list(val_set)
    Count = 0
    Freq = []
    # Step 3: Count the values
    # List of unique values
    for i in range(len(val_set)): #  For loop 1
    # List of temperature of a given month
        for j in range(len(list_data)): #  For loop 2
            # Compare the ith unique value with all the values of the input list 
            if val_list[i] == list_data[j]:
                Count = Count+1
        Freq.append(Count)
        Count = 0
        # Find the index of maximum frequency
        # Return the most repeated value in the input using the index 
    return val_list[Freq.index(max(Freq))]

temperature_2015 = {"January":[79.0,80.3,80.5,78.8,79.1,78.2,77.5,78.1,76.6,75.7,75.8,74.5,75.1,73.9,76.6,77.1,76.1,74.9,75.2,75.6,75.8,77.2,77.9,77.1,77.2,77.5,77.5,77.9,79.3,77.8,77.6],
"February":[77.7,78.2,77.8,77.6,78.6,78.8,78.9,77.8,77.4,76.7,78.4,79.0,79.1,79.6,79.3,79.2,78.2,79.0,79.2,78.2,78.5,78.3,80.7,82.0,82.3],
"March":[82.9,82.8,84.0,84.2,84.6,83.6,83.3,83.0,82.4,81.1,81.9,83.2,82.4,83.8,83.2,82.2,82.4,83.8,83.4,82.2,84.4,85.5,84.9,84.5,84.3,83.7,84.5,85.5,85.6,86.2],
"April":[85.7, 87.0,88.6,88.6,87.9,87.2,87.0,87.0,87.2,86.1,86.5,85.7,82.9,84.6,79.4,84.1,84.4,85.5,86.4,87.3,87.2,88.4,88.8,84.7,86.0,87.4,86.0,87.4,86.7,87.3,88.2,88.9],
"June":[85.1,86.8,88.0,88.8,89.0,88.9,90.4,89.9,87.7,89.0,89.9,88.1,89.4,88.8,90.3,87.4,83.6,81.9,85.0,87.7,90.7,92.4,89.8,91.9,92.5,93.1,89.7,88.7,89.0,89.5],
"July":[89.3,89.9,90.3,92.1,93.4,92.5,90.7,91.0,91.8,88.5,89.3,89.5,90.4,89.9,86.8,89.5,86.2,86.4,87.2,88.2,87.3,83.3,85.0,86.8,87.3,86.6,85.0,85.6,87.2,87.7,85.9],
"August":[85.0,84.1,87.1,84.3,85.7,87.3,85.9,87.7,88.1,87.1,87.0,86.2,87.0,87.2,87.3,86.2,81.2,82.1,85.6,87.4,88.2,87.7,84.2,86.1,88.1,87.1,87.3],
"Septemper":[89.0,88.0,86.0,87.4,86.7,88.0,83.0,86.1,85.1,84.9,86.1,86.1,86.5,87.3,88.4,89.9,88.1,87.5,87.0,86.2,86.4,87.1,87.3,87.8,87.8,87.3,85.3,84.3,82.6,84.5],
"October": [84.1,85.1 ,82.6,84.8,81.3,85.3,84.3,84.9,84.5,86.3,83.8,86.0 ,85.2,85.6,84.8,83.9,84.3,85.5,85.1,86.0,84.0,82.9,79.1,81.7,83.1,83.5,83.2,81.1,80.7,80.4 ,79.6],
"November":[83.5,84.3,77.6,77.3,77.2,79.9,79.7,77.1,82.5,83.6,82.3,82.7,81.0,79.8,77.5,79.6,78.9,79.6,80.9,80.2,82.5,82.6,78.8,79.9,78.2,80.0,79.3,79.6,78.2,78.3],
"December":[76.3,76.6,77.8,77.7,78.5,77.7,80.3,79.2,80.0,80.4,81.2,81.5,81.8,79.2,78.1,79.4,80.0,81.1,81.4,80.3,80.7,81.3,81.9,80.8,80.5,78.5,80.0,79.4,79.0,79.2,-99,-99]}

Mean_temp = Mean_val(temperature_2015["February"])
print(round(Mean_temp,2))
# Find the mean temperature values of each month and store it in a new dictionary
# {"January": mean_1,....}
# Find the Mode value of Jan, Feb.....
Mode_temp = Mode_val(temperature_2015["February"])

print(Mode_temp)
