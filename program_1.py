#Program #1: Rainfall
#Clara Riley
#Luke Snell
#10/18/24

rainfall_data = []

for i in range(12):
    rainfall = float(input(f"Enter the rainfall for month {i+1}: "))
    rainfall_data.append(rainfall)

total_rainfall = sum(rainfall_data)

average_rainfall = total_rainfall / 12

max_rainfall = max(rainfall_data)
min_rainfall = min(rainfall_data)
max_month = rainfall_data.index(max_rainfall) + 1
min_month = rainfall_data.index(min_rainfall) + 1

print(f"Total rainfall for the year is: {total_rainfall:.2f}")
print(f"Average rainfall per month is: {average_rainfall:.2f}")
print(f"Most rainfall in a month is: Month {max_month} with {max_rainfall:.2f}")
print(f"Least rainfall in a month is: Month {min_month} with {min_rainfall:.2f}")
