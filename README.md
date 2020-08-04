[![Python 3.6](https://img.shields.io/badge/python-3.7.4-blue.svg)](https://www.python.org/downloads/release/python-360/)

# Django Blog with integrated ButterCMS

## Getting started
These instructions will get you a copy of the project up and running on your local machine for development purposes.

### Installation

Create virtual environment **blog_env**
```
python -m venv blog_env
```

Activate virtual environment
```
# On Windows in command line
blog_env/Scripts/activate

# In VSCode (Windows)
source blog_env/Scripts/activate
```

Clone the repository to created folder
```
cd blog_env
git clone https://github.com/orlyohreally/django-butterCMS-blog.git
```

Create .env file in the same location and with the same structure as .env.example file 

Install all the requirements for the project
```
cd django-butterCMS-blog
pip install -r requirements.txt
```

Run the development server
```
python manage.py runserver
```

The project will be available at http://127.0.0.1:8000/.

## Built with
* [Django](https://www.djangoproject.com/) - Python Web framework
* [ButterCMS](https://buttercms.com/) - headless CMS and blog engine

## Authors
* **Orly Knop** - [orlyohreally](https://github.com/orlyohreally)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details