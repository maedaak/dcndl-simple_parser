import xml.etree.ElementTree as ET

columns = ['dc:title', 'dcndl:titleTranscription', 'dcterms:alternative',
           'dcndl:alternativeTranscription', 'dcndl:volume', 'dcndl:volumeTranscription',
           'dcndl:volumeTitle', 'dcndl:volumeTitleTranscription',
           'dcndl:seriesTitle', 'dcndl:seriesTitleTranscription',
           'dcndl:partTitle', 'dcndl:partTitleTranscription',
           'dc:creator', 'dcndl:creatorTranscription',
           'dcndl:seriesCreator', 'dcndl_partCreator', 'dcndl:edition',
           'dc:publisher', 'dcndl:publicationPlace', 'dc:date', 
           'dcterms:issued', 'dcndl:digitizedPublisher',
           'dcndl:dateDigitized', 
           'dc:subject', 'dcndl:NDLC', 'dcndl:NDC9',
           'dc:language', 
           'dcterms:description', 'dcterms:abstract',
           'dcndl:DOI', 'dcndl:ISBN', 'dcndl:NDLBibID',
           'dcndl:JPNO',
           'dcndl:publicationName', 'dcndl:publicationVolume',
           'dcndl:number', 'dcndl:issue', 'dcndl:pageRange',
           'dcndl:materialType', 'dcterms:rights',  
           'dcterms:extent', 
           'source_url']


def single(metadata, path, NS):
    data = metadata.find(path, NS)
    result = ""
    if ET.iselement(data):
        if data.text:
            result = data.text
    return result


def repeat(metadata, path, NS):
    data = metadata.findall(path, NS)
    data_list = []
    result = ""
    if len(data) > 0 and ET.iselement(data[0]):
        for work in data:
            if work.text:
                data_list.append(work.text)
    result = "|".join(data_list)
    return result


