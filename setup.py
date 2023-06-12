from setuptools import setup
from djangolazy import __version__ as version

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setup(
  name = 'djangolazy',         # How you named your package folder (MyLib)
  packages = ['djangolazy'],   # Chose the same as "name"
  version = version,      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Script for initial django project setup',   # Give a short description about your library
  long_description = long_description,
  long_description_content_type = "text/markdown",
  author = ' Ishu Singh',                   # Type in your name
  author_email = 'ishu.111636@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/IshuSinghSE',   # Provide either the link to your github or to your website
  download_url = f'https://github.com/IshuSinghSE/djangolazy/archive/refs/tags/v.{version}.tar.gz',    # I explain this later on
  keywords = ['django', 'setup', 'autosetup','setupscript'],   # Keywords that define your package best
  python_requires= '>=3.7',
  entry_points='djangolazy = djangolazy:version',
  install_requires=[
            'urllib3',
            ],
  classifiers=[
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: Microsoft :: Windows',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
  ],
  include_package_data=True,
      zip_safe=False
)
