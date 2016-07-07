import xml.etree.ElementTree as ET
import sys
from collections import Counter
import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter

tree = ET.parse(sys.argv[1])
root = tree.getroot()

names_dict = []

  
for child in root.iter('Name'):
  if "<" not in child.attrib['val']:
    names_dict.append([child.attrib['val'], child.attrib['pos'], child.attrib['len']])  
  else:
    names_dict.append(["title", child.attrib['val'].replace("<",""), child.attrib['pos'], child.attrib['len']])
   
WORD_WINDOW=15 
def dist(line):
  line = line.split()
  if (len(line)-2) > WORD_WINDOW:
    return False
  else:
    return True
  
pairs = Counter() 
names_for_file = {}
with open(sys.argv[2]) as f:
  text = f.read()
  t = 0
  for el in range(len(names_dict)-1):
    if names_dict[el][0] != 'title' and names_dict[el][0] not in names_for_file:
      names_for_file[names_dict[el][0]] = t
      t += 1
    for el2 in range(el+1, len(names_dict)):
      if names_dict[el][0] != names_dict[el2][0]:
        if names_dict[el][0] != 'title' and names_dict[el2][0] != 'title':
          name1, pos1, len1 = names_dict[el]
          name2, pos2, len2 = names_dict[el2]
            
          text_extract = text[int(pos1):(int(pos2)+int(len2))]
          if dist(text_extract):
            pair = (max(name1, name2), min(name1, name2))
            pairs[pair] += 1
          else:
            break
        else:
          break
          
step = int((max(pairs.values()) - min(pairs.values()))/float(20))
for i in pairs.items():
  for a in range(20):
    if i[1] > a*step and i[1] <= (a+1)*step:
      pairs[i[0]] = a+1
  if pairs[i[0]] > 20:
    pairs[i[0]] = 20

  
with open(sys.argv[3], 'w') as w:
  w.write('<?xml version="1.0" encoding="UTF-8"?>\n')
  w.write('<gexf xmlns:viz="http:///www.gexf.net/1.1draft/viz" version="1.1" xmlns="http://www.gexf.net/1.1draft">\n')
  w.write('<graph defaultedgetype="undirected" idtype="string" type="static">\n')
  w.write('<nodes count="'+str(len(names_for_file))+'">\n')
  for node in names_for_file.items():
    w.write('<node id="'+str(node[1])+'" label="'+node[0]+'"/>\n')
  w.write('</nodes>\n')  
  w.write('<edges count="'+str(len(pairs))+'">\n')
  c = 0
  for edge in pairs.items():
    w.write('<edge id="'+str(c)+'" source="'+str(names_for_file[edge[0][0]])+'" target="'+str(names_for_file[edge[0][1]])+'" weight="'+str(edge[1])+'"/>\n')
    c += 1
  w.write('</edges>\n')    
  w.write('</graph>\n')
  w.write('</gexf>\n') 
  