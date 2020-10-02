# BassTromboneSpecs
This repository has the code for [www.basstrombonespecs.com](https://www.basstrombonespecs.com).

---

### Why I made [www.basstrombonespecs.com](https://www.basstrombonespecs.com)
I've noticed that as musicians get better at their instruments, they also get a little more picky about their instruments.
For example, guitar players might only use certain strings on their guitars -- actually, they might also only play on guitars made from a certain brand.

Similarly, I've noticed some bass trombone players prefer certain specs over others, so that's where [www.basstrombonespecs.com](https://www.basstrombonespecs.com) comes in.
It's a website with many bass trombones and their specs, and you can filter out trombones by selecting which specs you're looking for.
Ideally, the website should make the process of finding a bass trombone with your desired specs much easier.
Without the website, you'd have to individually go to each manufacturer's website and then click and scroll around to find the trombones that fit your desired specs.
With [www.basstrombonespecs.com](https://www.basstrombonespecs.com), you no longer need to do as much clicking and scrolling around on manufacturer's websites because the specs are all on one page.

---

### Some info about the code
The website is made using [Django](https://www.djangoproject.com), a Python web framework.
[Bootstrap](https://getbootstrap.com) is used to style the front-end design.

For the most part, I'd say this is a pretty standard (and simple) Django project -- in other words, if you understand how Django projects are structured, then the code should make sense.

If you really inspect the code thoroughly, you'll notice I'm also using Google Analytics and reCAPTCHA.

##### The InitialData folder
The `InitialData` folder is probably the one thing that sticks out from the "standard" Django project.
The `InitialData` folder holds the CSV files and the Python script used to initially populate the database.

### Deployment and production
The website is hosted on [Heroku](https://www.heroku.com).
