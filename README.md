# Grocery Cache

Grocery Cache is a web app that helps users manage their grocery list and budget in an effective and fast way.

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
pip install requirements.txt
```

This will install the required dependencies to your virtual environment
venv has been kept in gitignore to avoid uploading the modules

## Project Description:

Nowadays, amidst a hectic life, we don’t often have much time to spend on walking around the stores and refreshing our memories on what we need to buy. It is also very frustrating when we forget to buy an item once we have already completed the trip. Moreover, we also want to budget our spending effectively every time we go shopping so that we don’t go over the limit. Thus, it will be convenient if we have an app that can help us keep track of the groceries items we need to shop, as well as the budget limit on each of them. This is where our Grocery Cache app comes in.

This app will allow its users to create grocery lists and track when they’re running low on certain items. This will help them effectively plan their grocery trips. They will be able to set up recurring reminders to purchase regular-use items as well as budget their expenses. Additionally, this app will have a feature to create lists for specific recipes such as that of momos. We also want to extend this feature to growing specific plants and purchasing items such as fertilizers for them. With growing environmental concerns we thought this would be a fun and quirky way to spotlight plants and encourage users to grow one :)
