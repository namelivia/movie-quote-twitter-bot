from setuptools import setup

setup(
    name='python-twitter-movie-quote-bot',
    packages=['python-twitter-movie-quote-bot'],
    include_package_data=True,
    install_requires=[
        'moviepy',
        'srt',
        'python-twitter',
    ],
)
