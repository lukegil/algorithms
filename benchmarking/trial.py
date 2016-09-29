import random
import array
import ctypes

class Trial(object):
    # To Dos -
    #       add support for characters, strings

    def __init__(self):
        pass

    def run_test(self, func, is_c = False):
        test_data = self.get_test_data()
        a_length = len(test_data)

        if (is_c):
            create_arr = ctypes.c_long * a_length
            c_arr = apply(create_arr, test_data)
            func.restype = ctypes.c_float
            self.set_elapsed_time(func(c_arr, a_length))
        else:
            self.set_elapsed_time(func(test_data, a_length))
    def get_elapsed_time(self):
        return self.elapsed_time

    def set_elapsed_time(self, time):
        # time - @type - int
        #      - @param - the time it took for the algorithm in the called
        #                 function to execute
        self.elapsed_time = time


    def get_test_data(self):
        return self.__test_data

    def set_test_data(self, random, obj_type, el_type, size, bound):
        # Sets an list/array (language dependent) of `size` with upper `bound`
        #
        # random   -  @type - bool
        #          -  @param - is test_data random or sorted
        # obj_type -  @type - Type object
        #          -  @param - should it be a list or array?
        # el_type  -  @type - Type object
        #          -  @param - the type of elements of the list. Only ints supported
        # size     -  @type - int
        #          -  @param - the number of elements of the list/array
        # bound    -  @type - int
        #          -  @param - number of bits of largest possible element
        #          --- e.g. char = 8; 100 = 7; obviously true bound is base2

        test_data = []

        if (random):
            func = self.get_random
        else:
            func = self.get_next
        for i in range(size):
            test_data.append(func(el_type, 2 ** bound - 1))

        if (obj_type is array.array):
            test_data = array.array('l', test_data)

        self.__test_data = test_data

    def get_random(self, obj_type, bound):
        if (obj_type is not int):
            raise TypeError("get_random only accepts integers")

        return random.randint(0, bound)

    def get_next(obj_type, bound):
        if (obj_type is not int):
            raise TypeError("get_random only accepts integers")

        try:
            self.next_element += 1
        except AttributeError:
            self.next_element = 0

        return self.next_element
