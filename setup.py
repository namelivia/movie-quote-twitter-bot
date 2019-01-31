from setuptools import setup

setup(
    name='movie-quote-twitter-bot',
    packages=['movie-quote-twitter-bot'],
    include_package_data=True,
    install_requires=[
        'moviepy',
        'srt',
        'python-twitter',
    ],
)
