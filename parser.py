# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 00:00:18 2019

@author: lab
"""

import json
import objectpath
import glob
from collections import defaultdict
import pandas as pd
import numpy as np
import os

# Get Current path
path = os.path.dirname(os.path.realpath('JSON Parser.py'))

# Getting all files in directory
# path =r'C://Users//lab//Desktop//Assembly Dataset//test//test//'
allFiles = glob.glob(path + "\*.json")

Data = pd.DataFrame()
Features = ['ID', 'Name', 'SHA1', 'SHA256', 'SHA512', 'MD5', 'Sender IP', 'Reciever IP', 'Duration',
            'Severity Score', 'Category', 'Package', 'Size', 'Type', 'Dll Imports', 'Files Created',
            'Files Recreated', 'Dirtectory Created', 'Loaded DLLs', 'Files Copied', 'Registery Keys Opened'
    , 'Hosts Resleves', 'Files Written', 'Files Deleted', 'Files Exits', 'Command Line', 'Failed Files'
    , 'Wmi Queries', 'Read Files', 'Registery Keys Read', 'Directories Enumarated', 'Registery Keys Written'
    , 'Label', 'Label 2']
Dataset = pd.DataFrame(columns=Features)

i = 0
for f in allFiles:
    # Opening Json file
    with open(f, errors='ignore') as datafile:
        next(datafile)
        data = json.load(datafile)

    Dataset.loc[i] = [data["_id"], data["target"]["file"]["name"], data["target"]["file"]["sha1"],
                      data["target"]["file"]["sha256"], data["target"]["file"]["sha512"], data["target"]["file"]["md5"],
                      data["network"]["udp"][0]["src"], data["network"]["udp"][0]["dst"], data["info"]["duration"],
                      data["info"]["score"], data["info"]["category"], data["info"]["package"]
        , data["target"]["file"]["size"],
                      data["target"]["file"]["type"]
        , data["static"]["imported_dll_count"],
                      len(data["behavior"]["summary"]["file_created"]),
                      len(data["behavior"]["summary"]["file_recreated"]),
                      len(data["behavior"]["summary"]["directory_created"]),
                      len(data["behavior"]["summary"]["dll_loaded"]),
                      len(data["behavior"]["summary"]["file_copied"]),
                      len(data["behavior"]["summary"]["regkey_opened"]),
                      len(data["behavior"]["summary"]["resolves_host"]),
                      len(data["behavior"]["summary"]["file_written"]),
                      len(data["behavior"]["summary"]["file_deleted"]),
                      len(data["behavior"]["summary"]["file_exists"]),
                      len(data["behavior"]["summary"]["command_line"]),
                      len(data["behavior"]["summary"]["file_failed"]),
                      len(data["behavior"]["summary"]["wmi_query"]),
                      len(data["behavior"]["summary"]["file_read"]),
                      len(data["behavior"]["summary"]["regkey_read"]),
                      len(data["behavior"]["summary"]["directory_enumerated"]),
                      len(data["behavior"]["summary"]["regkey_written"]),
                      "Malware",
                      "1"
                      ]
    i = i + 1

    print(data["_id"])  # ID
    print(data["target"]["file"]["name"])  # Name
    print(data["target"]["file"]["sha1"])  # SHA1
    print(data["target"]["file"]["sha256"])  # SHA256
    print(data["target"]["file"]["sha512"])  # SHA512
    print(data["target"]["file"]["md5"])  # MD5
    print(data["network"]["udp"][0]["src"])  # Sender IP
    print(data["network"]["udp"][0]["dst"])  # Reciever IP
    print(data["info"]["duration"])  # Duration of Execution
    print(data["info"]["score"])  # Severity Score
    print(data["info"]["category"])  # Category
    print(data["info"]["package"])  # Package i.e. exe
    print(data["target"]["file"]["size"])  # Size Bytes
    print(data["target"]["file"]["type"])  # File Type
    print(data["static"]["imported_dll_count"])  # Dll import count
    print(len(data["behavior"]["summary"]["file_created"]))  # File Created
    print(len(data["behavior"]["summary"]["file_recreated"]))  # File ReCreated
    print(len(data["behavior"]["summary"]["directory_created"]))  # Directory Created
    print(len(data["behavior"]["summary"]["dll_loaded"]))  # File loaded
    print(len(data["behavior"]["summary"]["file_copied"]))  # File Copied
    print(len(data["behavior"]["summary"]["regkey_opened"]))
    print(len(data["behavior"]["summary"]["resolves_host"]))
    print(len(data["behavior"]["summary"]["file_written"]))
    print(len(data["behavior"]["summary"]["file_deleted"]))  # file_deleted
    print(len(data["behavior"]["summary"]["file_exists"]))  # file_exists
    print(len(data["behavior"]["summary"]["command_line"]))  # command_line
    print(len(data["behavior"]["summary"]["file_failed"]))  # file_failed
    print(len(data["behavior"]["summary"]["wmi_query"]))  # wmi_query
    print(len(data["behavior"]["summary"]["file_read"]))  # file_read
    print(len(data["behavior"]["summary"]["regkey_read"]))  # regkey_read
    print(len(data["behavior"]["summary"]["directory_enumerated"]))  # directory_enumerated
    print(len(data["behavior"]["summary"]["regkey_written"]))  # regkey_written




