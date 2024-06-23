#!/usr/bin/python3

import re
import requests
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description='Download RFC text file and re-flow paragraphs for e-reader export')
    parser.add_argument('-r', '--rfc', help='RFC to get, i.e. rfc1925', required=True)
    args=parser.parse_args()

    filename = f"{args.rfc.lower()}.txt"
    url = f"https://www.rfc-editor.org/rfc/{filename}"
    rfc = get_http(url).text
    rfc_header = f"RFC {args.rfc.lower().replace('rfc', '')}"
    outfile = open(filename, 'w')

    paragraph = ""
    blanks = 0
    title_done = False
    for line in rfc.split('\n'):
        # Only outfile.write the page titles the first time they appear
        if re.match('.*\[Page ', line.strip()) or re.match(rfc_header, line.strip()):
            if not title_done:
                outfile.write(f"{line}\n")
                title_done = True
            continue

        # Table of contents lines we try to catch too
        if re.match("^[0-9].*[0-9]$", line.strip()) and "." in line:
            outfile.write(f"{line}\n")
            continue

        if len(line) > 60:
            blanks = 0
            # we try to keep line breaks in block diagrams (packet struct etc.)
            if "|" in line or "+" in line:
                if paragraph:
                    outfile.write(f"{paragraph}\n")
                    paragraph = ""
                outfile.write(f"{line.strip()}\n")
            else:
                # We assume this line is part of paragraph, which we want
                # to consolidate onto a single line so e-reader can reflow
                paragraph += f" {line.strip()}"
        else:
            if not re.match('^$', line.strip()):
                # We have a short line, but not a blank one
                blanks = 0
                if paragraph:
                    # We have paragraph data, it's likely the last line of one
                    paragraph += f" {line.strip()}"
                    outfile.write(f"{paragraph}\n")
                    paragraph = ""
                else:
                    # Probably somthing else, diagram etc.
                    outfile.write(f"{line.strip()}\n")
            else:
                # We have a blank line
                if paragraph:
                    outfile.write(f"{paragraph}\n")
                    paragraph = ""
                # Print the blank line but limit to two in a row
                if blanks <= 2:
                    outfile.write('\n')
                    blanks += 1

    outfile.close()

def get_http(url):
    try:
        response = requests.get(url)
    except Exception as e:
        print(f"Error connecting to {url}:\n{e}\n")
        sys.exit(1)

    if response.status_code == requests.codes.ok:
        return response
    else:
        print(f"HTTP Error getting {url}\nReturn code {response.status_code}:\n\n{response.text}")
        sys.exit(1)

if __name__ == "__main__":
    main()
