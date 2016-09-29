# algorithms

Test the speed of various algorithms written in Python and C

**To run**

python main.py -t TYPE [-a ALGORITHM] [-l ARRAYLENGTH] [-s STEP] [-n NUMTIMES] [-f FILEDESTINATION] [-p] [-c]

**Arguments**
```
  -h, --help            show this help message and exit
  -t TYPE, --type TYPE  the type of algorithm - sorting, searching, etc
  -a ALGORITHM, --algorithm ALGORITHM
                        the algorithm within type. Can be empty
  -l ARRAYLENGTH, --arraylength ARRAYLENGTH
                        the longest array to test the algorithms on
  -s STEP, --step STEP  how much to step the array size by
  -n NUMTIMES, --numtimes NUMTIMES
                        # of trials to run for each step
  -f FILEDESTINATION, --filedestination FILEDESTINATION
                        # of trials to run for each step
  -p, --python          Run on python scripts
  -c, --clang           Run on c scripts
```

*add a new algorithm*
Create a new C or Python file. The algorithm should live as a separate function, called from a function `wrapper`.
`wrapper` accepts array/list (lang dependent) and array/list length (int)
`wrapper` should return the execution time as a float

To time via C:
```
    lock_t start = clock();
    your_function(an_array, array_length);
    clock_t end = clock();
    float time_spent = (float)(end - start) / CLOCKS_PER_SEC;
```

To time via Python : 
```
    start = time.clock()
    your_function(list)
    end = time.clock()
```

**Output**
The script creates a (plotly)[https://plot.ly/python/] html file. 
