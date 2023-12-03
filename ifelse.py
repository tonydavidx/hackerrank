#!/bin/python3

import math
import os
import random
import re
import sys

n = int(input().strip())

if n % 2 != 0:
    print('Weird')
else:
    if (n % 2) == 0 and n in range(1, 6):
        print('Not Weird')
    else:
        if (n % 2) == 0 and n in range(5, 21):
            print('Weird')
        else:
            if (n % 2) == 0 and n > 21:
                print('Not Weird')
