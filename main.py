#!/usr/bin/env python
# Created by Enrique Plata
# set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\lf188653\AppData\Local\Google\Cloud SDK\microstrategyit-749574041a8c.json
# python main.py c:/Users/lf188653/Desktop/Data/

import time
import os
import sys
from pathlib import Path
from functions import getRegistry, synchronous_pull, binary_to_dict, download_blob
  
if __name__ == '__main__':

  REGISTRY = getRegistry()
  base_path: str = sys.argv[1]

  if base_path is not None or base_path != '':
    try:
      # Get new messages
      data_binary = synchronous_pull(REGISTRY['PROJECT_ID'], REGISTRY['SUBSCRIPTION'])
      data_dictonary = binary_to_dict(data_binary)

      # Download the file from bucket
      bucket = data_dictonary['bucket']
      name = data_dictonary['name']
      
      destination = Path(f'{base_path}{name}')

      download_blob(bucket_name=bucket, source_blob_name=name, destination_file_name=destination)
      
    except Exception as e:
      print(e)
  else:
    sys.exit()