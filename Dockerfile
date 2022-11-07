FROM python:3.8-alpine AS builder
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

FROM builder AS development
RUN pipenv install --dev

FROM builder AS production
RUN pipenv install
CMD ["pipenv", "run", "python", "main.py"]
