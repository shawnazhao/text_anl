# the library package
# Python 3.7 TO HELP TO extract highlighted text from docx


# step 1: unzip your docx document, so you get the xml file for your document
# step 2, read the xml file for the contents of your document 


import xml.etree.ElementTree as et

# read files
myfile=et.parse("document.xml")


# revised code from: https://gist.github.com/shreyu86/1982168

#as the code shared dont work anymore

WPML_URI = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
# it finds the tag r
tag_r = WPML_URI + 'r'
tag_p = WPML_URI + 'p'
tag_rPr = WPML_URI + 'rPr'
tag_t=WPML_URI + 't'

tag_highlight = WPML_URI + 'highlight'

tag_val = WPML_URI + 'val'


# find all functions find all the tag
for paragraph in myroot[0].findall(tag_p):
    #print(paragraph)
    for r in paragraph.findall(tag_r):
        #print(r)
        for rPr in r.findall(tag_rPr):
            if rPr.find(tag_highlight).attrib[tag_val]=='yellow':
                print(r.find(tag_t).text)


#can do it with list and everything


