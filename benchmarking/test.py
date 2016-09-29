import sys, os, math
import imp, array, subprocess, collections
from trial import Trial
from ctypes import *


def run_test(upper_len, incr, num_trials, func, is_c, safety_time = 2):
    '''Returns multidimensional array of [[array_size, time],...]

    upper_len  - @type - int
               - @param - the longest array size that should be tested on
    incr       - @type - int
               - @param - increment the length of array for every set of trials
    num_trials - @type - int
               - @param - how many trials for every array length?
    func       - @type - function
               - @param - the function to run the trials on
    '''

    trials = []
    cur_len = 1
    int_bound = int(math.log(sys.maxint, 2))  #is C's longint, actually
    do_more = True
    while (cur_len <= upper_len and do_more):
        for i in range(num_trials):
            t = Trial()
            t.set_test_data(True, [], int, cur_len, int_bound)
            t.run_test(func, is_c)
            trials.append([cur_len, t.get_elapsed_time()])
            e_t = t.get_elapsed_time()
            # if it took more than safety_time, finish this set and stop
            if (e_t > safety_time):
                do_more = False
        cur_len += incr
    return trials

def get_c_lib(path, filename):
    ''' compiles the file'''
    # Compile
    in_fn = "{}/{}".format(path, filename)
    out_fn = "{}/{}.{}".format(path, filename.split(".")[0], "out")


    compile_call = ["gcc", "-Wall", in_fn, "-o", out_fn]
    subprocess.call(compile_call)

    # retrieve
    lib = cdll.LoadLibrary("{}".format(out_fn))
    return lib


def get_functions(parent_dir, child_dir, langs):
    ''' Returns multidimensional list [[module_name, function_object],...]
        parent_dir - @type  - string
                   - @param - the top level directory to search, e.g. `sorting`
        child_dir  - @type  - string
                   - @param - the second level directory to search, e.g. `insertion`
                            - if empty, all dirs are of parent_dir are searched
        langs      - @type  - list
                   - @param - the file extensions to retrieve

    '''

    search_dir = "{}/{}/{}".format(os.getcwd(), parent_dir, child_dir)
    functions = []
    for directory, child_dirs, files in os.walk(search_dir):
        if (child_dirs):
            continue

        for fn in files:
            mod_name = fn.split(".")

            if (mod_name[1] not in langs or mod_name[0] == "__init__"):
                continue
            elif (mod_name[1] == "c"):
                lib = get_c_lib(directory, fn)
            else:
                m = imp.find_module(mod_name[0], [directory])
                lib = imp.load_module(mod_name[0], m[0], m[1], m[2])

            functions.append([mod_name[0], mod_name[1], lib.wrapper])

    return functions



def manage_tests(algo_class, algo, upper_len, increment, num_trials, langs):
    ''' Returns dictionary of {algorithm : [trial0, trial1, ...]}

        Runs tests for either all algorithms in algo_class, or the specified
        `algo` algorithm

        algo_class - @type - string
                   - @param - the type of algorithms. e.g. sorting, searching, etc
        algo       - @type - string
                   - @param - which algo of algo_class should be run? e.g. insertion_sort
                   - if left empty, all algos in algo_class will be run
        upper_len  - @type - int
                   - @param - the longest list/arr the algo should work on
        increment  - @type - int
                   - @param - starting at 1, increase length by n while < upper_len
        num_trials - @type - int
                   - @param - # of trials to run for each list size
        langs      - @type - list
                   - @param - the script extensions (py, c) to run
    '''


    functions = get_functions(algo_class, algo, langs)

    results = {}

    for name, lang, func in functions:
        if (lang == "c"):
            is_c = True
        else:
            is_c = False
        results[name] = run_test(upper_len, increment, num_trials, func, is_c)
    return results

def get_average(data):
    aggs = collections.OrderedDict()
    for datum in data:
        try:
            aggs[datum[0]][0] += datum[1]
            aggs[datum[0]][1] += 1
        except KeyError:
            aggs[datum[0]] = [datum[1], 1]

    avgs = []
    for x in aggs:
        avgs.append([x, aggs[x][0]/aggs[x][1]])

    return avgs

def plot_results(results, destination):
    ''' Returns destination of plot as string

    Plots the results into a linegraph in an html file

    results     - @type  - dictionary
                - @param - dictionary names as keys with multidimensional lists of
                           x,y coordinates
    destination - @type  - string
                - @param - the fullpath of the html file to write to
    '''
    from plotly.offline import plot
    from plotly.graph_objs import Scatter

    graph_lines = []
    for name in results:
        line = Scatter(
                    x = [data[0] for data in results[name]] ,
                    y = [data[1] for data in results[name]],
                    mode = 'markers',
                    name = name
                )
        graph_lines.append(line)

        avgs = get_average(results[name])

        line = Scatter(
            x = [d[0] for d in avgs],
            y = [d[1] for d in avgs],
            mode = 'line',
            name = "avg {}".format(name)
        )
        graph_lines.append(line)
    d_name = plot(graph_lines, filename=destination)
    return d_name
