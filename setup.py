from setuptools import setup
install_requires = {
    "time",
    "socket"
}
setup(name='jrpc.py',
      version='0.1',
      url='https://github.com/brokeboienige/jrpc.py',
      license='MIT',
      author='brokeboienige',
      author_email='enige@protonmail.com',
      description='A easy to use python library for Xx jAmes t xX\'s Xbox 360 JRPC plugin.',
      packages=['jrpc'],
      long_description=open('README.md').read(),
      zip_safe=False)
