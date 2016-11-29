# !/usr/bin/python

import sys
import os
import argparse
import astropy.io.fits as fits


def load_keys(keys_file):
    try:
        with open(keys_file) as f:
            keys = [k.strip('\n') for k in f.readlines()]
    except IOError:
        print('Cannot open {}'.format(keys_file))
        sys.exit(1)

    return keys


def open_hdr(file_to_open):
    hdr = fits.getheader(file_to_open)

    return hdr


def show_keys(name, keys, hdr):

    print('File :{}'.format(name))

    for key in keys:
        try:
            print(key, hdr[key])
        except KeyError:
            print(key, 'Not Found')


def main():
    keys = load_keys(args.keys)
    for root, _, files in os.walk('.'):
        for name in files:
            if name.endswith(args.ext):
                hdr = open_hdr(os.path.join(root, name))
                show_keys(name, keys, hdr)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Show FITS hdr keys')
    parser = add_argument('-k', '--keys', type=str, const=os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 'keys.txt'), 
        nargs='?', help='Dir to file with keys to show, '
                        'Default: keys.txt on program dir')
    parser = add_argument('-e', '--ext', type=str, const='.fits',
                          nargs='?', help='File to open extencion, '
                                          'Default: .fits')
    args = parser.parse_args()

    main()

