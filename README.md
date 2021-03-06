# Movie Quote Twitter Bot [![tag](https://img.shields.io/github/tag/namelivia/movie-quote-twitter-bot.svg)](https://github.com/namelivia/movie-quote-twitter-bot/releases) [![Build Status](https://travis-ci.org/namelivia/movie-quote-twitter-bot.svg?branch=master)](https://travis-ci.org/namelivia/movie-quote-twitter-bot) [![codecov](https://codecov.io/gh/namelivia/movie-quote-twitter-bot/branch/master/graph/badge.svg)](https://codecov.io/gh/namelivia/movie-quote-twitter-bot)


<p align="center">
  <img src="https://user-images.githubusercontent.com/1571416/52222505-f2374700-28a3-11e9-9cd7-7f03e9ca66ff.gif" alt="Example GIF" />
</p>

This is a Python script I made one day after work, it will pick random quotes from a provided movie and post them to Twitter as animated GIFs.

## Requeriments

* python3.7
* pipenv

## Installation

Clone the project, navigate to its root folder and execute `pipenv install` for installing it's dependencies.

## Configuration

To execute the script the following environment variables must be set.

* `CONSUMER_KEY`: Your Twitter account consumer key.
* `CONSUMER_SECRET`: Your Twitter account consumer secret.
* `ACCESS_TOKEN_KEY`: Your Twitter account access token key.
* `ACCESS_TOKEN_SECRET`: Your Twitter account access token secret.
* `SUBS_URI`: Path of the .srt subs file. e.g. `/home/user/movies/movie.srt`
* `SUBS_ENCODING`: Encoding of the subs file. e.g. `utf-8-sig`, `latin-1`, etc... 
* `VIDEO_URI`: Path of the actual movie file. e.g. `/home/users/movies/movie.mkv`
* `OUTPUT_URI`: Path where the GIF file that will be posted is stored. e.g. `/tmp/movie.gif`
* `TEXT_COLOR`: Color for the text that will be displayed e.g. `yellow`, `white`, etc...
* `TEXT_SIZE`: Font size for the text that will be displayed e.g. `18`
* `TEXT_FONT`: Font for the text that will be displayed e.g. `FreeSans-Negrita`
* `IDLE_PERIOD`: The number of seconds the script will wait before executing. e.g. `900`

## Usage

Just execute `pipenv run python main.py` and if everything is properly configured, a random movie quote will be posted to your Twitter account.

## Testing

For executing the tests just execute `pipenv run pytest` on the project's root folder.

## Docker deployment

A Docker image for a containerized development is included, when the container is running the bot will keep posting gifs. Find it on [DockerHub](https://hub.docker.com/r/namelivia/movie-quote-twitter-bot).

## Contributing
Any suggestion, bug reports, or any other kind enhacements are welcome. Just [open an issue first](https://github.com/namelivia/movie-quote-twitter-bot/issues/new) for creating a PR remember this project has linting checkings so any PR should comply with them before beign merged, this checks will be automatically applied when opening or modifying the PR's.
