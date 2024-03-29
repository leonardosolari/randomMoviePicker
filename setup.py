from setuptools import setup


setup(
    name='randomMoviePicker',
    version='0.1',
    author='Leonardo Solari', 
    author_email='leonardosolari67@gmail.com',
    url='https://github.com/leonardosolari/randomMoviePicker.git',
    scripts=['moviePicker.py'], 
    install_requires=[
        'certifi==2021.10.8',
        'charset-normalizer==2.0.12',
        'decorator==4.4.2',
        'greenlet==1.1.2',
        'idna==3.3',
        'imageio==2.16.0',
        'imageio-ffmpeg==0.4.5',
        'IMDbPY==2021.4.18',
        'lxml==4.9.1',
        'moviepy==1.0.3',
        'numpy==1.22.2',
        'parse-torrent-name==1.1.1',
        'Pillow==9.0.1',
        'proglog==0.1.9',
        'requests==2.27.1',
        'rtsimple==0.9.0',
        'SQLAlchemy==1.4.31',
        'tk==0.1.0',
        'tqdm==4.62.3',
        'urllib3==1.26.8'
    ],
)