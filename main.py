import csv
import argparse
from decimal import Decimal
import simultaneous_alarms

DEFAULT_DATA_FILEPATH = "sample_metrics_2019.csv"
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--metric', required=True)
    parser.add_argument('-f', '--filepath', required=False, default=DEFAULT_DATA_FILEPATH)
    parser.add_argument('-v', '--verbose', required=False, action='store_true')
    args = parser.parse_args()

    desired_metric_name = args.metric
    data_filepath = args.filepath
    verbose_mode = args.verbose

    # Given a specific metric name return all times when that metric and any other metric are in alarm simultaneously.
    alarm_times = simultaneous_alarms.get_simultaneous_alarms(data_filepath, desired_metric_name, verbose_mode=verbose_mode)
    alarm_time_moments = []
    for alarm_time in alarm_times:
        for alarm_time_key, _ in alarm_time.items():
            alarm_time_moments.append(alarm_time_key)
    print(
        f"Simultaneous alarm times for metric {desired_metric_name}: {alarm_time_moments}")

    # BONUS 1: Also return the time when the most metrics are in alarm.
    max_time = 0
    max_value = 0
    for alarm in alarm_times:
        alarm_time = list(alarm.keys())[0]
        alarm_value = list(alarm.values())[0]
        if alarm_value > max_value:
            max_time = alarm_time
            max_value = alarm_value
    print(
        f"Maximum alarm time for metric {desired_metric_name} occurs at time {max_time} with {max_value} simultaneous alarms.")

if __name__ == "__main__":
    main()
