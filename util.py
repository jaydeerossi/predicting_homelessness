import xml.etree.ElementTree as ET

def load_dbmi(filename, tag_phi = False):
    """
    takes:
        tag_phi: include PHI in note tagged with <phi> </phi>
        one_to_one: records are 1-1 with notes. usually true.
    
    returns:
        records: list of strings containing free-text medical records
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    # for child in root:
    #     print(child.tag, child.attrib)
    # print(set([elem.tag for elem in root.iter()]))
    records = []
    for record in root.iter('RECORD'):
        for text in record:
            note = ''
            for phi in text:
                if tag_phi == True:
                    note += '<phi>' + phi.text + '</phi>'
                else:
                    note += phi.text
                note += phi.tail
            records.append(note)
    return records


if __name__ == '__main__':
    filename = r'data/test_deid_surrogate_train_all_version2.xml'
    records = load_dbmi(filename)