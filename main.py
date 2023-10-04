# Завдання 1
#
# У списку цілих, заповненому випадковими числами обчислити:
#
# ■ Суму негативних чисел;
#
# ■ Суму парних чисел;
#
# ■ Суму непарних чисел;
#
# ■ Добуток елементів з кратними індексами 3;
#
# ■ Добуток елементів між мінімальним та максимальним елементом;
#
# ■ Суму елементів, що знаходяться між першим та останнім позитивними елементами.
#
# Завдання 2
#
# Є список цілих, заповнений випадковими числами.
#
# На підставі даних цього масиву потрібно:
#
# ■ Створити список цілих, що містить лише парні числа з першого списку;
#
# ■ Створити список цілих, що містить лише непарні числа з першого списку;
#
# ■ Створити список цілих, що містить лише негативні числа з першого списку;
#
# ■ Створити список цілих, що містить лише позитивні числа з першого списку.

import random
task_n = 1

while task_n != 3:
    try:
        task_n = int(input("Select please task number, that you want to check: \n"
                           "\t1. Порахуйте кількість літер, цифр у рядку. Виведіть обидві кількості на екран.\n"
                           "\t2. Порахуйте скільки разів у рядку зустрічається потрібний символ.\n"
                           "\t3. Stop checking tasks\n"
                           "Enter choise here: "))

        match task_n:
            case 1:
                finish_t1_l = "y"
                while finish_t1_l == "y":
                    rand_list = []
                    for i in range(20):
                        rand_list.append(random.randint(-10,10))
                    print(rand_list)

                    neg_sum = 0
                    for i in range(20):
                        if rand_list[i] < 0:
                            neg_sum = neg_sum + rand_list[i]
                    print(f"\t1. Sum of negative numbers is {neg_sum}")

                    odd_sum = 0
                    for i in range(20):
                        if rand_list[i] % 2 != 0:
                            odd_sum = odd_sum + rand_list[i]
                    print(f"\t2. Sum of even numbers is {odd_sum}")

                    even_sum = 0
                    for i in range(20):
                        if rand_list[i] % 2 == 0:
                            even_sum = even_sum + rand_list[i]
                    print(f"\t3. Sum of odd numbers is {even_sum}")

                    mul_3 = 0
                    mul_3_list = rand_list[::3]
                    for i in range(len(mul_3_list)):
                        mul_3 = mul_3 * mul_3_list[i]
                    print(f"\t4. Mul of numbers with indexes % 3 is {mul_3}")

                    mul_5 = 1
                    min_v_i = rand_list.index(min(rand_list))
                    max_v_i = rand_list.index(max(rand_list))
                    if min_v_i > max_v_i:
                        min_v_i, max_v_i = max_v_i, min_v_i
                    for i in range(min_v_i+1,max_v_i):
                        mul_5 = mul_5 * rand_list[i]
                    print(f"\t5. Mul of numbers btw min({min(rand_list)}) and max({max(rand_list)}) characters {mul_5}")

                    sum_6 = 0
                    for i in range(20):
                        if rand_list[i] > 0:
                            first_p_i = rand_list.index(rand_list[i])
                            break
                    rand_list_inv = rand_list[::-1]
                    for i in range(20):
                        if rand_list_inv[i] > 0:
                            last_p_i = rand_list_inv.index(rand_list_inv[i])
                            break
                    for i in range(first_p_i+1,len(rand_list)-last_p_i-2):
                        sum_6 = sum_6 + rand_list[i]
                    print(f"\t6. Sum of numbers btw first pos({rand_list[first_p_i]}) and last pos({rand_list[len(rand_list)-last_p_i-1]}) characters {sum_6}")

                    while finish_t1_l != "y" or finish_t1_l != "n":
                        finish_t1 = input("Do you want to continue?\n"
                                          "\ty - yes, n - no\n"
                                          "\tEnter your choice: ")
                        finish_t1_l = finish_t1.lower()
                        try:
                            if finish_t1_l == "y":
                                break
                            elif finish_t1_l == "n":
                                break
                            else:
                                raise Exception("Please enter valid answer!")
                        except Exception as e:
                            print(f"\tError: {e}")
            case 2:
                finish_t2_l = "y"
                while finish_t2_l == "y":

                    rand_list_t2 = []
                    for i in range(20):
                        rand_list_t2.append(random.randint(-10, 10))
                    print(f"\t{rand_list_t2}")

                    range_even = []
                    for i in range(len(rand_list_t2)):
                        if (rand_list_t2[i] % 2) == 0:
                            range_even.append(rand_list_t2[i])
                    print(f"\t{range_even}")

                    range_odd = []
                    for i in range(len(rand_list_t2)):
                        if (rand_list_t2[i] % 2) != 0:
                            range_odd.append(rand_list_t2[i])
                    print(f"\t{range_odd}")

                    range_pos = []
                    for i in range(len(rand_list_t2)):
                        if rand_list_t2[i] < 0:
                            range_pos.append(rand_list_t2[i])
                    print(f"\t{range_pos}")

                    range_neg = []
                    for i in range(len(rand_list_t2)):
                        if rand_list_t2[i] > 0:
                            range_neg.append(rand_list_t2[i])
                    print(f"\t{range_neg}")

                    while finish_t2_l != "y" or finish_t2_l != "n":
                        finish_t2 = input("Do you want to continue?\n"
                                          "\ty - yes, n - no\n"
                                          "\tEnter your choice: ")
                        finish_t2_l = finish_t2.lower()
                        try:
                            if finish_t2_l == "y":
                                break
                            elif finish_t2_l == "n":
                                break
                            else:
                                raise Exception("Please enter valid answer!")
                        except Exception as e:
                            print(f"\tError: {e}")
            case 3:
                print("\tThanks for your time!")
                break
            case _:
                raise Exception("Please enter a valid task number!")
    except ValueError as e:
        print("\tError: Please enter only integers!")
    except Exception as e:
        print(f"\tError: {e}")
