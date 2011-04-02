#!/usr/bin/python

from nose.tools import assert_equal, assert_raises
from StringIO import StringIO
from snapper_chain import decimal_to_binary, on_or_off, process_input

INPUT = """5
1 0
1 1
4 0
4 47
5 41
"""

OUTPUT = """Case #1: OFF
Case #2: ON
Case #3: OFF
Case #4: ON
Case #5: OFF
"""

def test_decimal_to_binary():
    cases = [(10, '1010'), (0, '0')]

    for case in cases:
        assert_equal(decimal_to_binary(case[0]), case[1])

    assert_raises(ValueError, decimal_to_binary, -1)

def test_on_or_off():
    on = 'ON'
    off = 'OFF'
    cases = [([1, 0], off),
        ([1, 1], on), ([4, 0], off), ([4, 47], on), ([5, 41], off)]

    for case in cases:
        assert_equal(on_or_off(*case[0]), case[1])

def test_process_intput():
    input = StringIO(INPUT)
    output = StringIO()
    process_input(input, output)
    output_value = output.getvalue()
    input.close()
    output.close()

    assert_equal(output_value, OUTPUT)
 
