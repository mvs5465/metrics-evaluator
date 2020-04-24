# metrics-evaluator

This is a metrics evaluator Python script.

## Requirements

- Python3
- A data file matching the format of the sample_metrics_2019.csv file
    - Must have a Time row at the top
    - Must have the Time row be indexed starting at 0
    - Must have the Time row increment by exactly 1
    - Must have the first column be the metric name

## Usage

This script works as a typical Python script as `python main.py [arguments]` and takes the following command line arguments:

| Argument     | Full Flag    | Short Flag | Required | Default Value           | Description                                                                       |
|--------------|--------------|------------|----------|-------------------------|-----------------------------------------------------------------------------------|
| Metric Name  | --metricname | -m         | True     | (n/a)                   | The name of the metric you wish to evaluate for simultaneous alarm events         |
| File Path    | --filepath   | -f         | False    | sample_metrics_2019.csv | The local or relative file path containing your metric data in the correct format |
| Verbose Mode | --verbose    | -v         | False    | False                   | Display the data as it is being manipulated and analyzed                          |

For example, you may run the script `python3 main.py -m "Metric 5"` to evaluate and return an analysis of the metric called "Metric 5".

## Testing

This repository includes a sample test.py script that may be run as `python test.py`.

Example:

```
$ python3 test.py
Running test 1...
Running test 2...
Running test 3...
Running test 4...
Running test 5...
All tests have passed!
```

## License

This project is licensed under the Apache 2.0 License.