import xmltodict
import pprint 



class ePubXMLProcessor(object):

    def __init__(self, xmlfile):
        self.xmlfile = xmlfile


    def todict(self, ns=None):
        xmldict = None # defaultdict(list)i
        with open(self.xmlfile) as xmlfile:
            xmlcontent = xmlfile.read()
            xmldict = xmltodict.parse(xmlcontent, namespaces=ns)
        return xmldict
    def toxml(self, ordered_dict):
        return xmltodict.unparse(ordered_dict, pretty=True)


if __name__ == '__main__':
    opffile = "/home/sofycomps/work/xmlprocessor/input/accessible_epub/EPUB/package.opf"
    xmlprocessor = ePubXMLProcessor(opffile)
    d = xmlprocessor.todict()
    pprint.pprint(d)
    s = xmlprocessor.toxml(d)
    pprint.pprint(s)

