#Program #3: US_Population
#Clara Riley
#Luke Snell
#10/18/24

def main():

    data = []

    while True:
        year = int(input("Enter the year (or 0 to stop): "))
        if year == 0:
            break
        state = input("Enter the name of the state: ")
        population = int(input("Enter the population: "))
        data.append([year, state, population])

    print("\nData entered:")
    for entry in data:
        print(entry)

    target_year = int(input("\nEnter the year to sum populations for: "))
    total_population = sum(entry[2] for entry in data if entry[0] == target_year)
    print(f"\nTotal population for the year {target_year}: {total_population}")

if __name__ == '__main__':
    main()
