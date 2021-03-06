FROM python:3.7-alpine
RUN apk add --no-cache gcc\
	ffmpeg\
	imagemagick\
	zlib-dev\
	jpeg-dev\
	ttf-freefont\
	musl-dev
WORKDIR /app
COPY . /app
RUN pip install pipenv
RUN pipenv install
CMD ["pipenv", "run", "python", "main.py"]
