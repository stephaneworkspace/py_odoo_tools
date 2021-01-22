from setuptools import setup, find_packages

setup(
    name='odoo_tools',
    version='0.1',
    license='MIT',
    author='stephane-bressani',
    author_email='s.bressani@bluewin.ch',
    url='http://www.stephane-bressani.ch',
    long_description="README.txt",

    # Sources
    packages = find_packages(),
    package_data = {
        'odoo_tools': [
            'resources/README.md',
            'resources/clap/*',
        ],
    },

#   package_data= {
#       "" : ["images/*.gif"]
#   },
#   data_files=[('images', ['images/hello.gif'])],

    description="Odoo tool",

    # Dependencies
    install_requires = ['clap==0.7'],
)
