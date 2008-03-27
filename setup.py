from setuptools import setup, find_packages
import os

kws = {}
if not int(os.getenv( 'DISABLE_INSTALL_REQUIRES','0' )):
    kws['install_requires'] = [
        'numpy>=1.0.4',
        'wxPython>=2.8',
        'motmot.imops>=0.5.2.dev'
        ]

setup(name='motmot.FlyMovieFormat',
      description='support for .fmf (fly movie format) files',
      long_description = """'Fly movie format' (or .fmf) files are a
simple, uncompressed video format for storing data from digital video
cameras. A fixed-size per frame means that random access is extremely
fast, and a variety of formats (e.g. MONO8, YUV422) are supported.

This is a subpackage of the motmot family of digital image utilities.
""",
      version='0.5.2',
      author='Andrew Straw',
      author_email='strawman@astraw.com',
      license='BSD',
      url='http://code.astraw.com/projects/motmot',
      namespace_packages = ['motmot'],
      packages = find_packages(),
      package_data = {'motmot.FlyMovieFormat':['playfmf.xrc',
                                               'matplotlibrc',
                                               'test_raw8.fmf',
                                               'test_mono8.fmf',
                                               'description.txt']},
      entry_points = {
    'console_scripts': ['fmf2bmps = motmot.FlyMovieFormat.fmf2bmps:main',
                        'fmf_collapse = motmot.FlyMovieFormat.fmf_collapse:main',
                        'fmf_info = motmot.FlyMovieFormat.fmf_info:main',
                        ],
    'gui_scripts': ['playfmf = motmot.FlyMovieFormat.playfmf:main',
                    'fmf_plottimestamps = motmot.FlyMovieFormat.fmf_plottimestamps:main',
                    ],
    'motmot.FlyMovieFormat.exporter_plugins':['txt = motmot.FlyMovieFormat.playfmf:TxtFileSaverPlugin',
                                              'fmf = motmot.FlyMovieFormat.playfmf:FmfFileSaverPlugin',
                                              'image_sequence = motmot.FlyMovieFormat.playfmf:ImageSequenceSaverPlugin',
                                       ],
    },
      **kws)
