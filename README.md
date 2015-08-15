# itineraryBuilder
1. Given basic details about a plan build an entire itinerary (Ex: Rental Car/ Hotel/Activities/ etc).
We often have this usecase where everyone wants to plan an entire trip but they do not exactly know the best
time or the best route to cover maximum things or what hotels/airbnb would be better if the preferences differ
from the usual ones found online. Even after finalizing the plans we often face the daunting task of syncing lot 
of things like rental car time, different hotel bookings and plan the hotels accordingly based on the nearest
distance to the next day's activity.
All this things are technogically solvable and we believe can help users plan a painless itinerary with a set budget 
and activity preference.

We also believe lot of users face problems digging out booking information regarding Rental Cars/ Baording Pass from 
Email / specific Apps and search a different App for activities etc, so this app would be one stop solution for all these 
use cases making your trip a delight.

Installation instructions:

Step 1: Add SSH key to your git account.
	ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
	eval "$(ssh-agent -s)"
	ssh-add ~/.ssh/id_rsa
	pbcopy < ~/.ssh/id_rsa.pub
	
	Now add the key to you git account.
	Test the connection using : ssh -T git@github.com

Step 2: Fork the repo
Step 3: Make changes and submit a PR.

WELCOME !
=======
Basic Setup For Python:
1. Once you clone the repo. It has the environment and related django files which should work without any dependencies.
2. You should see itinerary folder in your cloned directory.
3. Navigate to itinerary folder (ls itinerary) and you should see a manage.py file there.
4. Run this command to start your django server
   ==  python manage.py runserver ==
5. Now you can see the basic server view at http://127.0.0.1:8000/home in your browser.

== Linux Setup ==
1. Install pip (sudo apt-get install python-pip)
2. Install django (sudo apt-get install django)
3. Run Server (python manage.py runserver)
4. Go to first page built (http://127.0.0.1:8000/home

