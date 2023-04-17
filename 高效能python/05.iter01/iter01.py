#
#
def fibonacci_list(num_items):
    numbers=[]
    a,b =0,1
    while len(numbers) < num_items:
        numbers.append(a)
        a,b = b,a+b
    return numbers

def fibonacci_gen(num_items):
    a,b = 0,1
    while num_items:
        yield a
        a,b = b , a+b
        num_items-=1


def test_fibonacci_list():
    '''
        >>> %timeit test_fibonacci_list()
        >>> %memit  test_fibonacci_list()
    '''
    for i in fibonacci_list(100_000):
        pass

test_fibonacci_list()