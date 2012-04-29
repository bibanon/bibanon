#!/usr/bin/python
#
# -*- coding: utf-8 -*-
# vim: set ts=2 sw=2 et sts=2 ai: 

"""This program converts mediawiki format to markdown.

It takes a file as an argument and outputs the markdown text to stdout.
"""

# stdlib imports
import cStringIO as StringIO
import optparse
import sys

# External module imports
from mwlib.uparser import simpleparse
from mwlib.parser import nodes


class options:
  # Should we drop to the debugger on error
  DEBUGGER = False
  # Should we die on unknown flags
  STRICT = True

parser = optparse.OptionParser()
parser.add_option(
  "-f", "--file", dest="file",
  help="wikimedia FILE to read.", metavar="FILE")
parser.add_option(
  "-d", "--debugger", dest="DEBUGGER", action="store_true",
  default=sys.stdout.isatty() and sys.stdin.isatty(),
  help="Drop to Python PDB debugger on an error.")
parser.add_option(
  "--no-debugger", dest="DEBUGGER", action="store_false",
  default=sys.stdout.isatty() and sys.stdin.isatty(),
  help="Don't drop to Python PDB debugger on an error.")
parser.add_option(
  "-s", "--strict", dest="STRICT", action="store_true", default=options.STRICT,
  help="Error on known tags, style or other problems.")
parser.add_option(
  "--no-strict", dest="STRICT", action="store_false", default=options.STRICT,
  help="Error on known tags, style or other problems.")
parser.add_option(
  "-l", "--lenient", dest="STRICT", action="store_true", default=options.STRICT,
  help="Don't error on known tags, style or other problems.")


def debugger():
  if options.DEBUGGER:
    # Flush the output to make sure we see the latest errors/output
    sys.stderr.write('\n\n')
    sys.stderr.flush()

    sys.stdout.write('\n\n')
    sys.stdout.flush()

    import traceback, pdb
    type, value, tb = sys.exc_info()
    pdb.post_mortem(tb)
  else:
    raise

class BaseConverter(object):

  def __init__(self):
    self.out = ""
    self.listmode = []

  def append(self, s):
    if isinstance(s, unicode):
      s = s.encode('utf-8')
    self.out += s

  def getvalue(self):
    out = self.out
    self.out = ""
    return out

  def parse_node(self, node):
    try:
      tagname = 'on_'+str(node.tagname).replace('@', '')
      classname = 'on_'+node.__class__.__name__.lower().replace('@', '')
      f = getattr(self, tagname, getattr(self, classname, None))
      f(node)
    except AttributeError, e:
      sys.stderr.write('Unknown node: '+(node.tagname or node.__class__.__name__.lower()))
      assert not options.STRICT

  def parse_children(self, node):
    for child in node.children:
      self.parse_node(child)

  on_node = parse_children

  def on_article(self, node):
    self.parse_children(node)
    self.produce_dls()

  def on_ol(self, node):
    self.listmode.append('order')
    self.append('\n')
    self.parse_children(node)
    self.listmode.pop(-1)

  def on_ul(self, node):
    self.listmode.append('unorder')
    self.append('\n')
    self.parse_children(node)
    self.listmode.pop(-1)

  def on_text(self, node):
    self.append(node.asText())

  def on_style(self, node):
    # Definition list?
    if node.caption == ';':
      if not hasattr(self, 'dls'):
        self.dls = []

      self.dls.append(node)

    elif node.caption == ':':
      # If not part of an definition list, it's an indent...
      if not hasattr(self, 'dls'):
        self.on_blockquote(node)
      else:
        self.dls.append(node)

    # italics
    elif node.caption == "'''":
      self.on_bold(node)

    # bold
    elif node.caption == "''":
      self.on_italics(node)

    # underline
    elif node.caption == "u":
      self.on_underline(node)

    else:
      sys.stderr.write("Unknown style: %s\n" % node.caption)
      assert not options.STRICT

  def on_underline(self, node):
    self.append("<u>")
    self.parse_children(node)
    self.append("</u>")

  # Ignore category links as we don't have anything similar
  def on_categorylink(self, node):
    return

  def on_table(self, node):
    table_cell_parser = self.__class__()

    table = []
    table_caption = ""
    table_width = 0
    table_column_widths = []
    for row in node.children:
      if isinstance(row, nodes.Caption):
        table_cell_parser.parse_children(row)
        output = table_cell_parser.getvalue()
        table_caption += output
        continue

      if len(row.children) > table_width:
        table_width = len(row.children)
        while len(table_column_widths) < table_width:
          table_column_widths.append(0)

      cells = []
      for i, cell in enumerate(row.children):
        table_cell_parser.parse_children(cell)
        cell_data = table_cell_parser.getvalue()

        if table_column_widths[i] < len(cell_data):
          table_column_widths[i] = len(cell_data)

        cells.append({'node': cell, 'rendered': cell_data})

      args = {'rowtype': row}
      if len(row.children):
        args['celltype'] = row.children[-1]
      if len(cells):
        args['cells'] = cells
      table.append(args)

    for row in table:
      while len(row['cells']) < table_width:
        row['cells'].append({'rendered': ''})

    self.on_process_table(table_caption, table_column_widths, table)


