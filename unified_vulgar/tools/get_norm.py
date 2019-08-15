#!/usr/bin/env python
import argparse
import sys
import numpy as np


def get_prob(fn, column):
    lines = open(fn, 'r').readlines()
    probs = [float(l.strip().split()[column]) for l in lines]
    probs = sorted(probs, reverse=True)
    return np.array(probs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--random", default='huoshan_random_pred.list')
    parser.add_argument("--positive", default='weapon_pred.list')
    parser.add_argument("--prob_column", default=3, type=int)
    args = parser.parse_args()


    prob_column = args.prob_column - 1
    random = get_prob(args.random, prob_column)
    pos = get_prob(args.positive, prob_column)

    for percent in range(1, 51):
        p = percent * 0.001
        thresh = random[int(p * len(random))]
        print '{}\t{}\t{}'.format(p, thresh, np.sum(pos >= thresh) / float(len(pos)))