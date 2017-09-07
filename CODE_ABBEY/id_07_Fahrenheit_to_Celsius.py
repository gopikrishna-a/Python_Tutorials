"""
Fahrenheit to Celsius conversion:

0 °F = -17.77778 °C

T(°C) = (T(°F) - 32) × 5/9
or
T(°C) = (T(°F) - 32) / (9/5)
or
T(°C) = (T(°F) - 32) / 1.8

Celsius to Fahrenheit conversion:

0 °C = 32 °F

T(°F) = T(°C) × 9/5 + 32
or
T(°F) = T(°C) × 1.8 + 32

"""

arr = map(float,raw_input("Enter no. of test cases followed by temperatur in Celsius:").strip().split(" "))
l = []
if arr[0] == (len(arr) - 1):
    arr = arr[1:]
    for i in arr:
        fh_temp = (i - 32) / 1.8
        fh_temp = int(round(fh_temp))
        l.append(fh_temp)
    for i in l:
        print i,
else:
    print "No. of test cases and No. of temperatures mismatched"
    
