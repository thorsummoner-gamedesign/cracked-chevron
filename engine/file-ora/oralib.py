from pprint import pprint

from os import path
import zipfile
import xml.etree.ElementTree as xml_object
from StringIO import StringIO

def load_ora(ora_path):
    ora_file = zipfile.ZipFile(ora_path)
    file_ora_meta = xml_object.fromstring(ora_file.read('stack.xml'))

    layers = {}
    for i in file_ora_meta.iter('layer'):
        layers[i.attrib['name']] = StringIO(ora_file.read(i.attrib['src'])),

    return {
        'name'  : path.splitext(path.basename(ora_path))[0],
        'layers': layers,
        'width' : int(file_ora_meta.attrib.get('w', '')),
        'height': int(file_ora_meta.attrib.get('h', '')),
    }

if '__main__' == __name__:
    ora_file = '../../assets/CrackedSpire.ora'
    pprint(
        load_ora(ora_file)
    )