class HTMLConverter(BaseConverter):
  """During HTML output (such as dl lists and tables) Markdown doesn't work."""

  def on_p(self, node):
    self.append("<p>")
    self.parse_children(node)
    self.append("</p>")
    self.produce_dls()

  def on_italics(self, node):
    self.append("<em>")
    self.parse_children(node)
    self.append("</em>")

  def on_bold(self, node):
    self.append("<strong>")
    self.parse_children(node)
    self.append("</strong>")

  def on_url(self, node):
    parser = HTMLConverter()
    parser.parse_children(node)
    output = parser.getvalue()

    if not output:
      output = node.caption

    self.append("<a href='%s'>%s</a>" % (
        node.caption.replace(' ', '_'), output))

  on_namedurl = on_url

  def on_imagelink(self, node):
    self.append("<img src='%s' alt='%s' />'" % (
        node.target.replace('Image:', '').replace(' ', '_'), node.asText()))

  def on_articlelink(self, node):
    for i in ['jpg', 'png', 'gif']:
      if node.target.endswith(i):
        self.on_imagelink(node)
        break
    else:
      self.append("<a href='%s'>%s</a>" % (
          node.caption.replace(' ', '_'), node.caption))

  def on_namespacelink(self, node):
    for i in ['jpg', 'png', 'gif']:
      if node.target.endswith(i):
        self.on_imagelink(node)
        break
    else:
      node.caption = node.target
      self.on_url(node)

  def produce_dls(self):
    # We need to specially handle defintion lists
    if hasattr(self, "dls"):
      self.append("<dl>\n")

      dls = self.dls
      del self.dls

      for dl in dls:
        if dl.caption == ';':
          self.append('<dt>')
          self.parse_children(dl)
          self.append('</dt>\n')
        elif dl.caption == ':':
          self.append('<dd>')
          self.parse_children(dl)
          self.append('</dd>\n')

      self.append("</dl>\n")
    self.append('\n')

  def on_section(self, node):
    self.append("\n")
    self.append("<h%i>" % node.level)
    self.parse_node(node.children[0])
    self.append("</h%i>" %node.level)
    for child in node.children[1:]:
      self.parse_node(child)


