n= int(raw_input("Enter No. of Test cases: ").strip())
arr = map(int,raw_input("Enter values saperated by space:").strip().split(" "))

if n == len(arr):
    srt_arr = sorted(arr)
    for i in srt_arr:
        print arr.index(i) + 1,
else:
    print "No. of Test cases and No. of values mismatched"
