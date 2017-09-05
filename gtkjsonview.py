import sys
import os
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
try:
  import json
except:
  import simplejson as json
  pass

if len(sys.argv) == 2:
  data = open(sys.argv[1]).read().strip()
else:
  data = sys.stdin.read().strip()
if data[0] == '(' and data[-1] == ')':
  data = data[1:-1]

def add_item(key, data, model, parent = None):
  if isinstance(data, dict):
    if len(key):
      obj = model.append(parent, [str(key) + ' (object)'])
      walk_tree(data, model, obj)
    else:
      walk_tree(data, model, parent)
  elif isinstance(data, list):
    arr = model.append(parent, [key + ' (array)'])
    for index in range(0, len(data)):
      add_item('', data[index], model, model.append(arr, ['[' + str(index) + ']']))
  elif isinstance(data, str):
    if len(data) > 256:
      data = data[0:255] + "..."
      model.append(parent, [key + ' : "' + data + '"'])
    else:
      model.append(parent, [key + ' : "' + data + '"'])
  elif isinstance(data, int):
      model.append(parent, [key + ' : ' + str(data)])
  else:
    model.append(parent, [str(data)])

def walk_tree(data, model, parent = None):
  if isinstance(data, list):
    add_item('', data, model, parent)
  elif isinstance(data, dict):
    for key in data:
      add_item(key, data[key], model, parent)
  else:
    add_item('', data, model, parent)

class JSONViewerWindow(Gtk.Window):
    def __init__(self):
      Gtk.Window.__init__(self, title="JSon Viewer")
      self.set_default_size(600, 400)
      swin = Gtk.ScrolledWindow()
      model = Gtk.TreeStore(str)
      tree = Gtk.TreeView(model)
      tvcol = Gtk.TreeViewColumn('JSON')
      tree.append_column(tvcol)
      cell = Gtk.CellRendererText()
      tvcol.pack_start(cell, True)
      tvcol.add_attribute(cell, 'text', 0)
      swin.add_with_viewport(tree)
      self.add(swin)
      walk_tree(json.loads(data), model)

win = JSONViewerWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
