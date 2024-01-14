In this project, we use tables and plots to compare a set of functions f(n) for several different values of n.  Because the range of inputs and outputs varies so greatly, we will fare better -  for the purposes of the table and graph - by taking the log of the output. See https://en.wikipedia.org/wiki/Log%E2%80%93log_plot 

[1] Copy the function from Assignment #1 that gives the content of a function, i.e. the code just after the return statement.

def func_body(f):
    body = inspect.getsource(f)  # gets the code
    idx = body.index("return")  # get the part after return
    return body[7 + idx:].strip()

[2] Define several different functions called f0, f1, f2, f3, etc. Let f0 be the Identity Function, i.e. f(n) = n. Let f1 thru f10 be the functions that appear in Slide 50 of Chapter 3.  Then define functions f11-f20 using the functions from the Final Exam for Summer 2023, Session 2, Problem 3.

[3] Define a function compute_values() to evaluate all functions in a list for a set of values of n. 

def compute_values(funcs, inputs):
    dict_funcs = {}
    for func in funcs:
        funcName = get_func_name(func)
        dict_funcs[funcName] = {}
        for n in inputs:
             dict_funcs[funcName][n] = log(func(n))
    return dict_funcs
 
[4] Define a function print_values() to print the values of the functions for different inputs, both as is and ranked by the last column..

def print_values(dict_funcs, ranked=False):
    print("List of functions", "ranked" if ranked else "unranked")	
    pd.set_option("display.max_rows", 500)
    pd.set_option("display.max_columns", 500)
    pd.set_option("display.width", 1000)
    df = pd.DataFrame.from_dict(dict_funcs).T
    if ranked:
        df = df.sort_values(by=[df.columns[-1]])
    print(df)

[5] Define a function plot_graph() to plot the graph. Use both the name of the function and its content as the labels

def plot_values(file_name, dict_funcs, inputs, funcs):
    func_num = 0
    plt.xticks([j for j in range(len(ns))], [str(n) for n in inputs])
    for func in funcs:
        funcName= get_func_name(func)
        func_num += 1
        d = dict_funcs[funcName]
        x_axis = [j + 0.05 * func_num for j in range(len(inputs))]
        y_axis = [d[i] for i in ns]
        plt.bar(x_axis, y_axis, width=0.05, alpha=0.75, label=func_body(func))
    plt.legend()
    plt.title("Value of functions")
    plt.xlabel("n")
    plt.ylabel("log f(n)")
    plt.savefig(file_name)
    plt.show()

[6] Define a function process_functions(functions, inputs) that does the calculating, tabulating, and plotting:

def process_functions(assn, functions, inputs):
    dict_funcs = eval_funcs(funcs, inputs)
    plot_values(assn + '.png', dict_funcs, inputs, funcs)
    print_values(dict_funcs, False)
    print_values(dict_funcs, True)

[7] Run the code for two batches of functions f0-f10 and f11-f20.

def main():
    assn = "Assignment05"
    inputs = [10 * i for i in range(1, 11)]
    funcs1 = [f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]
    process_functions(assn, funcs1, inputs)
    process_functions(assn, funcs2, inputs)
