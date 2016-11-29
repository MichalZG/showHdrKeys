#!/usr/bin/env python

import sys
import os
import argparse
import warnings
import astropy.io.fits as fits

warnings.filterwarnings('ignore')

def load_keys(keys_file):
    try:
        with open(keys_file) as f:
            keys = [k.strip('\n') for k in f.readlines()]
    except (IOError, TypeError):
        print('Cannot open: {}'.format(keys_file))
        sys.exit(1)

    return keys


def open_hdr(file_to_open):
    hdr = fits.getheader(file_to_open)

    return hdr


def show_keys(name, keys, hdr):

    output_keys = []

    for key in keys:
        try:
            hdr_key = hdr[key]
            if not args.miss:
                output_keys.append([key, hdr_key])
        except KeyError:
            output_keys.append([key, 'Not found'])

    if len(output_keys) > 0:
        print('')
        print('File: {}'.format(name))

        for key, value in output_keys:
            print('{}: {}'.format(key, value))


def main():
    keys = load_keys(args.keys)
    for root, _, files in os.walk('.'):
        for name in files:
            if name.endswith(args.ext):
                hdr = open_hdr(os.path.join(root, name))
                show_keys(name, keys, hdr)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Show FITS hdr keys')
    parser.add_argument('-m', '--miss', action='store_true',
                        help='If set program will  show only missing keys')
    parser.add_argument('--keys', type=str, default=os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 'keys.txt'), 
        nargs='?', help='Dir to file with keys to show, '
                        'Default: keys.txt on program dir')
    parser.add_argument('--ext', type=str, default='.fits',
                        nargs='?', help='File to open, '
                                        'Default: .fits')
    args = parser.parse_args()

    main()

