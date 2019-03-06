
# The script finds out how many pages are there in each pdf file
# in a given location. And then writes this information to a csv file.
# Each line in a csv file consist of filename and number of pages

import PyPDF2
import sys
import csv
import os


def get_page_number(filename):
    """
    Function takes a filename (including path) of a pdf file and
    calculates number of pages in it
    :param filename:
    :return number of pages in a given pdf file:
    """
    pdf = PyPDF2.PdfFileReader(open(filename, 'rb'))
    return pdf.getNumPages()


def scroll_files(location):
    """
    Function checks each file in a given directory.
    For pdf files calculates number of pages and stores the
    information in a list
    :param location:
    :return list of filenames and number of pages en each file:
    """
    info = list()
    for filename in os.listdir(location):
        if filename.endswith('.pdf'):
            file_path = os.path.join(location, filename)
            page_number = get_page_number(file_path)
            info.append((filename, page_number))

    return info


def write_to_csv(info):
    """
    Writes each element of a list as a row to a csv file
    :param info:
    :return:
    """
    with open('page_number.csv', 'w') as out:
        csv_out = csv.writer(out)
        for row in info:
            csv_out.writerow(row)


def main(location):
    """
    Main function which initiates calculating number of pages
    for each file in a given location
    :param location:
    :return:
    """
    info = scroll_files(location)
    write_to_csv(info)


if __name__ == '__main__':
    args = sys.argv
    location = args[1]
    main(location)
