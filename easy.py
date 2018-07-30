import time

def to_hash(array):
    """Function returns a hashed table w/ counts of an array of numbers"""
    my_hash = {}
    for i in array:
        if i in my_hash:
            my_hash[i] += 1
        else:
            my_hash[i] = 1
    return my_hash


def to_buckets(max_val, bin_count):
    """Function creates buckets of values in a range
    based on an input of maximum value and Number of Bins"""
    bin_size = max_val / bin_count
    x = 0
    bins = []

    while x < max_val:
        for i in range(bin_count):
            i = range(x, x+bin_size)
            bins.append(i)
            x += bin_size
    return bins


def my_hist(nums, max_val, bin_count):
    """This function creates a histogram from a list of integers.
            It first creates a hash table from input list, then creates buckets,
            then aggregates count by element, and finally prints a tuple of the histogram.

            Input requires: an array, the max value of bin range, and number of bins.
            Limits: # of buckets is limited to 4
    """
    # Create a dictionary of elements in array
    print "Creating Hash.."
    my_hash = to_hash(nums)

    # Create bins
    print "Creating Bins.."
    a, b, c, d = to_buckets(max_val,bin_count)
    print(type(a))

    # Build the histogram
    print "Building histogram.."
    a1 = b1 = c1 = d1 = 0

    print(time.clock())
    for j in my_hash:
        if j in a: a1 += my_hash[j]
        if j in b: b1 += my_hash[j]
        if j in c: c1 += my_hash[j]
        if j in d: d1 += my_hash[j]
    print(time.clock())
    hist_out = [["Bucket 1: ", a1], ["Bucket 2: ", b1], ["Bucket 3: ", c1], ["Bucket 4: ", d1]]

    print "\nHistogram:"
    for k, v in hist_out:
        print k, v

# Input
#array = [1, 5, 9, 10, 13, 18, 3, 5, 5, 7, 1]
array = range(10000)
# Execute
my_hist(array, 10000, 4)


