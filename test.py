import simultaneous_alarms

DEFAULT_DATA_FILEPATH = "sample_metrics_2019.csv"

def test_1():
    """
    Test metric 1 results are correct
    """
    expected_list = [{12: 1}, {13: 3}]
    alarm_times = simultaneous_alarms.get_simultaneous_alarms(DEFAULT_DATA_FILEPATH, "Metric 1")

    assert len(expected_list) == len(alarm_times), "Returned list is of unexpected length!"
    for expected_alarm, actual_alarm in zip(expected_list, alarm_times):
        assert expected_alarm == actual_alarm, "Found incorrect alarm!"


def test_2():
    """
    Test metric 2 results are correct
    """
    expected_list = [{12: 1}, {13: 3}, {14: 4}, {17: 1}, {18: 2}, {19: 2}]
    alarm_times = simultaneous_alarms.get_simultaneous_alarms(
        DEFAULT_DATA_FILEPATH, "Metric 2")

    assert len(expected_list) == len(
        alarm_times), "Returned list is of unexpected length!"
    for expected_alarm, actual_alarm in zip(expected_list, alarm_times):
        assert expected_alarm == actual_alarm, "Found incorrect alarm!"


def test_3():
    """
    Test metric 3 results are correct
    """
    expected_list = [{7: 1}, {12: 1}, {13: 3}, {14: 4}, {18: 2}, {19: 2}]
    alarm_times = simultaneous_alarms.get_simultaneous_alarms(
        DEFAULT_DATA_FILEPATH, "Metric 3")

    assert len(expected_list) == len(
        alarm_times), "Returned list is of unexpected length!"
    for expected_alarm, actual_alarm in zip(expected_list, alarm_times):
        assert expected_alarm == actual_alarm, "Found incorrect alarm!"

def test_4():
    """
    Test metric 4 results are correct
    """
    expected_list = [{7: 1}, {13: 3}, {17: 1}]
    alarm_times = simultaneous_alarms.get_simultaneous_alarms(
        DEFAULT_DATA_FILEPATH, "Metric 4")

    assert len(expected_list) == len(
        alarm_times), "Returned list is of unexpected length!"
    for expected_alarm, actual_alarm in zip(expected_list, alarm_times):
        assert expected_alarm == actual_alarm, "Found incorrect alarm!"


def test_5():
    """
    Test metric 5 results are correct
    """
    expected_list = []
    alarm_times = simultaneous_alarms.get_simultaneous_alarms(
        DEFAULT_DATA_FILEPATH, "Metric 5")

    assert len(expected_list) == len(
        alarm_times), "Returned list is of unexpected length!"
    for expected_alarm, actual_alarm in zip(expected_list, alarm_times):
        assert expected_alarm == actual_alarm, "Found incorrect alarm!"

if __name__ == "__main__":
    print("Running test 1...")
    test_1()
    print("Running test 2...")
    test_2()
    print("Running test 3...")
    test_3()
    print("Running test 4...")
    test_4()
    print("Running test 5...")
    test_5()
    print("All tests have passed!")