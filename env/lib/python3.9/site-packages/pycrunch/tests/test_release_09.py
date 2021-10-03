from time import sleep

from pycrunch.insights import trace


def test_trace_dict_variable():
    a = 2
    b = 3
    sleep(0.01)
    x = a + b
    trace(some_dictionary=dict(a=a, b=b, sum=x))
    trace(can_trace_a_lot=True)












