import math
import os
import random
import re
import sys



def birthdayCakeCandles(candles):
    Max_candles = max(candles)
    count_max_candles = candles.count(Max_candles)
    return count_max_candles

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