def dcndlsimple_parse(file, record_path, metadata_path, NS, data_row):
    xsi_type = '{' + NS["xsi"] + '}type'
    rdf_type = '{' + NS["rdf"] + '}type'
    rdf_resource = '{' + NS["rdf"] + '}resource'
    xml_lang = '{' + NS["xml"] + '}lang'
    tree = ET.parse(file)
    root = tree.getroot()
    records = root.findall(record_path, NS)

    for record in records:
        # 変数の初期化
        dc_title = ""
        dcndl_titleTranscription = ""
        dcterms_alternative = ""
        dcndl_alternativeTranscription = ""
        dcndl_volume = ""
        dcndl_volumeTranscription = ""
        dcndl_volumeTitle = ""
        dcndl_volumeTitleTranscription = ""
        dcndl_seriesTitle = ""
        dcndl_seriesTitleTranscription = ""
        dcndl_partTitle = ""
        dcndl_partTitleTranscription = ""
        dc_creator = ""
        dcndl_creatorTranscription = ""
        dcndl_seriesCreator = ""
        dcndl_partCreator = ""
        dcndl_edition = ""
        dc_publisher =""
        dcndl_publicationPlace = ""
        dc_date = ""
        dcterms_issued = ""
        dcndl_digitizedPublisher = ""
        dcndl_dateDigitized = ""
        subject = ""
        NDLC = ""
        NDC9 = ""
        dc_language = ""
        dcterms_description = ""
        dcterms_abstract = ""
        dcterms_extent = ""
        dcndl_materialType = ""
        DOI = ""
        ISBN = ""
        NDLBibID = ""
        JPNO = ""
        dcndl_publicationName = ""
        dcndl_publicationVolume = ""
        dcndl_number = ""
        dcndl_issue = ""
        dcndl_pageRange = ""
        dcterms_rights  = ""
        source_uri = ""

        if metadata_path:
            metadata = record.find(metadata_path, NS)
        else:
           metadata = record

        if not ET.iselement(metadata):
            continue

        dc_title = repeat(metadata, "./dc:title", NS)

        dcndl_titleTranscription = \
            single(metadata, "./dcndl:titleTranscription", NS)

        dcterms_alternative = \
            single(metadata, "./dcterms:alternative", NS)

        dcndl_alternativeTranscription = \
            single(metadata, "./dcndl:alternativeTranscription", NS)

        dcndl_volume = single(metadata, "./dcndl:volume", NS)

        dcndl_volumeTranscription = \
           single(metadata, "./dcndl:volumeTranscription", NS)

        dcndl_volumeTitle = \
           single(metadata, "./dcndl:volumeTitle", NS)

        dcndl_volumeTitleTranscription = \
           single(metadata, "./dcndl:volumeTitleTranscription", NS)

        dcndl_seriesTitle = \
           single(metadata, ".dcndl:seriesTitle", NS)

        dcndl_seriesTitleTranscription = \
           single(metadata, "./dcndl:seriesTitleTranscription", NS)

        dcndl_partTitle = \
           repeat(metadata, "./dcndl:partTitle", NS)

        dcndl_partTitleTranscription = \
           repeat(metadata, "./dcndl:partTitleTranscription", NS)

        dc_creator = repeat(metadata, "./dc:creator", NS)

        dcndl_creatorTranscription = repeat(metadata, "./dcndl:creatorTranscription", NS)

        dcndl_seriesCreator = \
            repeat(metadata, "./dcndl:seriesCreator", NS)

        dcndl_partCreator = \
            repeat(metadata, "./dcndl:partCreator", NS)

        dcndl_edition = \
            repeat(metadata, "./dcndl:edition", NS)

        dc_publisher = repeat(metadata, "./dc:publisher", NS)

        dcndl_publicationPlace = repeat(metadata, "./dcndl:publicationPlace", NS)

        dc_date = repeat(metadata, "./dc:date", NS)

        dcterms_issued = repeat(metadata, "./dcterms:issued", NS)

        dcndl_digitizedPublisher = repeat(metadata, "./dcndl:digitizedPublisher", NS)

        dcndl_dateDigitized = repeat(metadata, "./dcndl:dateDigitized", NS)

        # dc_subject
        dc_subject = \
           metadata.findall("./dc:subject", NS)
        if len(dc_subject) > 0:
            subject_list = []
            for value in dc_subject:
                if xsi_type in value.attrib:
                    if value.attrib[xsi_type] == "dcndl:NDLC":
                        NDLC = value.text
                    elif value.attrib[xsi_type] == "dcndl:NDC9":
                    	NDC9 = value.text
                else:
                    subject_list.append(value.text)
            subject = "|".join(subject_list)

        dc_language = repeat(metadata, "./dc:language", NS)

        dcterms_description = repeat(metadata, "./dcterms:description", NS)

        dcterms_abstract = repeat(metadata, "./dcterms:abstract", NS)

        dcterms_extent = repeat(metadata, "./dcterms:extent", NS)

        dcndl_materialType = repeat(metadata, "./dcndl:materialType", NS)

        # dc:identifier
        dc_identifier = \
           metadata.findall("./dc:identifier", NS)
        if len(dc_identifier) > 0:
            for value in dc_identifier:
                if xsi_type in value.attrib:
                    if value.attrib[xsi_type] == "dcndl:DOI":
                        DOI = value.text
                    elif value.attrib[xsi_type] == "dcndl:ISBN":
                        ISBN = value.text
                    elif value.attrib[xsi_type] == "dcndl:NDLBibID":
                    	NDLBibID = value.text
                    elif value.attrib[xsi_type] == "dcndl:JPNO":
                    	JPNO = value.text

        dcndl_publicationName = \
            repeat(metadata, "./dcndl:publicationName", NS)

        dcndl_publicationVolume = \
            repeat(metadata, "./dcndl:publicationVolume", NS)

        dcndl_number = \
            repeat(metadata, "./dcndl:number", NS)

        dcndl_issue = \
            repeat(metadata, "./dcndl:issue", NS)

        dcndl:pageRange = \
            repeat(metadata, "./dcndl:pageRange", NS)

        dcterms_rights = single(metadata, "./dcterms:rights", NS)

        # source_uri
        dcterms_source = metadata.find("./dcterms:source", NS)
        if ET.iselement(dcterms_source):
            source_uri  = dcterms_source.attrib[rdf_resource]

        row = [dc_title, dcndl_titleTranscription, dcterms_alternative,
           dcndl_alternativeTranscription, dcndl_volume, dcndl_volumeTranscription,
           dcndl_volumeTitle, dcndl_volumeTitleTranscription,
           dcndl_seriesTitle, dcndl_seriesTitleTranscription,
           dcndl_partTitle, dcndl_partTitleTranscription,
           dc_creator, dcndl_creatorTranscription, dcndl_seriesCreator,
           dcndl_partCreator, dcndl_edition,
           dc_publisher, dcndl_publicationPlace, dc_date,
           dcterms_issued, dcndl_digitizedPublisher, dcndl_dateDigitized,
           subject, NDLC, NDC9,
           dc_language, dcterms_description, dcterms_abstract,
           DOI, ISBN, NDLBibID, JPNO,
           dcndl_publicationName, dcndl_publicationVolume,
           dcndl_number, dcndl_issue, dcndl_pageRange,
           dcndl_materialType, dcterms_rights, 
           dcterms_extent, 
           source_uri]
        data_row.append(row)
