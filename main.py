#!/usr/bin/env python
# -*-coding:utf-8 -*-
import random
filename = "test.log"
random_string = random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()')
with open(filename, 'a') as f:
    f.write(random_string)
