from setuptools import setup, find_packages

requires = [
  'flask',
  'flask-sqlalchemy',
  'psycopg2',
]

setup(
  name='barax',
  version='0.0',
  description='Guild management website for World of Warcraft',
  author='Tristan Brooks',
  author_email='3stanbrooks@gmail.com',
  keywords='web flask',
  packages=find_packages(),
  include_package_data=True,
  install_requires=requires
)