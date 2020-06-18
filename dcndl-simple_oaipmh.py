#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import glob
import xml.etree.ElementTree as ET
import pandas as pd
import csv
import sys
import dcndl_perse

NS = {'xml': 'http://www.w3.org/XML/1998/namespace',
      'oai': 'http://www.openarchives.org/OAI/2.0/',
      'rdf' : 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
      'rdfs' : 'http://www.w3.org/2000/01/rdf-schema#',
      'owl' : 'http://www.w3.org/2002/07/owl#',
      'dc' : 'http://purl.org/dc/elements/1.1/',
      'dcterms' : 'http://purl.org/dc/terms/',
      'foaf' : 'http://xmlns.com/foaf/0.1/',
      'dcndl_simple' : 'http://ndl.go.jp/dcndl/dcndl_simple/',
      'dcndl' : 'http://ndl.go.jp/dcndl/terms/',
      'xsi' : 'http://www.w3.org/2001/XMLSchema-instance'}

record_path = "./oai:ListRecords/oai:record"
metadata_path = "./oai:metadata/dcndl_simple:dc"

data_row = []

if __name__ == "__main__":

    # file = "0005.xml"
    for file in glob.glob("./data/*.xml"):
        dcndl_perse.dcndlsimple_parse(file, record_path, metadata_path, NS, data_row)

    dcndl_data = pd.DataFrame(data_row)
    dcndl_data.columns = dcndl_perse.columns
    dcndl_data.to_csv('dcndl-oai.csv', encoding='utf-8_sig', quoting=csv.QUOTE_ALL, index=False )
