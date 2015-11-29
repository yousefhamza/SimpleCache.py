__author__ = 'yousefhamza'
from texttable import Texttable

hexByteAddresses = [
    "0054",
    "0298",
    "0324",
    "023C",
    "00F4",
    "0298",
    "00F8",
    "0214",
    "01BC",
    "023C",
    "0240",
    "00F4"
]
def main():
    table = Texttable()
    table.set_deco(Texttable.HEADER)
    table.set_cols_dtype(['t', 't'])

    rows = [['Hexadecimal', 'Binary']]
    for hexAddress in hexByteAddresses:
        size = len(hexAddress) * 4
        rows.append(['0x'+hexAddress, bin(int(hexAddress, 16))[2:].zfill(size)])

    table.add_rows(rows)
    print table.draw()

if __name__ == '__main__':
    main()