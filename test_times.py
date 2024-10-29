from times import compute_overlap_time,time_range
from pytest import raises
from times import compute_overlap_time, time_range
import pytest


def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [("2010-01-12 10:30:00", "2010-01-12 10:36:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]

    assert result == expected




"""def test_given_nooverlap_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 12:10:00", "2010-01-12 12:40:00")
    result = compute_overlap_time(large, short)
 #   for start, end in result:
  #      if(start>=end):
   #         raise ValueError("start time cannot larger than end")
    expected = []
    assert result == expected

def test_given_equal_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 12:00:00", "2010-01-12 12:40:00")
    result = compute_overlap_time(large, short)
    expected = []
    assert result == expected


def test_given_large_input():
    large = time_range("2010-01-12 13:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 12:00:00", "2010-01-12 12:40:00")
    result = compute_overlap_time(large, short)

    #message="11"
    #with pytest.raises(ValueError,message):
     #   time_range("2010-01-12 13:00:00", "2010-01-12 12:00:00")

#test_given_input()
#test_given_nooverlap_input()
#test_given_equal_input()
#test_given_large_input()

"""


test_given_input()

"""

@pytest.mark.parametrize("first_range, second_range, expected_overlap",

#test given input
[(time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
  time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
  [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]),
#test nooverlap_input
  (time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00"),
  time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00", 2, 60),
  []),
#test more inputs
  (time_range("2010-01-12 10:00:00", "2010-01-12 13:00:00", 3, 900),
  time_range("2010-01-12 10:40:00", "2010-01-12 11:20:00", 2, 120),
  [("2010-01-12 10:40:00","2010-01-12 10:50:00"), ("2010-01-12 11:05:00", "2010-01-12 11:20:00")]),
  #test equal input
  (time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00"),
  time_range("2010-01-12 11:00:00", "2010-01-12 12:45:00"),
  [])
])
def test_time_range_overlap(first_range, second_range, expected_overlap):
    assert compute_overlap_time(first_range, second_range) == expected_overlap
"""