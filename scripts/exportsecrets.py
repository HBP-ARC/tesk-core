#!/usr/bin/python

import json
import os

config = json.load(open(os.path.join(os.environ["HOME"], '.kube/config')))

print('export KUBE_CA='+config['clusters'][0]['cluster']['certificate-authority-data'])
print('export KUBE_CC='+config['users'][0]['user']['client-certificate-data'])
print('export KUBE_CK='+config['users'][0]['user']['client-key-data'])
