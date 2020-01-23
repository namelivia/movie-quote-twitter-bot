FROM python:3.7-alpine
WORKDIR /app
COPY . /app
RUN pip install -e .
CMD ["python", "movie_quote_twitter_bot/movie_quote_twitter_bot.py"]
