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
        binary_address = bin(int(hexAddress, 16))[2:].zfill(size)
        rows.append(['0x'+hexAddress,
                     ' '.join([binary_address[i:i+4] for i in range(0, len(binary_address), 4)])])

    table.add_rows(rows)
    print table.draw()

if __name__ == '__main__':
    main()