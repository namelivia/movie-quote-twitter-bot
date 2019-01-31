# Movie Quote Twitter Bot

This is a Python script I made one day after work, it will pick random quotes from a provided movie and post them to Twitter as animated GIFs.

## Requeriments

* python3
* pip3

## Installation

Clone the project, navigate to its root folder and execute `pip3 install -e . --user` for installing it's dependencies.

## Configuration

Copy `movie-quote-twitter-bot/config.example.py` to `movie-quote-twitter-bot/config.py` 

Then open the file with a text editor and replace the default values with your actual values.

 * `subsURI` : Path of the .srt subs file. e.g. `/home/user/movies/movie.srt`
 * `videoURI`: Path of the actual movie file. e.g. `/home/users/movies/movie.mkv`
 * `outputPath`: Path where the GIF file that will be posted is stored. e.g. `/tmp/movie.gif`
 * `consumerKey`: Your Twitter account consumer key.
 * `consumerSecret`: Your Twitter account consumer secret.
 * `accessTokenKey`: Your Twitter account access token key.
 * `accessTokenSecret`: Your Twitter account access token secret.

## Usage

Just execute `./run.py` and if everything is properly configured, a random movie quote will be posted to your Twitter account.
