from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='oktaloginagain',
      install_requires=['lxml', 'requests'],
      version='0.3.0',
      description='Okta login made easy from the command line without API token',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/fprimex/okta-login-again',
      author='Brent W. Woodruff',
      author_email='brent@brentwoodruff.com',
      license='MIT',
      packages=['oktaloginagain'],
      classifiers=(
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
      ),)
