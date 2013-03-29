kaleido - hacker news django clone
==================================

QUICK INSTALL
-------------

###Setup

1. Create virtual environment and install Django (v1.5 is recommneded)

	% mkvirtualenv kaleido
	% pip install django

2. Get the [source code][source] for the course
	
	a. Clone the repo

		% git clone git@github.com:Chasiepoo/kaleido.git
		% cd kaleido

3. Setup permissions

	% chmod +x manage.py

Sync DB

	% ./manage.py syncdb 		# setup an admin user
	% python loader.py 			# load in some stories (modify with your admin name)

Run Server

	% ./manage.py runserver

OTHER FUNCTIONS
---------------

If you want to have the static files collected

	% ./manage.py collectstatic

[source]: https://github.com/chasiepoo/kaleido/archive/master.zip