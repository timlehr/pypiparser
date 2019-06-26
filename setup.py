# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(name='pypiparser',
      author="Tim Lehr",
      packages=find_packages(exclude=['tests']),
      license='MIT',
      description='Simple Python Package Index Parser',
      author_email='contact@timlehr.com',
      url='https://github.com/timlehr/pypiparser',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      keywords=['pypi', 'parser', 'packaging', 'simple', "pip"],
      include_package_data=True,
      use_scm_version=True,
      setup_requires=['setuptools_scm'],
      install_requires=[
          'beautifulsoup4',
          'requests'
      ],
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
      ]
)
