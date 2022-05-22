from setuptools import setup


setup(
    name='geojsonformer',
    version='0.1.0',    
    description='Easily create geojson files from shapely polygons',
    url='https://github.com/ArminasSid/geojsonformer',
    author='Arminas Šidlauskas',
    author_email='armis920@gmail.com',
    license='MIT Licence',
    packages=['geojsonformer'],
    install_requires=['Shapely>=1.2.2',
                      'numpy',                     
                      ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows :: Windows 10',        
        'Programming Language :: Python :: 3.10',
    ],
)
 