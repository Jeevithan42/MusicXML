import xml.etree.ElementTree as ET


#Get all of the information to make a basic file
print("Enter the following information. If any are not applicable, just press enter without typing anything")
print("Anything left unentered will be set to default")

Tempo = input('Tempo?  Default => 60')
Key = input('Key?  Default => C Major')
Time_Signature = input('Time Signature(Seperated be backslash)? Default => 4/4')
Clef = input('Clef?  Default => Treble')
Title = input('Title? Default => Applesauce')

#Prep xml document


root = ET.Element('score-partwise version="4.0"')
partlist = ET.SubElement(root, 'part-list')
scorepart = ET.SubElement(partlist, 'scorepart')
age = ET.SubElement(person, 'age')




#At the end
tree = ET.Element('tmx', {'version': '1.4a'})

with open('myfile.tmx', 'wb') as f:
    f.write('<?xml version="1.0" encoding="UTF-8" ?><!DOCTYPE tmx SYSTEM "tmx14a.dtd">'.encode('utf8'))
    ET.ElementTree(tree).write(f, 'utf-8')