import csv
from decimal import Decimal

def get_simultaneous_alarms(data_filepath, desired_metric_name, verbose_mode=False):
    """Detect simultaneous alarms.

    Arguments:
    data_filepath -- path to metrics file
    desired_metric_name -- metric of which to detect simultaneous alarms
    verbose_mode -- prints metrics data tables

    Returns:
    simultaneous_alarm_times -- a list of dicts of form [{alarm time: alarm count}, ...]
    """
    with open(data_filepath, newline='') as csvfile:
        metrics_data = list(csv.reader(csvfile))

    if verbose_mode:
        print("\nLoaded metric data:")
        for row in metrics_data:
            print(row, "\n")

    # Step 1: Calculate average values for each metric
    # TLDR: Average each metric and store averages in a {metric_name: average} dictionary
    #
    # Runtime: O(n*m) where n = number of metrics, m = number of datapoints (times)
    metrics_averages = {}
    for row in metrics_data[1:]:
        metric_name = row[0]
        avg_value = 0
        for datapoint in row[1:]:
            avg_value += Decimal(datapoint)
        avg_value = avg_value/(len(row)-1)
        metrics_averages[metric_name] = avg_value

    if verbose_mode:
        print("\nMetric average values:")
        for k, v in metrics_averages.items():
            print(k, v)

    # Step 2: Detect and store times that value exceeds threshold (is in alarm)
    # TLDR: Copy the original array and store 1/0 values at the datapoints if they exceed/do not exceed threshold
    #
    # Runtime: O(n*m) where n = number of metrics, m = number of datapoints (times)
    metric_alarms = metrics_data.copy()
    for row in metric_alarms[1:]:
        metric_name = row[0]
        alarm_threshold = metrics_averages[metric_name]*Decimal(1.1)
        for time, datapoint in enumerate(row[1:]):
            if Decimal(datapoint) > alarm_threshold:
                row[time+1] = 1
            else:
                row[time+1] = 0
    # Step 3: Sum the number of alarms at every time point
    # TLDR: Add a new row to the metric_alarms array called Total and in it store the sum of each column
    #
    # Runtime: O(n*m) where n = number of metrics, m = number of datapoints (times)
    num_rows = len(metric_alarms)
    num_cols = len(metric_alarms[0])
    totals_list = [0]*num_cols
    totals_list[0] = 'Total'
    for col_index in range(num_cols)[1:]:
        for row_index in range(num_rows)[1:]:
            totals_list[col_index] += metric_alarms[row_index][col_index]
    metric_alarms.append(totals_list)
    if verbose_mode:
        print("\nMetric alarm counts at each time:")
        for row in metric_alarms:
            print(row, "\n")

    # Step 4: Given a specific metric name return all times when that metric and any other metric are in alarm simultaneously.
    # TLDR: Check the total row each time that the metric > 1
    #
    # Runtime: O(m) where m = number of datapoints (times)
    simultaneous_alarm_times = []
    for row in metric_alarms:
        if row[0] == desired_metric_name:
            for col_index, value in enumerate(row[1:]):
                if value > 0 and metric_alarms[-1][col_index+1] > 1:
                    simultaneous_alarm_times.append(
                        {col_index-1: metric_alarms[-1][col_index]})
            return simultaneous_alarm_times
