#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import glob
import xml.etree.ElementTree as ET
import pandas as pd
import csv
import sys
import dcndl_perse

NS = {'xml': 'http://www.w3.org/XML/1998/namespace',
      'dc' : 'http://purl.org/dc/elements/1.1/',
      'dcterms' : 'http://purl.org/dc/terms/',
      'rdfs' : 'http://www.w3.org/2000/01/rdf-schema#',
      'dcmitype' : 'http://purl.org/dc/dcmitype/',
      'dcndl' : 'http://ndl.go.jp/dcndl/terms/',
      'xsi' : 'http://www.w3.org/2001/XMLSchema-instance',
      'rdf' : 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
      'openSearch' : 'http://a9.com/-/spec/opensearchrss/1.0/'}

record_path = "./channel/item"
metadata_path = None

data_row = []

if __name__ == "__main__":

    file = "0005.xml"
    dcndl_perse.dcndlsimple_parse(file, record_path, metadata_path, NS, data_row)

    dcndl_data = pd.DataFrame(data_row)
    dcndl_data.columns = dcndl_perse.columns
    dcndl_data.to_csv('dcndl_search.csv', encoding='utf-8_sig', quoting=csv.QUOTE_ALL, index=False )
