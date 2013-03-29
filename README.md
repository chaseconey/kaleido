# kaleido - hacker news django clone

## Quick Install

### Setup

1. Create virtual environment and install Django (v1.5 is recommneded)

		% mkvirtualenv kaleido
		% pip install django

2. Get the [source code][source] for the course
	
	a. Clone the repo

		% git clone git@github.com:Chasiepoo/kaleido.git
		% cd kaleido

3. Setup permissions

		% chmod +x manage.py

4. Sync DB

		% ./manage.py syncdb 		# setup an admin user
		% python loader.py 			# load in some stories (modify with your admin name)

5. Run Server

		% ./manage.py runserver

## Other Functions

If you want to have the static files collected

		% ./manage.py collectstatic

[source]: https://github.com/chasiepoo/kaleido/archive/master.zip