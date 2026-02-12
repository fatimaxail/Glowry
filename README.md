# Glowry

## Idea description
Glowry is a skincare-focused web application that helps users manage and personalize their skincare journey. The app allows users to create skin profiles, build step-by-step skincare routines, and write reviews for skincare products retrieved from a free third-party API, including detailed ingredient information. In addition, users can read and publish skincare articles to learn more about effective skincare practices. By combining personalized profiles, routine planning, and real product data, Glowry supports informed and mindful skincare decisions through a simple and user-friendly platform.

#### Logo:
![App Logo](https://i.postimg.cc/CxpP5Lqp/serum.png)

## App ERD
![App ERD](https://i.postimg.cc/509QwyrX/Screenshot-2026-02-12-at-2-12-28-AM.png)

## Trello board link
[Trello Board](https://trello.com/invite/b/696fba02e3cec67777086c18/ATTI394029c331fa112edaabe0ce76b85453BAF23E73/glowry)

## App wireframe
[App wireframe](https://www.figma.com/make/wf4XOqsVhlKytR6IQIy02P/Skincare-App-Wireframe?t=RynT5inf7po8ErA2-1)

## Deployment  Link

[Glowry](https://glowry.onrender.com)

## Screenshots of the APP
Home Page
![home page](https://i.postimg.cc/XqKh8gQC/Screenshot-2026-02-11-at-7-49-01-PM.png)

Product Page
![Product page](https://i.postimg.cc/05mqjYdg/Screenshot-2026-02-11-at-7-48-24-PM.png)

Routine Page
![Article page](https://i.postimg.cc/pLcSqrYG/Screenshot-2026-02-11-at-7-49-20-PM.png)

## Future enhancements
* doing the drag and drop for the products in the routine.
* adding the product to the routine from the product detail page.
* add products and article to the Favorites.
* doing a skin tracker.

## Technologies used
* Django
* Python
* Pillow

## Resources
<details>
  <summary><strong>Profile resources</strong></summary>
  <a href="https://dev.to/earthcomfy/django-user-profile-3hik">
      Django - User Profile
  </a>
  <br>
  <a href="https://docs.djangoproject.com/en/6.0/ref/contrib/postgres/fields/">
      ArrayField(for multi select)
  </a>
   <br>
  <a href="https://www.geeksforgeeks.org/python/multiplechoicefield-django-forms/">
     MultipleChoiceField - Django Forms
  </a>
   <br>
  <a href="https://www.geeksforgeeks.org/python/aggregate-vs-annotate-in-django/">
     Aggregation and Annotation in Django(profile count written reviews and articles)
  </a>
</details>

<details>
  <summary><strong>Loading JSON File resources</strong></summary>
    <a href="https://www.geeksforgeeks.org/python/json-load-in-python/?utm_source=chatgpt.com">
      json.load() in Python
  </a>
  <br>
  <a href="https://hackmd.io/@HyC-1029/B1UOvyIJWe#%E4%BB%A5json%E5%81%9A%E8%B3%87%E6%96%99%E5%BA%AB">
      Using JSON as a database
  </a>
   <br>
   <a href="https://coderivers.org/blog/python-reading-a-json-file/">
      Python Reading JSON Files: A Comprehensive Guide
  </a>
</details>

<details>
  <summary><strong>General resources</strong></summary>
   <a href="https://docs.djangoproject.com/en/3.2/ref/forms/fields/#modifying-querysets-in-init">
      Fields
  </a>
  <br>
   <a href="https://docs.djangoproject.com/en/3.2/ref/forms/fields/#modifying-querysets-in-init">
      QuerySet
  </a>
   <br>
    <a href="https://www.geeksforgeeks.org/python/what-does-super-__init__args-kwargs-do-in-python/">
     What Does Super().__Init__(*Args, **Kwargs) Do in Python?
  </a>
</details>


<details>
  <summary><strong>Search bar resources</strong></summary>
  <a href="https://dev.to/foxy4096/implementing-search-in-django-fbv-27c1">
      Implementing search in Django
  </a>
  <br>
  <a href="https://friskycodeur.hashnode.dev/implementing-search-functionality-in-your-django-website">
      Implementing Search functionality in your Django website
  </a>
</details>


<details>
  <summary><strong>Pagination resources</strong></summary>
  <a href="https://docs.djangoproject.com/en/6.0/topics/pagination/">
      Pagination Documentation
  </a>
  <br>
  <a href="https://dev.to/merichard123/django-diaries-pagination-1i0i">
      Django Diaries - Pagination
  </a>
</details>

<details>
  <summary><strong>Styling resources</strong></summary>
   <a href="https://materializecss.com/grid.html">
      Materialize CSS
  </a>
    <br>
  <a href="https://fontawesome.com/">
      Fontawesome- icons
  </a>
</details>

<details>
  <summary><strong>ckeditor resources</strong></summary>
  <a href="https://pypi.org/project/django-ckeditor-5/">
      django-ckeditor-5 0.2.19
  </a>
    <br>
   <a href="https://www.geeksforgeeks.org/python/richtextfield-django-models/">
      RichTextField - Django Models
  </a>
</details>

<details>
  <summary><strong>Model resources</strong></summary>
  <a href="https://stackoverflow.com/questions/42425933/how-do-i-set-a-default-max-and-min-value-for-an-integerfield-django">
      How do I set a default, max and min value for an integerfield Django?
  </a>
  <br>
  <a href="https://www.geeksforgeeks.org/python/how-to-add-created-at-and-updated-at-fields-to-all-django-models-using-timestampedmodel/">
      How to Add created_at and updated_at Fields to All Django Models Using TimeStampedModel
  </a>
</details>

<details>
  <summary><strong>Ordering the products in the routine resources</strong></summary>
  <a href="https://docs.python.org/3/howto/sorting.html">
      Sorting Techniques
  </a>
  <br>
  <a href="https://www.geeksforgeeks.org/python/python-lambda-anonymous-functions-filter-map-reduce/">
      Python Lambda Functions
  </a>
</details>

<details>
  <summary><strong>Reviews Stars</strong></summary>
   <a href="https://youtu.be/p59si_el1FU?si=25mIcRoiWD9BxWxc">
     Display Rating Stars
  </a>
   <br>
  <a href="https://youtu.be/v9Dd556pF3Q?si=3RPnjeXBr1kN4Wm8">
    Making Rating Stars
  </a>
</details>
