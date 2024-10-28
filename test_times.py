from times import compute_overlap_time,time_range



def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [("2010-01-12 10:30:00", "2010-01-12 10:36:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]

    assert result == expected




def test_given_nooverlap_input():
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
    expected = []
    assert result == expected


#test_given_input()
#test_given_nooverlap_input()
#test_given_equal_input()
test_given_large_input()