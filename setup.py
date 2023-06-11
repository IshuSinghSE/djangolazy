from io import open
from setuptools import setup
from djangolazy import __version__ as version


setup(
  name = 'djangolazy',         # How you named your package folder (MyLib)
  packages = ['djangolazy'],   # Chose the same as "name"
  version = version,      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Script for initial django project setup',   # Give a short description about your library
  long_description = ''.join(open('README.md', encoding='utf-8').readlines()),
  long_description_content_type = "text/markdown",
  author = ' Ishu Singh',                   # Type in your name
  author_email = 'ishu.111636@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/IshuSinghSE',   # Provide either the link to your github or to your website
  download_url = f'https://github.com/IshuSinghSE/djangolazy/archive/refs/tags/v.{version}.tar.gz',    # I explain this later on
  keywords = ['django', 'setup', 'autosetup','setupscript'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
            'urllib3',
            ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.11',
  ],
)
