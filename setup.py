from setuptools import setup
from version import __version__ as version

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setup(
  name = 'djangolazy',
  packages = ['djangolazy'],
  version =  version,
  license='MIT',
  description = 'Script for initial django project setup',
  long_description = long_description,
  long_description_content_type = "text/markdown",
  author = ' Ishu Singh',
  author_email = 'ishu.111636@gmail.com',
  url = 'https://github.com/IshuSinghSE',
  download_url = f'https://github.com/IshuSinghSE/djangolazy/archive/refs/tags/v.{version}.tar.gz',
  keywords = ['django', 'setup', 'autosetup','setupscript'],
  install_requires=[
            'urllib3',
            ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.11',
  ],
)