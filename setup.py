from setuptools import setup
import os


README = open(os.path.abspath('README.rst')).read()
HISTORY = open(os.path.abspath('HISTORY.rst')).read()


setup(
    name='certsling',
    version='0.9.0.dev0',
    description='Opinionated letsencrypt acme client working via a ssh port forward.',
    long_description="\n\n".join([README, HISTORY]),
    url='https://github.com/fschulze/certsling',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"],
    install_requires=[
        'click',
        'dnspython>=1.15.0',
        'pyOpenSSL',
        'requests'],
    entry_points={
        'console_scripts': ['certsling = certsling:main']},
    packages=['certsling'],
    package_dir={'': 'src'})
