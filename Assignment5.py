# Queens College
# Dicrete Structures CSCI 220
# Winter 2024
# Assignment 5
# Mikdad Abdullah
# Collaborated With Class

import inspect
import pandas as pd
import matplotlib.pyplot as plt
from math import log, factorial, sqrt


# [1] Copy the function from Assignment #1 that gives the content of a function,
# i.e. the code just after the return statement.


def func_body(f):
    body = inspect.getsource(f)  # gets the code
    idx = body.index("return")  # get the part after return
    return body[7 + idx:].strip()


# [2] Define several different functions called f0, f1, f2, f3, etc. Let f0 be the Identity Function, i.e. f(n) = n.
# Let f1 thru f10 be the functions that appear in Slide 50 of Chapter 3.
# Then define functions f11-f20 using the functions from the Final Exam for Summer 2023, Session 2, Problem 3.


def f0(n):
    return n


def f1(n):
    return 1.5 ** n


def f2(n):
    return 8 * n ** 3 + 17 * n ** 2 + 111


def f3(n):
    return (log(n)) ** 2


def f4(n):
    return 2 ** n


def f5(n):
    return log(log(n))


def f6(n):
    return n ** 2 * (log(n)) ** 3


def f7(n):
    return 2 ** n * (n ** 2 + 1)


def f8(n):
    return n ** 3 + n * (log(n)) ** 2


def f9(n):
    return 10000


def f10(n):
    return factorial(n)


def f11(n):
    return 3 ** n


def f12(n):
    return n ** 3 * (log(n,3))


def f13(n):
    return 3 * n ** 3 + 3 * n ** 2 + 3 * n + 3


def f14(n):
    return factorial(333)


def f15(n):
    return 3 ** (log(n, 3))


def f16(n):
    return 3 ** sqrt(n)


def f17(n):
    return n * log(log(n,3) , 3)


def f18(n):
    return factorial(3 * n)


def f19(n):
    return sqrt(n) ** 3


def f20(n):
    return (n * log(n, 3)) ** 3


# [3] Define a function compute_values() to evaluate all functions in a list for a set of values of n.


def compute_values(funcs, inputs):
    dict_funcs = {}
    for func in funcs:
        funcName = func_name(func)
        dict_funcs[funcName] = {}
        for n in inputs:
             dict_funcs[funcName][n] = log(func(n))
    return dict_funcs


# [4] Define a function print_values() to print the values of the functions for different inputs,
# both as is and ranked by the last column..


def print_values(dict_funcs, ranked=False):
    print("List of functions", "ranked" if ranked else "unranked")
    pd.set_option("display.max_rows", 500)
    pd.set_option("display.max_columns", 500)
    pd.set_option("display.width", 1000)
    df = pd.DataFrame.from_dict(dict_funcs).T
    if ranked:
        df = df.sort_values(by=[df.columns[-1]])
    print(df)


def func_name(func):
    return func.__name__+" "+func_body(func)


# [5] Define a function plot_graph() to plot the graph. Use both the name of the function
# and its content as the labels


def plot_values(file_name, dict_funcs, inputs, funcs):
    func_num = 0
    plt.xticks([j for j in range(len(inputs))], [str(n) for n in inputs])
    for func in funcs:
        funcName = func_name(func)
        func_num += 1
        d = dict_funcs[funcName]
        x_axis = [j + 0.05 * func_num for j in range(len(inputs))]
        y_axis = [d[i] for i in inputs]
        plt.bar(x_axis, y_axis, width=0.05, alpha=0.75, label=func_body(func))
    plt.legend()
    plt.title("Value of functions")
    plt.xlabel("n")
    plt.ylabel("log f(n)")
    plt.savefig(file_name)
    plt.show()


# [6] Define a function process_functions(functions, inputs) that does the calculating, tabulating, and plotting:


def process_functions(assn, functions, inputs):
    dict_funcs = compute_values(functions, inputs)
    plot_values(assn + '.png', dict_funcs, inputs, functions)
    print_values(dict_funcs, False)
    print()
    print_values(dict_funcs, True)


# [7] Run the code for two batches of functions f0-f10 and f11-f20.


def main():
    assn = "Assignment05"
    inputs = [10 * i for i in range(1, 11)]
    funcs1 = [f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]
    process_functions(assn + "a", funcs1, inputs)
    funcs2 = [f11, f12, f13, f14, f15, f16, f17, f18, f19, f20]
    process_functions(assn + "b", funcs2, inputs)


if __name__ == "__main__":
    main()

