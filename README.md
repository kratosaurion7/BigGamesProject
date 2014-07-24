BigGamesProject
===============

Setup for Python
----------------

### Python3 vs Python2 ###
I'm using Python 3.3 right now. I chose 3.3 because I like coding with the newest version of whatever language I'm using. 

I acknowledge that 2.x is more standard than the 3.x branch and if I hit *any* wall with Python3 I will switch to 2.7 version. I plan on adding multiplayer with a MessageQueue server (RabbitMQ) using the 'pika' library. The problem right now is that pika is only supported on 2.7 and I don't like the other libraries. I found the python3 port of pika but I have inconsistencies with it. But anyway, multiplayer version of the games is still quite far away.

### PreReqs ###
Here are the steps to get the program up and running (Only Pong is in the repo so far)

0. Make sure Python3.3 and Python2.7 are installed. Make sure your path points to Python3.3. Install the pip package manager too. Check out this [StackOverflow answer](http://stackoverflow.com/questions/4750806/how-to-install-pip-on-windows) on how to install pip.

1. Checkout the repository.

2. Look in the Support Files folder and install pygame for both Python versions.