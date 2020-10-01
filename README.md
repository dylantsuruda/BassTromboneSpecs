# BassTromboneSpecs
This repository has the code for [www.basstrombonespecs.com](https://www.basstrombonespecs.com).

---

## Why I made [www.basstrombonespecs.com](https://www.basstrombonespecs.com)
I've noticed that as musicians get better at their instruments, they also get a little more picky about their instruments.
For example, guitar players might only use certain strings on their guitars -- actually, they might also only play on guitars made from a certain brand.

Similarly, I've noticed some bass trombone players prefer certain specs over others, so that's where [www.basstrombonespecs.com](https://www.basstrombonespecs.com) comes in.
It's a website with many bass trombones and their specs, and you can filter out trombones by selecting which specs you're looking for.
Ideally, the website should make the process of finding a bass trombone with your desired specs much easier.
Without the website, you'd have to individually go to each manufacturer's website and then click and scroll around to find the trombones that fit your desired specs.
With the website, you no longer need to do as much clicking and scrolling around on manufacturer's websites because the specs are all on one page.

---

## Some info about the code
The website is made using [Django](https://www.djangoproject.com), a Python web framework.
[Bootstrap](https://getbootstrap.com) is used to style the front-end design.

For the most part, I'd say this is a pretty standard (and simple) Django project -- in other words, if you understand how Django projects are structured, then the code should make sense.

If you really inspect the code thoroughly, you'll notice I'm also using Google Analytics and reCAPTCHA.

### The InitialData folder
The `InitialData` folder is probably the one thing that sticks out from the "standard" Django project.
The `InitialData` folder holds the CSV files and the Python script used to initially populate the database.

## Deployment and production
The website is hosted on [Heroku](https://www.heroku.com).

---

## If you want to run the code on your local machine
If you want to run the code locally on your local machine (like on *127.0.0.1* or *localhost*), then you can follow these instructions.
I'm assuming you have an understanding of Django -- it's somewhat out of the scope of this README to explain how and why certain things need to be done with Django.

1. Download/get the code onto your local machine. You should also create a Python virtual environment to run this project as using virtual environments is good Python practice.
2. Install the dependencies. Run this command in the same directory with the `requirements.txt` file:
   ```
   $ pip install -r requirements.txt
   ```
3. This step is going to be pretty vague, but you now need to set up the database. You'll have to figure out how to do that yourself. I'm using a Postgres database locally for development, but I think you could use SQLite by creating a `db.sqlite3` in the same directory as the `manage.py` file and then connect the Django code to the SQLite database. More information can be found [here](https://docs.djangoproject.com/en/3.1/intro/tutorial02/#database-setup) and [here](https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-DATABASES).
4. I imagine you'll also have to create environment variables for the `SECRET_KEY` and `DEBUG` values in the `settings.py` file. This step is should make sense if you understand Django.
5. You should now be able to migrate the Django migrations. Run this command in the same directory with the `manage.py` file:
   ```
   $ python manage.py migrate
   ```
   You should get an error after running the above command -- this is because the *specs 0010* migration has an error (which is because I made a mistake while editing my models).
   Run this command to fake the *specs 0010* migration:
   ```
   $ python manage.py migrate specs 0010 --fake
   ```
   Then run this command to complete the migrations:
   ```
   $ python manage.py migrate
   ```
6. I'm now pretty sure you can run this command:
   ```
   $ python manage.py runserver
   ```
   The website should now be running locally, and you should be able to access it at *127.0.0.1:8000* or at *localhost:8000*. If errors have popped up, then it's my hope that you understand Django and can figure out how to resolve those errors.
7. But wait, if you have gotten it run locally, you'll notice there's no data. To add the data into the database, run this command:
   ```
   $ python manage.py shell
   ```
   You should now have the Python interpreter running. In the interpreter, run this:
   ```
   >>> exec(open("InitialData/importcsvdata.py").read())
   ```
   You should now have the data in the database, and after refreshing the page, you'll see the specs populate on your website that's running locally.

Again, if the instructions to run locally are not working for you, my best hope is that you can resolve the errors yourself. You could also leave an issue in this GitHub repo (although I do understand that's not exactly what GitHub issues are for), and I might be able to help you.
