##  RFC Re-Flow

![pic1](https://github.com/topranks/rfc_reflow/raw/main/diagram.png)

I got nerd-sniped doing this by someone asking how to view RFCs on their Kindle.

Trying to convert with Calibre I found the fixed-formatting of the RFCs problematic.  Specifically paragraphs have hard line breaks in the RFCs, both in HTML and TXT form, which make things look ugly as the e-reader can't fit a whole line without breaking it again.  So I made this script to download TXT RFCs and - as best as possible - consolidate paragraphs into a single line in the output file.

Tbh if you set up calibre right it will also format the 

## Running the script 

If you want to use the script to download RFCs just run as follows:
```
./rfc_reflow.py -r rfc7433
```

It will download rfc7433.txt to the local directory.

## Calibre converstion

Whether downloading the RFCs direct or using the script Calibre is the key to getting acceptable view on an e-reader.  RFCs are specifically designed for a certain width in terms of characters, however, and diagrams/tables/figures will never display perfectly if you've limited width such as on most e-readers.

With that said for the calibre conversion about the best I've found to use AZW3 output format (for Kindle), with the following converstion settings:
```
Look & Feel:
  Fonts:
    - embed font family - using a serif, mono font, on my system Nimbus Mono worked well
    - embed all fonts in document

  Text:
    - Text justification: Justify text

Hueristic processing: off

Page setup:
  Output: set for your e-reader
  Input: Default profile

Text Input:
  Paragraph: auto or off
  Fommatting style: auto or off
```

For this last one setting to 'off' preserves any ascii-based diagramns, like packet strucutre ones, as the script produces.  But on my reader most wouldn't fit on a line, and the 'auto', while it messes up these a litte, actually made it more readable.


Fo