class MarkdownConverter(BaseConverter):

  def __init__(self):
    BaseConverter.__init__(self)
    self.html = HTMLConverter()

  def parse(self, text):
    sys_stdout = sys.stdout
    ast_str = StringIO.StringIO()
    sys.stdout = ast_str
    ast = simpleparse(text.decode('utf-8'))
    sys.stdout = sys_stdout
    self.parse_node(ast)

  def on_blockquote(self, node):
    parser = MarkdownConverter()
    parser.parse_children(node)
    output = parser.getvalue()

    lines = []
    for line in output.split('\n'):
      if line:
        lines.append("> "*len(node.caption)+line)
      else:
        lines.append(line)
    self.append("\n".join(lines))

  def on_preformatted(self, node):
    parser = MarkdownConverter()
    parser.parse_children(node)
    output = parser.getvalue()

    lines = []
    for line in output.split('\n'):
      if line:
        lines.append("    "+line)
      else:
        lines.append(line)
    self.append("\n".join(lines))

  def on_pre(self, node):
    parser = HTMLConverter()
    parser.parse_children(node)
    output = parser.getvalue()
    self.append('<pre>%s</pre>\n' % output)

  def on_code(self, node):
    self.append('`')
    self.parse_children(node)
    self.append('`')

  def on_tt(self, node):
    self.append('<tt>')
    self.parse_children(node)
    self.append('</tt>')

  def on_p(self, node):
    self.parse_children(node)
    self.produce_dls()

  def produce_dls(self):
    if hasattr(self, "dls"):
      self.append("<dl>\n")

      dls = self.dls
      del self.dls

      for dl in dls:
        if dl.caption == ';':
          self.append('<dt>')
          self.html.parse_children(dl)
          self.append(self.html.getvalue())
          self.append('</dt>\n')
        elif dl.caption == ':':
          self.append('<dd>')
          self.html.parse_children(dl)
          self.append(self.html.getvalue())
          self.append('</dd>\n')

      self.append("</dl>\n")

  def on_italics(self, node):
    self.append("_")
    self.parse_children(node)
    self.append("_")

  def on_bold(self, node):
    self.append("**")
    self.parse_children(node)
    self.append("**")

  def on_gallery(self, node):
    """Gallery widgets are converted to lists."""
    for child in node:
      self.append('*   ')
      self.parse_node(child)
      self.append('\n')

  def on_url(self, node):
    parser = MarkdownConverter()
    parser.parse_children(node)
    output = parser.getvalue().strip()

    if not output:
      self.append("<%s>" % node.caption)
    else:
      self.append("[")
      self.append(output)
      self.append("](%s)" % node.caption)

  on_namedurl = on_url

  def on_imagelink(self, node):
    self.append('![%s](%s)' % (
        node.asText(), node.target.replace('Image:', '').replace(' ', '_')))

  def on_articlelink(self, node):
    for i in ['jpg', 'png', 'gif']:
      if node.target.endswith(i):
        self.on_imagelink(node)
        break
    else:
      self.append("[%s](/%s)" % (node.target, node.target.replace(' ', '_')))

  def on_namespacelink(self, node):
    for i in ['jpg', 'png', 'gif']:
      if node.target.endswith(i):
        self.on_imagelink(node)
        break
    else:
      node.caption = node.target.replace(' ', '_')
      self.on_url(node)

  def on_section(self, node):
    self.append("\n")
    self.append("#" * node.level + " ")
    self.parse_node(node.children[0])
    self.append(" "+"#" * node.level)
    self.append("\n")
    for child in node.children[1:]:
      self.parse_node(child)

  def on_li(self, node):
    listmode = {'order': '1.', 'unorder': '*'}

    # mediawiki format looks like the following:
    # * List item A
    # *: More list item A
    #   which mwlib converts to
    # Item tagname='li'->'li'
    #  Node lineprefix=
    #   u' List item A'
    #   u'\n'
    #  Style':'
    #   Node
    #    Node lineprefix=
    #     Paragraph tagname='p'->'p'
    #      u'More list item A'
    #
    # So we need to strip out the Style elements
    children = [node.children[0]]
    for child in node.children[1:]:
      if isinstance(child, nodes.Style) and child.caption == ':':
        children += child.children
      else:
        children.append(child)
    node.children = children

    parser = MarkdownConverter()
    parser.parse_children(node)
    output = parser.getvalue()

    if not output.strip():
      return

    # Strip a leading space (from the following)
    # *> <test
    if output and output[0] == ' ':
      output = output[1:]

    indent = '    '*(len(self.listmode)-1)

    output = output.split('\n')

    lines = ["%s%s %s" % (
        indent, listmode[self.listmode[-1]], output[0].lstrip())]
    for line in output[1:]:
      if line:
        lines.append("%s  %s" % (indent, line.lstrip()))
      else:
        lines.append(line)

    self.append("\n".join(lines))

  def on_tagnode(self, node):
    if node.caption == 'hr':
      self.append('-'*75+'\n')
    elif node.caption == 'br':
      self.append('<br>')
    else:
      sys.stderr.write( "Unknown tag %s %s\n" % (node, node.caption))
      assert not options.STRICT

  def on_process_table(self, caption, widths, rows):
    if caption:
      self.append('### %s ###\n' % caption)

    # Insert a dummy header if one doesn't exist
    if rows[0]['celltype'].tagname != 'th':
      fakenode = nodes.Node()
      fakenode.tagname = 'th'
      fakenode.vlist = {}
      rows.insert(0, {'rowtype': rows[0]['rowtype'],
                      'celltype': fakenode,
                      'cells': [{'node': fakenode, 'rendered': ''}]*len(widths)})

    header = rows[0]
    for row in rows:
      line = '| '
      divider = '| '
      for i, cell in enumerate(row['cells']):
        headernode = header['cells'][i].get('node', None)
        if headernode:
          align = headernode.vlist.get('align', 'left')
        else:
          align = 'left'

        width = widths[i]

        rendered = unicode(cell['rendered'], 'utf-8').strip()
        rendered = "<br>".join(rendered.split('\n'))

        if align == 'right':
          f = rendered.rjust
          divider += '-'*(width-1) + ':'
        elif align == 'center' or align == 'centre':
          f = rendered.center
          divider += ':' + '-'*(width-2) + ':'
        elif align == 'left':
          f = rendered.ljust
          divider += '-'*width
        else:
          assert False, 'Unknown alignment %s (%s)' % (cell['align'], cell)

        line += f(widths[i])
        line += ' | '
        divider += ' | '

      self.append(line[:-2])
      self.append('\n')

      if row['celltype'].tagname == 'th':
        self.append(divider[:-2])
        self.append('\n')

        header = row


def main(argv):
  global options
  (options, args) = parser.parse_args(argv)

  if options.file:
    infile = file(options.file)
  elif args:
    infile = file(args[0])
  else:
    infile = sys.stdin

  mediawiki = infile.read()

  try:
    c = MarkdownConverter()
    c.parse(mediawiki)
    print c.out
  except:
    debugger()


if __name__ == "__main__":
  main(sys.argv[1:])
