# Movie Quote Twitter Bot [![Build Status](https://travis-ci.org/namelivia/movie-quote-twitter-bot.svg?branch=master)](https://travis-ci.org/namelivia/movie-quote-twitter-bot)

This is a Python script I made one day after work, it will pick random quotes from a provided movie and post them to Twitter as animated GIFs.

## Requeriments

* python3
* pip3

## Installation

Clone the project, navigate to its root folder and execute `pip3 install - e . --user` for installing it's dependencies.

## Configuration

Copy `movie_quote_twitter_bot/config.example.py` to `movie_quote_twitter_bot/config.py`

Then open the file with a text editor and replace the default values with your actual values.

* `subsURI`: Path of the .srt subs file. e.g. `/home/user/movies/movie.srt`
* `subsEncoding`: Encoding of the subs file. e.g. `utf-8-sig`, `latin-1`, etc... 
* `videoURI`: Path of the actual movie file. e.g. `/home/users/movies/movie.mkv`
* `outputURI`: Path where the GIF file that will be posted is stored. e.g. `/tmp/movie.gif`
* `consumerKey`: Your Twitter account consumer key.
* `consumerSecret`: Your Twitter account consumer secret.
* `accessTokenKey`: Your Twitter account access token key.
* `accessTokenSecret`: Your Twitter account access token secret.

## Usage

Just execute `movie_quote_twitter_bot/movie_quote_twitter_bot.py` and if everything is properly configured, a random movie quote will be posted to your Twitter account.

## Testing

For executing the tests just execute `python3 -m unittest discover` on the project's root folder.

## Contributing
Any suggestion, bug reports, or any other kind enhacements are welcome. Just [open an issue first](https://github.com/namelivia/movie-quote-twitter-bot/issues/new) for creating a PR remember this project has linting checkings so any PR should comply with them before beign merged, this checks will be automatically applied when opening or modifying the PR's.
