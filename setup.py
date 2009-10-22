#from ez_setup import use_setuptools
#use_setuptools()
from setuptools import setup, find_packages

setup(name="PythonPreviewMarkdown",
      version="0.1dev",
      description="Renders markdown to a tmp file and lauches it in browser",
      author="Nick Fisher",
      packages = find_packages(),
      zip_safe = True,
      entry_points = {
          'console_scripts': [
              'ppmd = ppmd:tool',
          ]
      }
     )
