# Kassandra-Dashboard

# What is this

The Kassandra-Dashboard is a dashboard my team and I created with the intent to visualize covid data from the CDC, while also integrating an individualized risk calculator which has it's guidelines derived from several reputable sources. This project was initially our product at the end of a hackathon, which can be seen in my data_challenge repo. We built upon it substantially and got the results published, this is the result.

# Installation

If interested in running a local version, clone this repo and make sure to have pip installed.

Then, make a separate virtualenv like so (this example makes a virtual environment named venv at the given path):
python -m venv c:\path\to\myenv

copy the contents of the cloned repo into this new venv folder. Activate the venv like so:
cd venv\path\to\myenv\Scripts
then type "activate" and hit enter

The name of your venv should appear next to the command prompt. Now type:
cd ..

And finally:
pip install requirements.txt

Then, running the app/app.py file in your editor of choice will boot up a local Flask server, which you can then do as you please with.

Official website is located here:
kassandra-dashboard.herokuapp.com
