

if __name__ == "__main__":
    import argparse, os, time
    import benchmarking.test as test

    parser = argparse.ArgumentParser()

    parser.add_argument("-t", "--type",
                        type=str,
                        required = True,
                        help="the type of algorithm - sorting, searching, etc")
    parser.add_argument("-a", "--algorithm",
                        type=str,
                        required=False,
                        default="",
                        help="the algorithm within type. Can be empty")
    parser.add_argument("-l", "--arraylength",
                        type=int,
                        required=False,
                        default=1000,
                        help="the longest array to test the algorithms on")
    parser.add_argument("-s", "--step",
                        type=int,
                        required=False,
                        default=100,
                        help="how much to step the array size by")
    parser.add_argument("-n", "--numtimes",
                        type=int,
                        required=False,
                        default=10,
                        help="# of trials to run for each step")
    parser.add_argument("-f", "--filedestination",
                        type=str,
                        required=False,
                        default="{}/graph_{}.html".format(os.getcwd(), int(time.time())),
                        help="# of trials to run for each step")
    parser.add_argument("-p", "--python",
                        action="store_true",
                        default=False,
                        required=False,
                        help="Run on python scripts")
    parser.add_argument("-c", "--clang",
                        action="store_true",
                        default=False,
                        required=False,
                        help="Run on c scripts")
    args = parser.parse_args()

    langs = []
    if args.python: langs.append("py")
    if args.clang: langs.append("c")

    results = test.manage_tests(args.type, args.algorithm, args.arraylength, args.step, args.numtimes, langs)
    destination = test.plot_results(results, args.filedestination)
    print "the resulting graph has been save in {}".format(destination)
