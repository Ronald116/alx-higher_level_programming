#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
  """Adds two tuples.

  Args:
    tuple_a: The first tuple.
    tuple_b: The second tuple.

  Returns:
    A tuple with the sum of the corresponding elements of the two tuples.
  """

  if len(tuple_a) < 2:
    tuple_a = tuple_a + (0, 0)
  if len(tuple_b) < 2:
    tuple_b = tuple_b + (0, 0)

  return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

