#!/usr/bin/env python
# -*- coding: utf-8 -*-

import drmaa

def main():
    """Create a drmaa session and exit"""
    with drmaa.Session() as s:
        print('A session was started successfully')

if __name__ == "__main__":
    main()
