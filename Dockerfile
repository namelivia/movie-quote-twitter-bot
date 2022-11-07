FROM python:3.8-alpine AS builder
WORKDIR /app
COPY . /app
RUN apk update
RUN apk add --no-cache gcc\
	ffmpeg\
	imagemagick\
	zlib-dev\
	jpeg-dev\
	ttf-freefont\
	musl-dev
RUN pip install -I pipenv==2022.10.25

FROM builder AS development
RUN pipenv install --dev

FROM builder AS production
RUN pipenv install
# CMD ["pipenv", "run", "python", "main.py"]
