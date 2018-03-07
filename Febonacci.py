
def produce_set(number_of_runs):
    data_set = [1, 1]

    for x in range(2, number_of_runs+1):
        data_set.append(data_set[x-1] + data_set[x-2])

    print(data_set)

    return data_set


def find_ratio(data_set):
    ratio_set = []

    for x in range(2, len(data_set)):
        ratio = data_set[x]/data_set[x-1]
        ratio_set.append(ratio)

    total = 0
    for x in ratio_set:
        total = total + x

    return total/len(ratio_set)


input = int(input("How many different data values do you want?: "))

print()
print("The closest approximation to the reoccuring ratio is : " + str(find_ratio(produce_set(input))))
