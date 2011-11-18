def pl(items):
  if type(items) == type(list()):
    for i in items:
      print i
  else:
    print "## pl: expected <type 'list'>, got %s" % type(items)
  return items

def pd(items):
  if type(items) == type(dict()):
    for i in items.keys():
      print i, "|", items[i]
  else:
    print "## pl: expected <type 'dict'>, got %s" % type(items)
  return items