from times import time_range, compute_overlap_time

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    result = compute_overlap_time(large, short) 
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_intervals():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 60)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    st=[]
    en=[]
    for start1, end1 in large:
        st.append(start1)
        en.append(end1)
    for i in range(len(st)-1):
        assert en[i] != st[i+1]

    st=[]
    en=[]
    for start1, end1 in short:
        st.append(start1)
        en.append(end1)
    for i in range(len(st)-1):
        assert en[i] != st[i+1]

            
def test_notoverlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 13:30:00", "2010-01-12 13:45:00")

    result = compute_overlap_time(large, short) 
    expected = []
    assert result == expected


def test_exact_end_start_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    short = time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00")
    expected = []
    assert compute_overlap_time(large, short) == expected



