from __future__ import with_statement # Until Python 2.6
"""
Parse latex equations in markdown file.
"""

"""
Author:
    doubletony <doubletony@gmail.com>
    URL: http://www.doubletony.com

Revision History:
    2012/06/26 - Initial version

TODO:
    - Make handing equations cross over more than one lines.
---

Licensed under the MIT License:

Copyright (c) 2012 doubletony <doubletony@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
IN THE SOFTWARE.
"""


import latexmath2png

PARSED_PREFIX = "_parsed_"
MATH_TOKEN = '$$$'
MATH_IMG_PATH = './img/'
MATH_IMG_PREFIX = '_math_'
MATH_IMG_SIZE = 2

def extractEqs(text):
    eqs = text.split(MATH_TOKEN)
    return eqs[1::2]

def extractText(text):
    ts = text.split(MATH_TOKEN)
    return ts[::2]

def getImgMarkdown(idx):
    return "![](" + MATH_IMG_PATH + MATH_IMG_PREFIX + str(idx+1)+".png)"

# parse tex equation in the markdown file
def parse(filename):
    eqs_all = []
    eqs_count = 0
    fileOriginal = open(filename)
    fileParsed = open(PARSED_PREFIX+filename, 'w+')
    ineqa = False
    for line in fileOriginal:
        if MATH_TOKEN in line:
            # assume all $$$ are paired
            eqs_all = eqs_all + extractEqs(line)
            eqs_new_count = len(eqs_all)
            text = extractText(line)
            line = ''
            for i in range(eqs_new_count - eqs_count):
                line = line + text[i] + getImgMarkdown(eqs_count+i)
            line = line + text[-1]
            fileParsed.writelines(line)
            eqs_count = eqs_new_count
        else:
            fileParsed.writelines(line)

    latexmath2png.math2png(eqs_all, outdir=MATH_IMG_PATH, prefix=MATH_IMG_PREFIX, size = MATH_IMG_SIZE)
    fileOriginal.close()
    fileParsed.close()
