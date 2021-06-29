# RTX 3070 Best Buy Bot

## Features
- Automatically refreshes product page until available then completes the checkout process

## Prerequisites
- Sign up for a Best Buy account
- Ensure that only one card is on your account
- Add shipping address to your account

## Dependencies
- [Python 3.9](https://www.python.org/downloads/release/python-390/)
- [pipenv](https://pypi.org/project/pipenv/)
- [Google Chrome](https://www.google.com/chrome/)
- [ChromeDriver](https://chromedriver.chromium.org/downloads)
	- Extract the compressed chromedriver executable to a directory of your choice

## Running the Bot
1. Navigate to project directory
2. Copy `.env.example` to `.env` and replace the example data with your own
3. Install python dependencies (this will create a new virtual environment when run for the first time)
	```sh
	pipenv sync
	```
4. Enter environment
	```sh
	pipenv shell
	```
5. Run application
	```sh
	python bot.py
	```
