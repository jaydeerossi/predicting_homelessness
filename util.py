import xml.etree.ElementTree as ET

def load_dbmi(filename, mode = 'smoking'):
    """
    takes:
        mode: what dataset? ['deid', 'smoking']
        tag_phi: include PHI in note tagged with <phi> </phi>
    
    returns:
        records: list of strings containing free-text medical records
    """
    def load_deid(filename, tag_phi = False):
        tree = ET.parse(filename)
        root = tree.getroot()
        # for child in root:
        #     print(child.tag, child.attrib)
        # print(set([elem.tag for elem in root.iter()]))
        notes = []
        for record in root.iter('RECORD'):
            for text in record:
                note = ''
                for phi in text:
                    if tag_phi == True:
                        note += '<phi>' + phi.text + '</phi>'
                    else:
                        note += phi.text
                    note += phi.tail
                notes.append(note)
        return notes, []

    def load_smoking(filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        ids, smoking, notes = [], [], []
        for record in root.iter('RECORD'):
            ids.append(record.attrib['ID'])
            for item in record:
                if item.tag == 'SMOKING':
                    smoking.append(item.attrib['STATUS'])
                elif item.tag == 'TEXT':
                    notes.append(item.text)
        return notes, smoking
    
    if mode == 'deid':
        return load_deid(filename)
    elif mode == 'smoking':
        return load_smoking(filename)

if __name__ == '__main__':
    filename = r'data/smokers_surrogate_train_all_version2.xml'
    notes, smoking = load_dbmi(filename, mode = 'smoking')