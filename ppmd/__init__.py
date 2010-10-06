import markdown
from tempfile import gettempdir
import webbrowser
import os.path
import sys

def tool():
    tempdir = gettempdir()
    args = sys.argv[1:]
    for arg in args:
        md_path = os.path.abspath(arg)
        md_filename = os.path.basename(arg)
        md = open(md_path).read()
        html = markdown.markdown(md)
        html_path = os.path.join(tempdir,'%s.html'%md_filename)
        open(html_path,'w').write(html)
        webbrowser.open(html_path)
        print '%s -> %s'%(arg,html_path)
