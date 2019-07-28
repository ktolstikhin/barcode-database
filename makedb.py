#!/usr/bin/env python3
'''Parse UhttBarcodeReference repository and create SQLite database from the
parsed records.
'''
import re
import csv
import sys
from argparse import ArgumentParser

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from models import ModelBase, Product


def get_args():
    parser = ArgumentParser(description=__doc__)

    parser.add_argument('-c', '--csv-files', nargs='+', required=True,
                        help='input csv files (multiple)')
    parser.add_argument('-d', '--database', default='barcodes.sqlite',
                        help='a path to output sqlite db file')

    return parser.parse_args()


def session(filename):
    engine = create_engine('sqlite:///{}'.format(filename))
    ModelBase.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    return Session()


def main():
    args = get_args()
    sess = session(args.database)
    regex = re.compile(r'\d{4}.csv$')
    n_files = len(args.csv_files)

    for i, fname in enumerate(args.csv_files, start=1):

        if not regex.search(fname):
            print('WARNING: Skip file', fname)
            continue

        print('[{i}/{n}] Parse {f} ... '.format(i=i, n=n_files, f=fname),
              flush=True, end='')

        with open(fname) as csv_file:
            reader = csv.reader(csv_file,
                                delimiter='\t',
                                quoting=csv.QUOTE_NONE)

            for row in reader:

                try:
                    product = Product(code=row[1],
                                      name=row[2],
                                      category=row[4],
                                      brand=row[6])
                except IndexError:
                    print('ERROR: Failed to parse', row, file=sys.stderr)
                else:
                    sess.add(product)

        try:
            sess.commit()
        except SQLAlchemyError as e:
            print('ERROR:', e, file=sys.stderr)
            sess.rollback()

        print('Done')


if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        pass

