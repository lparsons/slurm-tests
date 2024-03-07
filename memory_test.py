#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import psutil

PROCESS = psutil.Process(os.getpid())
KILO = 10 ** 3
MEGA = 10 ** 6
GIGA = 10 ** 9
MEGA_STR = ' ' * MEGA
GIGA_STR = ' ' * GIGA


def pmem():
    mem = psutil.virtual_memory()
    tot, avail, used, free = mem.total / MEGA, mem.available / MEGA, mem.used / MEGA, mem.free / MEGA
    proc = PROCESS.memory_info().rss / MEGA
    print('process = %s total = %s avail = %s used = %s free = %s percent = %s'
          % (proc, tot, avail, used, free, mem.percent))


def alloc_max_array():
    i = 0
    ar = []
    while True:
        try:
            # ar.append(MEGA_STR)  # no copy if reusing the same string!
            ar.append(GIGA_STR + str(i))
            if i % 1 == 0:
                pmem()
        except MemoryError:
            break
        i += 1
    max_i = i - 1
    print 'maximum array allocation:', max_i
    pmem()


pmem()
alloc_max_array()
