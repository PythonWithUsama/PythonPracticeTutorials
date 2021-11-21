from functools import reduce
# Use map to print the square of each numbers rounded
# to three decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

# Use filter to print only the names that are less than
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
my_numbers = [4, 6, 8, 10, 2]
if __name__ == '__main__':
    sq = list(map(lambda x:round(x*x,3), my_floats))
    print(sq)
    name = list(filter(lambda n:len(n)<=7,my_names))
    print(name)
    product_N = reduce(lambda x,y:x*y,my_numbers)
    print(product_N)