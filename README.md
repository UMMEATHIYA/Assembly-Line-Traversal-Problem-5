# Assembly Line Scheduling

This repository contains a Python implementation of the Assembly Line Scheduling algorithm using dynamic programming. The Assembly Line Scheduling problem involves finding the most efficient way to move through a series of assembly lines in a factory.

## Table of Contents
- [Introduction](#introduction)
- [Usage](#usage)
- [Input Parameters](#input-parameters)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Assembly Line Scheduling algorithm optimizes the traversal of a series of assembly lines, minimizing the time required to move from the entry to the exit points.

## Usage

To use this implementation, simply clone the repository and run the Python code provided. You can customize the input parameters for your specific use case.

## Input Parameters

The program takes the following input parameters:

- `a`: Processing times for each station on the assembly lines.
- `t`: Transfer times between stations on different assembly lines.
- `e`: Entry times for each assembly line.
- `x`: Exit times for each assembly line.

## Example

```python
a = [
    [7, 9, 3, 4, 8],
    [8, 5, 6, 4, 5]
]
t = [
    [2, 3, 1, 3],
    [2, 1, 2, 2]
]
e = [2, 4]
x = [3, 2]

min_time = assembly_line_scheduling(a, t, e, x)
print(f"The minimum time to traverse the assembly lines is: {min_time}")
