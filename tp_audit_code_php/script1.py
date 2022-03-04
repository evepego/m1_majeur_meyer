from collections import defaultdict
import glob
from itertools import count
from unittest import result


http_requests = ['$_GET', '$_POST', '$_REQUEST']

dir = ['./wp-mobile-detector/*.php', './wp-mobile-detector/*/*.php', './wp-mobile-detector/*/*/*.php', './wp-mobile-detector/*/*/*/*.php', './wp-mobile-detector/*/*/*/*/*.php', './wp-mobile-detector/*/*/*/*/*/*.php']

def occurence1(string_list):
    results =  defaultdict(int)
    count = 0
    for d in dir:
        for file_name in glob.iglob(d):
            with open(file_name) as input_file:
                for line in input_file:
                    for s in string_list:
                        if s in line:
                            results[s] += 1
                            count += 1
                            print(file_name)
    return results, count

print(occurence1(http_requests), count)