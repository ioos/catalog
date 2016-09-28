# Borowwed from OWSLib https://geopython.github.io/OWSLib/
def nspath_eval(xpath, namespaces):
  ''' Return an etree friendly xpath '''
  out = []
  for chunks in xpath.split('/'):
    namespace, element = chunks.split(':')
    out.append('{%s}%s' % (namespaces[namespace], element))
  return '/'.join(out)
