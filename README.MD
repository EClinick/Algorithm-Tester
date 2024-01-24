# ALGORITHM TESTER
    This is a simple algorithm tester that can be used to test the performance of different algorithms.
    It filters the best percentages with the corresponding timeframes.

    You can currently test the following variables:
    - Ticker
    - Timeframe
    - Initial Capital
    - Trade size (amount of shares bought at a time)
# Down Side
    - Currently have to manually do the reCAPTCHA

# HOW TO GET SET UP
    - 'pip install -r requirements.txt'
    - 'python main.py <ticker> <timeframe_range> <initial_amount> <trade_size> <debug(T/F)>'
    - Put Username and Password into the .env file following the .env_example
    - Example:
        python main.py AMD 80 1000 2 T

        The outcome (removing the debugging statements):


                Timeframe: 3, Percent: 43.74
                Timeframe: 4, Percent: 42.46
                Timeframe: 5, Percent: 41.06
                Timeframe: 9, Percent: 36.59
                Timeframe: 19, Percent: 27.44
                Timeframe: 17, Percent: 26.95
                Timeframe: 18, Percent: 26.71
                Timeframe: 29, Percent: 26.69
                Timeframe: 13, Percent: 26.58
                Timeframe: 2, Percent: 26.51
                Timeframe: 31, Percent: 26.5
                Timeframe: 24, Percent: 26.39
                Timeframe: 34, Percent: 25.46
                Timeframe: 71, Percent: 24.97
                Timeframe: 33, Percent: 24.74
                Timeframe: 36, Percent: 24.73
                Timeframe: 21, Percent: 24.29
                Timeframe: 6, Percent: 24.08
                Timeframe: 23, Percent: 23.65
                Timeframe: 50, Percent: 23.59
                Timeframe: 27, Percent: 23.28
                Timeframe: 28, Percent: 23.11
                Timeframe: 73, Percent: 22.81
                Timeframe: 42, Percent: 22.75
                Timeframe: 52, Percent: 22.68
                Timeframe: 49, Percent: 22.01
                Timeframe: 20, Percent: 21.84
                Timeframe: 40, Percent: 21.83
                Timeframe: 22, Percent: 21.71
                Timeframe: 53, Percent: 21.55
                Timeframe: 37, Percent: 20.98
                Timeframe: 72, Percent: 20.93
                Timeframe: 30, Percent: 20.81
                Timeframe: 25, Percent: 20.29
                Timeframe: 61, Percent: 19.96
                Timeframe: 32, Percent: 19.81
                Timeframe: 59, Percent: 19.28
                Timeframe: 51, Percent: 19.16
                Timeframe: 16, Percent: 19.13
                Timeframe: 41, Percent: 18.72
                Timeframe: 70, Percent: 18.66
                Timeframe: 39, Percent: 18.26
                Timeframe: 35, Percent: 18.12
                Timeframe: 62, Percent: 18.07
                Timeframe: 8, Percent: 17.78
                Timeframe: 7, Percent: 17.41
                Timeframe: 63, Percent: 17.3
                Timeframe: 11, Percent: 17.2
                Timeframe: 38, Percent: 17.06
                Timeframe: 12, Percent: 16.87
                Timeframe: 57, Percent: 16.63
                Timeframe: 56, Percent: 16.61
                Timeframe: 14, Percent: 16.54
                Timeframe: 60, Percent: 16.37
                Timeframe: 26, Percent: 15.96
                Timeframe: 47, Percent: 15.82
                Timeframe: 67, Percent: 15.77
                Timeframe: 0, Percent: 15.24
                Timeframe: 74, Percent: 14.88
                Timeframe: 15, Percent: 14.27
                Timeframe: 46, Percent: 13.38
                Timeframe: 10, Percent: 13.22
                Timeframe: 66, Percent: 12.83
                Timeframe: 79, Percent: 12.71
                Timeframe: 58, Percent: 12.22
                Timeframe: 54, Percent: 11.96
                Timeframe: 75, Percent: 11.6
                Timeframe: 43, Percent: 11.48
                Timeframe: 45, Percent: 11.21
                Timeframe: 44, Percent: 9.19
                Timeframe: 69, Percent: 7.6
                Timeframe: 55, Percent: 5.8
                Timeframe: 48, Percent: 5.71
                Timeframe: 65, Percent: 4.48
                Timeframe: 76, Percent: 4.45
                Timeframe: 78, Percent: 3.42
                Timeframe: 68, Percent: 3.01
                Timeframe: 77, Percent: 1.85
                Timeframe: 64, Percent: 1.68
                Timeframe: 1, Percent: 0.73
