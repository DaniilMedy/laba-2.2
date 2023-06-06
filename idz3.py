#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    words_per_day = 5
    total_words = 0

    for day in range(1, 10):
        total_words += words_per_day
        words_per_day += 2

    total_words += words_per_day

    print(total_words)

