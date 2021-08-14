# from distutils.core import setup, 
from setuptools import setup, find_packages
setup(
  name = 'MajorProblem_bot',        
  packages = find_packages(where="src"),
  package_dir={'': 'src'},   
  version = '0.0.3', license='MIT',        
  description = 'Looks for Reddit comments containg "major problem" and replies with a proper salute and "MAJOR PROBLEM"',
  author = 'Zach Cohn',                  
  author_email = 'mypythonexperiments@gmail.com',
  url = 'https://github.com/zachicecreamcohn/MajorProblem_bot',
  download_url = 'https://github.com/zachicecreamcohn/MajorProblem_bot/archive/refs/tags/0.0.1.tar.gz',    # I explain this later on
  keywords = ['Reddit', 'bot', 'humor'],  
  install_requires=[            # I get to this in a second
          'certifi==2021.5.30',
          'charset-normalizer==2.0.4',
          'click==8.0.1',
          'colorama==0.4.4',
          'idna==3.2',
          'pickleDB==0.9.2',
          'praw==7.4.0',
          'prawcore==2.3.0',
          'psaw==0.1.0',
          'requests==2.26.0',
          'update-checker==0.18.0',
          'urllib3==1.26.6',
          'websocket-client==1.2.1',
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
  ],
)
