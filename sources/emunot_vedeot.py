# -*- coding: utf-8 -*-
import urllib
import urllib2
from urllib2 import URLError, HTTPError
import json 
import pdb
import os
import sys
import re
p = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, p)
os.environ['DJANGO_SETTINGS_MODULE'] = "sefaria.settings"
from local_settings import *
from functions import *

sys.path.insert(0, SEFARIA_PROJECT_PATH)
from sefaria.model import *

root = SchemaNode()
root.key = 'emunot'
root.add_title("Emunot VeDeot", "en", primary=True)
root.add_title(u"אמונות ודעות", "he", primary=True)

intro = JaggedArrayNode()
intro.key = 'intro'
intro.depth = 1
intro.sectionNames = ["Paragraph"]
intro.addressTypes = ["Integer"]
intro.add_title("Introduction", "en", primary=True)
intro.add_title(u"הקדמה", "he", primary=True)

content = JaggedArrayNode()
content.default = True
content.key = "default"
content.depth = 2
content.sectionNames = ["Essay", "Paragraph"]
content.addressTypes = ["Integer", "Integer"]

root.append(intro)
root.append(content)

root.validate()
index = {
    "title": "Emunot VeDeot",
    "categories": ["Philosophy"],
    "schema": root.serialize()
    }
#post_index(index)
send_text = {
	"text": ["a", "b"],
	"versionTitle": "demo",
	"versionSource": "other",
	"language": "en"
}
post_text("Emunot VeDeot, Introduction", send_text)