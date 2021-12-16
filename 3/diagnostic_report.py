print("Day 3: Binary Diagnostic Part 1 & 2 (Not yet functioning :))")


def get_input():
    with open("3/input.txt") as f:
        return f.read().splitlines()


def gen_diagnostic_report():
    gamma_rate = ""
    for i in range(12):
        temp_column = []
        for input in get_input():
            temp_column.append(input[i])
        gamma_rate += "1" if temp_column.count("1") >= len(get_input()) / 2 else "0"

    epsilon_rate = gamma_rate.translate(gamma_rate.maketrans("10", "01"))
    print("Gamma rate:", gamma_rate)
    print("Epsilon rate:", epsilon_rate)
    print("Power consumption:", int(gamma_rate, 2) * int(epsilon_rate, 2))


def determine_most_common(input_list, index):
    indexed_list = []
    for line in input_list:
        indexed_list.append(line[index])
    return "1" if indexed_list.count("1") >= len(input_list) / 2 else "0"


def filter_list(target_list, number, index, weight):
    if len(target_list) == 2:
        return filter(lambda r: r[index] == weight, target_list)
    return filter(lambda r: r[index] == number, target_list)


def find_oxygen_generator_rating():
    data = get_input().copy()
    for i in range(12):
        most_common = determine_most_common(get_input(), i)
        data = list(filter_list(data, most_common, i, "1"))
        if len(data) == 1:
            return data[0]
    return data


def find_co2_scrubber_rating():
    data = get_input().copy()
    for i in range(12):
        least_common = str(abs(int(determine_most_common(get_input(), i)) - 1))
        data = list(filter_list(data, least_common, i, "0"))
        if len(data) == 1:
            return data[0]
    return data


def gen_life_support_rating():
    oxygen_generator_rating = find_oxygen_generator_rating()
    print("oxygen_generator_rating:", oxygen_generator_rating)

    co2_scrubber_rating = find_co2_scrubber_rating()
    print("co2_scrubber_rating:", co2_scrubber_rating)

    print(
        "Life support rating:",
        int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2),
    )
    # 4135032 too high
    # 230 too low
    # 4128201 too high
    # 4128201
    # 4135032


if __name__ == "__main__":
    gen_diagnostic_report()
    gen_life_support_rating()
