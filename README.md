# BookShare

The idea is to develop a book sharing social media website and mobile application similar to GoodReads.

Users can
* Download books
* Read books online
* Write reviews for books
* Rate books
* Share what books they are reading
* Create a virtual bookshelf
* Add other users as friends
* Recommend books to friends
* Create collection of books
* Search for books based on genre, author, recommendations
* Use a catalog of books (opds.io)
* View most downloaded and trending books
* Register their kindle email and send books directly to kindle through the website

Admin users can
* Add books


## Start Server
To start the server run
* Install the requirements
`pip install -r requirements.txt`


* Run the migrations
`python manage.py makemigrations`
`python manage.py migrate`

* Create a superuser
`python manage.py createsuperuser`

* Start the server
`python manage.py runserver`
