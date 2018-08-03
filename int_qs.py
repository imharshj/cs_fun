#  Enter your code here. Read input from STDIN. Print output to STDOUT

# [0,3,5,9,10,15,12,8,9,3,5,2,7,11,20,12,14,17,...]

# [0-4]   : ....
# [5-10]  : .......
# [11-15] : .....
# [16-20] : ..


def my_hist(array):
    ans = profiler(array)
    print hist_builder(ans)


def profiler(array):
    my_hash = {}
    for i in array:
        if i in my_hash:
            my_hash[i] += 1
        else:
            my_hash[i] = 1

    return my_hash


def hist_builder(my_hash):
    # Buckets
    a = range(5)
    b = range(5, 10)
    c = range(10, 15)
    d = range(15, 20)

    a_count = b_count = c_count = d_count = 0
    for key, value in my_hash.items():
        if key in a:
            a_count += value
        if key in b:
            b_count += value
        if key in c:
            c_count += value
        if key in d:
            d_count += value

    return a_count, b_count, c_count, d_count


# Execute
my_hist(range(0, 20, 2))
