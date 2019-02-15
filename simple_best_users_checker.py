# coding: UTF-8

from collections import defaultdict, OrderedDict


def id_best_users(*args):
    counter_dict = defaultdict(lambda: defaultdict(lambda: 0))
    number_of_month = len(args)

    for i, users_list in enumerate(args):
        for u in users_list:
            counter_dict[u][i] += 1

    result_dict = defaultdict(list)
    for user in counter_dict.keys():
        if len(counter_dict[user].keys()) == number_of_month:
            result_dict[sum(counter_dict[user].values())].append(user)

    result_dict = OrderedDict(sorted(result_dict.items(), key=lambda x: (x[0], x[1].sort()), reverse=True))

    return [[key, value] for key, value in result_dict.iteritems()]


if __name__ == '__main__':
    import cProfile
    import string
    from random import randint

    def generate_test_list(users_amount, purchases_amount, months__amount):
        uppercase_letters = string.ascii_uppercase

        users = [uppercase_letters[randint(0, len(uppercase_letters) - 1)]
                 + str(randint(0, 100)).zfill(3) for _ in range(users_amount)]

        return [[users[randint(0, len(users) - 1)] for _ in range(purchases_amount)] for _ in range(months__amount)]

    low_performance_data = generate_test_list(200, 100, 8)
    print 'Low performance data generated'

    pr = cProfile.Profile()
    pr.enable()
    id_best_users(*low_performance_data)
    pr.disable()
    pr.print_stats(sort="calls")

    high_performance_data = generate_test_list(90000, 80000, 12)
    print 'High performance data generated'

    pr = cProfile.Profile()
    pr.enable()
    id_best_users(*high_performance_data)
    pr.disable()
    pr.print_stats(sort="calls")

