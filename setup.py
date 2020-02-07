from setuptools import setup
from src.PyTkBindings.__version__ import version




data_files = [
        'PySwitchCase/*.py'
        ]
setup(
        name='PyTkBindings',
        version=version,
        packages=['PyTkBindings'],
        url='https://github.com/Jakar510/PySwitchCase',
        download_url='https://github.com/Jakar510/PythonTkinterBindings/',
        license='GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007',
        author='Tyler Stegmaier',
        author_email='tyler.stegmaier.510@gmail.com',
        description='All Python Tkinter Bindings and helper functions.',
        install_requires=[],
        classifiers=[
            # How mature is this project? Common values are
            #   3 - Alpha
            #   4 - Beta
            #   5 - Production/Stable
            'Development Status :: 3 - Alpha',

            # Indicate who your project is intended for
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Build Tools',

            # Pick your license as you wish
            'License :: Free To Use But Restricted',

            # Support platforms
            'Operating System :: MacOS',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX',

            'Programming Language :: Python :: 3',
        ],
        keywords='bind tkinter-binding binding tkinter-bind python-tkinter python-tkinter-binding python-tkinter-bind',
        package_dir={'PyTkBindings': 'src/PyTkBindings'},
        package_data={
                'PyTkBindings': data_files,
            },
        )

