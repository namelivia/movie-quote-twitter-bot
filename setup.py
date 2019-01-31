from setuptools import setup

setup(
    name='MovieQuoteTwitterBot',
    author='José Ignacio Amelivia Santiago',
    author_email='jignacio.amelivia@gmail.com',
    url='https://namelivia.com',
    description='This is a small python bot for posting movie quotes',
    license='LICENSE',
    long_description=open('README.md').read(),
    packages=['movie_quote_twitter_bot'],
    include_package_data=True,
    install_requires=[
        'moviepy >= 0.2',
        'srt >= 1.9',
        'python-twitter >= 3.5',
    ],
)
