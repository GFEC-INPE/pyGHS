# pyGHS

## Introduction
Recently, based on the operation of the box counting algorithm, the measure of the GHS separation parameter was proposed based only on the geometric properties of the histograms.
It is a measure calculated straightforward on the histograms files that maximizes the mutual separation considering the quantitative balance between areas and heights for typical binomial patterns.

## Required Libraries
The following libraries are required to run this operator:

* numpy
* pandas

## Benchmark
We selected a benchmark for 
```
python ghs.py benchmark/AA/d1.txt benchmark/AA/d2.txt
```
In this example the metric is for the following distribution:
![Benchmark](benchmark/distribution.png)

