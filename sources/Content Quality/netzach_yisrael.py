#encoding=utf-8
import django
django.setup()
from sefaria.model import *
from sefaria.helper.schema import *
    #first convert to complex
    # i = library.get_index("Netzach Yisrael")
    # convert_simple_index_to_complex(i)
    #
    # #now add an intro node
    # i = library.get_index("Netzach Yisrael")
    # intro = JaggedArrayNode()
    # intro.add_shared_term("Introduction")
    # intro.add_structure(["Paragraph"])
    # insert_first_child(intro, i.nodes)

root = SchemaNode()
root.add_primary_titles("Netzach Yisrael", u"נצח ישראל")
intro = JaggedArrayNode()
intro.add_structure(["Paragraph"])
intro.add_shared_term("Introduction")
intro.key = "intro"
intro.validate()
default = JaggedArrayNode()
default.default = True
default.key = "default"
default.add_structure(["Chapter", "Paragraph"])
default.validate()
root.append(intro)
root.append(default)
root.validate()
schema = root.serialize()

mapping = {}
for i in range(1, 65):
    actual_value = i-1
    if actual_value == 0:
        mapping["Netzach Yisrael 1"] = "Netzach Yisrael, Introduction"
    else:
        mapping["Netzach Yisrael {}".format(i)] = "Netzach Yisrael {}".format(actual_value)


migrate_to_complex_structure("Netzach Yisrael", schema, mapping)

