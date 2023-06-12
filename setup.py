from distutils.core import setup
from djangolazy.__init__ import __version__
with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setup(
  name = 'djangolazy',         # How you named your package folder (MyLib)
  packages = ['djangolazy'],   # Chose the same as "name"
  version = f'{__version__}',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Script for initial django project setup',   # Give a short description about your library
  long_description = long_description,
  long_description_content_type = "text/markdown",
  author = ' Ishu Singh',                   # Type in your name
  author_email = 'ishu.111636@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/IshuSinghSE',   # Provide either the link to your github or to your website
  download_url = f'https://github.com/IshuSinghSE/djangolazy/archive/refs/tags/v.{__version__}.tar.gz',    # I explain this later on
  keywords = ['django', 'setup', 'autosetup','setupscript'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
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
