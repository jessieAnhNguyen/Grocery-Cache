# Grocery Cache
A web app that allows users to manage their grocery list and budget expenses efficiently and effectively.  

## Information for collaborators:

Please clone this repository https://github.com/jessieAnhNguyen/Grocery-Cache.git
From the terminal of the project directory from the terminal, type the following commands

1. Install the virtual environment called venv:

```
python3 -m venv venv
```

2. Switch to the environment

```
- (MAC) : source venv/bin/activate
- (Windows) : venv\Scripts\activate
```

3. Do the following to set the app (if the main file name is different from app.py)

```
- (MAC) : export FLASK_APP=app.py
- (Windows) : set FLASK_APP=app.py
```

4. Use debug (DEV) mode

```
- (MAC) : export FLASK_ENV=development
- (Windows) : set FLASK_ENV=development
```

5. Install the required dependencies:

```
pip install -r requirements.txt
```

This will install the required dependencies to your virtual environment
venv has been kept in gitignore to avoid uploading the modules

6. Run the project:

```
flask run
```

If you install more dependencies, please update the requirements.txt by

```
pip freeze > requirements.txt
```

## Project Description:

Given our busy lifestyles, it can be inconvenient to purchase groceries without a list or create an ill-organised one on the fly using the notes app on our phones. It can also be rather frustrating to forget to purchase an important item during a shopping trip or over-spending by purchasing items already present in your refrigerator/ pantry. We, therefore, want to create a web application that effectively allows users to create grocery lists and manage their grocery expenses. “Grocery Cache” will enable users to do just that with its simple design and useful functionality. It will allow users to create generic grocery lists, lists specific to particular recipes, set up recurring reminders to purchase regular-use items, and effectively budget their expenses.
