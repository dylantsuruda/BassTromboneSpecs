# BassTromboneSpecs
This repository has the code for [www.basstrombonespecs.com](https://www.basstrombonespecs.com).

---

## Some info about the code
The website was made using [Django](https://www.djangoproject.com), a Python web framework.
[Bootstrap](https://getbootstrap.com) was used to style the front-end design.

For the most part, I'd say this is a pretty standard (and simple) Django project -- in other words, if you understand how Django projects are structured, then my code should make sense.

If you really inspect the code thoroughly, you'll notice I'm also using Google Analytics and reCAPTCHA.

## The InitialData folder
The `InitialData` folder is probably the one thing that sticks out from the "standard" Django project.
The `InitialData` folder holds the CSV files and the Python script used to initially populate the database.

## Deployment and production
The website is hosted on [Heroku](https://www.heroku.com).
