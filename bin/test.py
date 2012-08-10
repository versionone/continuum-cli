from xml.dom.minidom import Document
import copy

class dict2xml(object):
    doc     = Document()

    def __init__(self, structure):
        if len(structure) == 1:
            rootName    = str(structure.keys()[0])
            self.root   = self.doc.createElement(rootName)

            self.doc.appendChild(self.root)
            self.build(self.root, structure[rootName])

    def build(self, father, structure):
        if type(structure) == dict:
            for k in structure:
                tag = self.doc.createElement(k)
                father.appendChild(tag)
                self.build(tag, structure[k])

        elif type(structure) == list:
            grandFather = father.parentNode
            tagName     = father.tagName
            grandFather.removeChild(father)
            for l in structure:
                tag = self.doc.createElement(tagName)
                self.build(tag, l)
                grandFather.appendChild(tag)

        else:
            data    = str(structure)
            tag     = self.doc.createTextNode(data)
            father.appendChild(tag)

    def display(self):
        print self.doc.toprettyxml(indent="  ")

x = """{'auftrag':{"ecosystem_name": "teststorm8", "account_id": "e914be73-09ea-4a64-9b6a-383529e6e2b3", "ecosystem_desc": null, "tags": null, "storm_status": "Stopped", "num_objects": 0, "last_update_dt": "2012-06-27T14:09:46", "ecosystem_id": "473d4635-c083-11e1-8da5-c8bcc89d4845", "created_dt": "2012-06-27T14:09:46", "request_id": null, "ecotemplate_name": "Single Server"}}"""

xml = dict2xml(x)
xml.display()
