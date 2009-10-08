from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='AWSECommerceClient',
      version=version,
      description="Client to the Amazon AWSECommerceService",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='Amazon AWS ECommerce',
      author='Jonathan Gardner',
      author_email='jgardner@jonathangardner.net',
      url='http://tech.jonathangardner.net/Python/AWSECommerceService',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
