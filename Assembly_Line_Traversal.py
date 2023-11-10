def assembly_line_scheduling(a, t, e, x):
    n = len(a[0])  # Number of stations on each line
    f = [[0] * n for _ in range(2)]

    # Initialization
    f[0][0] = e[0] + a[0][0]
    f[1][0] = e[1] + a[1][0]

    # Dynamic Programming
    for j in range(1, n):
        # Line 1
        f[0][j] = min(f[0][j-1] + a[0][j], f[1][j-1] + t[1][j-1] + a[0][j])

        # Line 2
        f[1][j] = min(f[1][j-1] + a[1][j], f[0][j-1] + t[0][j-1] + a[1][j])

    # Finalization
    f[0][-1] += x[0]
    f[1][-1] += x[1]

    # Return the minimum time
    return min(f[0][-1], f[1][-1])

# Example usage:
a = [
    [7, 9, 3, 4, 8],
    [8, 5, 6, 4, 5]
]
t = [
    [2, 3, 1, 3],
    [2, 1, 2, 2]
]
e = [2, 4]
x = [3, 6]

min_time = assembly_line_scheduling(a, t, e, x)
print(f"The minimum time to traverse the assembly lines is: {min_time}")
