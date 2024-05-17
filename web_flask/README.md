# 0x04. AirBnB clone - Web framework

Python Back-end Webserver Flask


Write a script that starts a Flask web application:

-   Your web application must be listening on `0.0.0.0`, port `5000`
-   Routes:
    -   `/`: display “Hello HBNB!”
-   You must use the option `strict_slashes=False` in your route definition

```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.0-hello_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000 ; echo "" | cat -e
Hello HBNB!$
guillaume@ubuntu:~$ 
```

**Repo:**

-   GitHub repository: `AirBnB_clone_v2`
-   Directory: `web_flask`
-   File: `0-hello_route.py, __init__.py`

Done? Get a sandbox

### 1\. HBNB

mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on `0.0.0.0`, port `5000`
-   Routes:
    -   `/`: display “Hello HBNB!”
    -   `/hbnb`: display “HBNB”
-   You must use the option `strict_slashes=False` in your route definition

```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.1-hbnb_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
HBNB$
guillaume@ubuntu:~$ 
```

**Repo:**

-   GitHub repository: `AirBnB_clone_v2`
-   Directory: `web_flask`
-   File: `1-hbnb_route.py`

Done? Get a sandbox

### 2\. C is fun!

mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on `0.0.0.0`, port `5000`
-   Routes:
    -   `/`: display “Hello HBNB!”
    -   `/hbnb`: display “HBNB”
    -   `/c/<text>`: display “C ” followed by the value of the `text` variable (replace underscore `_` symbols with a space )
-   You must use the option `strict_slashes=False` in your route definition

```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.2-c_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/is_fun ; echo "" | cat -e
C is fun$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/cool ; echo "" | cat -e
C cool$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c
&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"&gt;
&lt;title&gt;404 Not Found&lt;/title&gt;
&lt;h1&gt;Not Found&lt;/h1&gt;
&lt;p&gt;The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.&lt;/p&gt;
guillaume@ubuntu:~$ 
```

**Repo:**

-   GitHub repository: `AirBnB_clone_v2`
-   Directory: `web_flask`
-   File: `2-c_route.py`

Done? Get a sandbox

### 3\. Python is cool!

mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on `0.0.0.0`, port `5000`
-   Routes:
    -   `/`: display “Hello HBNB!”
    -   `/hbnb`: display “HBNB”
    -   `/c/<text>`: display “C ”, followed by the value of the `text` variable (replace underscore `_` symbols with a space )
    -   `/python/<text>`: display “Python ”, followed by the value of the `text` variable (replace underscore `_` symbols with a space )
        -   The default value of `text` is “is cool”
-   You must use the option `strict_slashes=False` in your route definition

```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.3-python_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/is_magic ; echo "" | cat -e
Python is magic$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
Python is cool$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
Python is cool$
guillaume@ubuntu:~$ 
```

**Repo:**

-   GitHub repository: `AirBnB_clone_v2`
-   Directory: `web_flask`
-   File: `3-python_route.py`

Done? Get a sandbox

### 4\. Is it a number?

mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on `0.0.0.0`, port `5000`
-   Routes:
    -   `/`: display “Hello HBNB!”
    -   `/hbnb`: display “HBNB”
    -   `/c/<text>`: display “C ”, followed by the value of the `text` variable (replace underscore `_` symbols with a space )
    -   `/python/(<text>)`: display “Python ”, followed by the value of the `text` variable (replace underscore `_` symbols with a space )
        -   The default value of `text` is “is cool”
    -   `/number/<n>`: display “`n` is a number” **only** if `n` is an integer
-   You must use the option `strict_slashes=False` in your route definition

```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.4-number_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/89 ; echo "" | cat -e
89 is a number$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/8.9 
&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"&gt;
&lt;title&gt;404 Not Found&lt;/title&gt;
&lt;h1&gt;Not Found&lt;/h1&gt;
&lt;p&gt;The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.&lt;/p&gt;
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/python 
&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"&gt;
&lt;title&gt;404 Not Found&lt;/title&gt;
&lt;h1&gt;Not Found&lt;/h1&gt;
&lt;p&gt;The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.&lt;/p&gt;
guillaume@ubuntu:~$ 
```

**Repo:**

-   GitHub repository: `AirBnB_clone_v2`
-   Directory: `web_flask`
-   File: `4-number_route.py`

Done? Get a sandbox

### 5\. Number template

mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on `0.0.0.0`, port `5000`
-   Routes:
    -   `/`: display “Hello HBNB!”
    -   `/hbnb`: display “HBNB”
    -   `/c/<text>`: display “C ”, followed by the value of the `text` variable (replace underscore `_` symbols with a space )
    -   `/python/(<text>)`: display “Python ”, followed by the value of the `text` variable (replace underscore `_` symbols with a space )
        -   The default value of `text` is “is cool”
    -   `/number/<n>`: display “`n` is a number” **only** if `n` is an integer
    -   `/number_template/<n>`: display a HTML page **only** if `n` is an integer:
        -   `H1` tag: “Number: `n`” inside the tag `BODY`
-   You must use the option `strict_slashes=False` in your route definition

```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.5-number_template
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/89 ; echo ""
&lt;!DOCTYPE html&gt;
&lt;HTML lang="en"&gt;
    &lt;HEAD&gt;
        &lt;TITLE&gt;HBNB&lt;/TITLE&gt;
    &lt;/HEAD&gt;
    &lt;BODY&gt;
        &lt;H1&gt;Number: 89&lt;/H1&gt;
    &lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/8.9 
&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"&gt;
&lt;title&gt;404 Not Found&lt;/title&gt;
&lt;h1&gt;Not Found&lt;/h1&gt;
&lt;p&gt;The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.&lt;/p&gt;
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/python 
&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"&gt;
&lt;title&gt;404 Not Found&lt;/title&gt;
&lt;h1&gt;Not Found&lt;/h1&gt;
&lt;p&gt;The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.&lt;/p&gt;
guillaume@ubuntu:~$ 
```

**Repo:**

-   GitHub repository: `AirBnB_clone_v2`
-   Directory: `web_flask`
-   File: `5-number_template.py, templates/5-number.html`

Done? Get a sandbox

### 6\. Odd or even?

mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on `0.0.0.0`, port `5000`
-   Routes:
    -   `/`: display “Hello HBNB!”
    -   `/hbnb`: display “HBNB”
    -   `/c/<text>`: display “C ”, followed by the value of the `text` variable (replace underscore `_` symbols with a space )
    -   `/python/(<text>)`: display “Python ”, followed by the value of the `text` variable (replace underscore `_` symbols with a space )
        -   The default value of `text` is “is cool”
    -   `/number/<n>`: display “`n` is a number” **only** if `n` is an integer
    -   `/number_template/<n>`: display a HTML page **only** if `n` is an integer:
        -   `H1` tag: “Number: `n`” inside the tag `BODY`
    -   `/number_odd_or_even/<n>`: display a HTML page **only** if `n` is an integer:
        -   `H1` tag: “Number: `n` is `even|odd`” inside the tag `BODY`
-   You must use the option `strict_slashes=False` in your route definition

```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.6-number_odd_or_even
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/89 ; echo ""
&lt;!DOCTYPE html&gt;
&lt;HTML lang="en"&gt;
    &lt;HEAD&gt;
        &lt;TITLE&gt;HBNB&lt;/TITLE&gt;
    &lt;/HEAD&gt;
    &lt;BODY&gt;
        &lt;H1&gt;Number: 89 is odd&lt;/H1&gt;
    &lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/32 ; echo ""
&lt;!DOCTYPE html&gt;
&lt;HTML lang="en"&gt;
    &lt;HEAD&gt;
        &lt;TITLE&gt;HBNB&lt;/TITLE&gt;
    &lt;/HEAD&gt;
    &lt;BODY&gt;
        &lt;H1&gt;Number: 32 is even&lt;/H1&gt;
    &lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/python 
&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"&gt;
&lt;title&gt;404 Not Found&lt;/title&gt;
&lt;h1&gt;Not Found&lt;/h1&gt;
&lt;p&gt;The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.&lt;/p&gt;
guillaume@ubuntu:~$ 
```

**Repo:**

-   GitHub repository: `AirBnB_clone_v2`
-   Directory: `web_flask`
-   File: `6-number_odd_or_even.py, templates/6-number_odd_or_even.html`

Done? Get a sandbox

### 7\. Improve engines

mandatory

Before using Flask to display our HBNB data, you will need to update some part of our engine:

Update `FileStorage`: (`models/engine/file_storage.py`)

-   Add a public method `def close(self):`: call `reload()` method for deserializing the JSON file to objects

Update `DBStorage`: (`models/engine/db_storage.py`)

-   Add a public method `def close(self):`: call `remove()` method on the private session attribute (`self.__session`) [tips](https://intranet.alxswe.com/rltoken/_lTxhB5UgQ4nFRoS9ooI5g "tips") or `close()` on the class `Session` [tips](https://intranet.alxswe.com/rltoken/xlPf9pDUFMb599rkoDElvg "tips")

Update `State`: (`models/state.py`) - If it’s not already present

-   If your storage engine is not `DBStorage`, add a public getter method `cities` to return the list of `City` objects from `storage` linked to the current `State`

```
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 
&gt;&gt;&gt; from models import storage
&gt;&gt;&gt; from models.state import State
&gt;&gt;&gt; len(storage.all(State))
5
&gt;&gt;&gt; len(storage.all(State))
5
&gt;&gt;&gt; # Time to insert new data!
```

At this moment, in another tab:

```
guillaume@ubuntu:~/AirBnB_v2$ echo 'INSERT INTO `states` VALUES ("421a55f1-7d82-45d9-b54c-a76916479545","2017-03-25 19:42:40","2017-03-25 19:42:40","Alabama");' | mysql -uroot -p hbnb_dev_db
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ 
```

And let’s go back the Python console:

```
&gt;&gt;&gt; # Time to insert new data!
&gt;&gt;&gt; len(storage.all(State))
5
&gt;&gt;&gt; # normal: the SQLAlchemy didn't reload his `Session`
&gt;&gt;&gt; # to force it, you must remove the current session to create a new one:
&gt;&gt;&gt; storage.close()
&gt;&gt;&gt; len(storage.all(State))
6
&gt;&gt;&gt; # perfect!
```

And for the getter `cities` in the `State` model:

```
guillaume@ubuntu:~/AirBnB_v2$ cat main.py
#!/usr/bin/python3
"""
 Test cities access from a state
"""
from models import storage
from models.state import State
from models.city import City

"""
 Objects creations
"""
state_1 = State(name="California")
print("New state: {}".format(state_1))
state_1.save()
state_2 = State(name="Arizona")
print("New state: {}".format(state_2))
state_2.save()

city_1_1 = City(state_id=state_1.id, name="Napa")
print("New city: {} in the state: {}".format(city_1_1, state_1))
city_1_1.save()
city_1_2 = City(state_id=state_1.id, name="Sonoma")
print("New city: {} in the state: {}".format(city_1_2, state_1))
city_1_2.save()
city_2_1 = City(state_id=state_2.id, name="Page")
print("New city: {} in the state: {}".format(city_2_1, state_2))
city_2_1.save()


"""
 Verification
"""
print("")
all_states = storage.all(State)
for state_id, state in all_states.items():
    for city in state.cities:
        print("Find the city {} in the state {}".format(city, state))

guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ rm file.json ; HBNB_TYPE_STORAGE=fs ./main.py 
New state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509954), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New state: [State] (a5e5311a-3c19-4995-9485-32c74411b416) {'name': 'Arizona', 'id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510256), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}
New city: [City] (e3e36ded-fe56-44f5-bf08-8a27e2b30672) {'name': 'Napa', 'id': 'e3e36ded-fe56-44f5-bf08-8a27e2b30672', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510797), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510791)} in the state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New city: [City] (12a58d70-e255-4c1e-8a68-7d5fb924d2d2) {'name': 'Sonoma', 'id': '12a58d70-e255-4c1e-8a68-7d5fb924d2d2', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511437), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511432)} in the state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New city: [City] (a693bdb9-e0ca-4521-adfd-e1a93c093b4b) {'name': 'Page', 'id': 'a693bdb9-e0ca-4521-adfd-e1a93c093b4b', 'state_id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511873), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511869)} in the state: [State] (a5e5311a-3c19-4995-9485-32c74411b416) {'name': 'Arizona', 'id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510373), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}

Find the city [City] (e3e36ded-fe56-44f5-bf08-8a27e2b30672) {'name': 'Napa', 'id': 'e3e36ded-fe56-44f5-bf08-8a27e2b30672', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510953), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510791)} in the state [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
Find the city [City] (12a58d70-e255-4c1e-8a68-7d5fb924d2d2) {'name': 'Sonoma', 'id': '12a58d70-e255-4c1e-8a68-7d5fb924d2d2', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511513), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511432)} in the state [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
Find the city [City] (a693bdb9-e0ca-4521-adfd-e1a93c093b4b) {'name': 'Page', 'id': 'a693bdb9-e0ca-4521-adfd-e1a93c093b4b', 'state_id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 512073), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511869)} in the state [State] (a5e5311a-3c19-4995-9485-32c74411b416) {'name': 'Arizona', 'id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510373), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}
guillaume@ubuntu:~/AirBnB_v2$ 
```

**Repo:**

-   GitHub repository: `AirBnB_clone_v2`
-   File: `models/engine/file_storage.py, models/engine/db_storage.py, models/state.py`

Done?

### 8\. List of states

mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on `0.0.0.0`, port `5000`
-   You must use `storage` for fetching data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`
-   After each request you must remove the current SQLAlchemy Session:
    -   Declare a method to handle `@app.teardown_appcontext`
    -   Call in this method `storage.close()`
-   Routes:
    -   `/states_list`: display a HTML page: (inside the tag `BODY`)
        -   `H1` tag: “States”
        -   `UL` tag: with the list of all `State` objects present in `DBStorage` **sorted by `name`** (A->Z) [tip](https://intranet.alxswe.com/rltoken/2y_hunzGCCvSot06EW67UQ "tip")
            -   `LI` tag: description of one `State`: `<state.id>: <B><state.name></B>`
-   Import this [7-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql "7-dump") to have some data
-   You must use the option `strict_slashes=False` in your route definition

**IMPORTANT**

-   Make sure you have a running and valid `setup_mysql_dev.sql` in your `AirBnB_clone_v2` repository ([Task](https://intranet.alxswe.com/rltoken/v5CSUMU7FY9wj_cnBY7P1A "Task"))
-   Make sure all tables are created when you run `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`

```
guillaume@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.7-states_list
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/states_list ; echo ""
&lt;!DOCTYPE html&gt;
&lt;HTML lang="en"&gt;
    &lt;HEAD&gt;
        &lt;TITLE&gt;HBNB&lt;/TITLE&gt;
    &lt;/HEAD&gt;
    &lt;BODY&gt;
        &lt;H1&gt;States&lt;/H1&gt;
        &lt;UL&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479545: &lt;B&gt;Alabama&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479546: &lt;B&gt;Arizona&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;California&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479548: &lt;B&gt;Colorado&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479549: &lt;B&gt;Florida&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479550: &lt;B&gt;Georgia&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479551: &lt;B&gt;Hawaii&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Illinois&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479553: &lt;B&gt;Indiana&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479554: &lt;B&gt;Louisiana&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479555: &lt;B&gt;Minnesota&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479556: &lt;B&gt;Mississippi&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479557: &lt;B&gt;Oregon&lt;/B&gt;&lt;/LI&gt;

        &lt;/UL&gt;
    &lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ 
```

**Repo:**

-   GitHub repository: `AirBnB_clone_v2`
-   File: `web_flask/7-states_list.py, web_flask/templates/7-states_list.html`

Done? Get a sandbox

### 9\. Cities by states

mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on `0.0.0.0`, port `5000`
-   You must use `storage` for fetching data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`
-   To load all cities of a `State`:
    -   If your storage engine is `DBStorage`, you must use `cities` relationship
    -   Otherwise, use the public getter method `cities`
-   After each request you must remove the current SQLAlchemy Session:
    -   Declare a method to handle `@app.teardown_appcontext`
    -   Call in this method `storage.close()`
-   Routes:
    -   `/cities_by_states`: display a HTML page: (inside the tag `BODY`)
        -   `H1` tag: “States”
        -   `UL` tag: with the list of all `State` objects present in `DBStorage` **sorted by `name`** (A->Z) [tip](https://intranet.alxswe.com/rltoken/2y_hunzGCCvSot06EW67UQ "tip")
            -   `LI` tag: description of one `State`: `<state.id>: <B><state.name></B>` + `UL` tag: with the list of `City` objects linked to the `State` **sorted by `name`** (A->Z)
                -   `LI` tag: description of one `City`: `<city.id>: <B><city.name></B>`
-   Import this [7-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql "7-dump") to have some data
-   You must use the option `strict_slashes=False` in your route definition

**IMPORTANT**

-   Make sure you have a running and valid `setup_mysql_dev.sql` in your `AirBnB_clone_v2` repository ([Task](https://intranet.alxswe.com/rltoken/v5CSUMU7FY9wj_cnBY7P1A "Task"))
-   Make sure all tables are created when you run `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`

```
guillaume@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.8-cities_by_states
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/cities_by_states ; echo ""
&lt;!DOCTYPE html&gt;
&lt;HTML lang="en"&gt;
    &lt;HEAD&gt;
        &lt;TITLE&gt;HBNB&lt;/TITLE&gt;
    &lt;/HEAD&gt;
    &lt;BODY&gt;
        &lt;H1&gt;States&lt;/H1&gt;
        &lt;UL&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479545: &lt;B&gt;Alabama&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479545: &lt;B&gt;Akron&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479545: &lt;B&gt;Babbie&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479545: &lt;B&gt;Calera&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;551a55f4-7d82-47d9-b54c-a76916479545: &lt;B&gt;Fairfield&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479546: &lt;B&gt;Arizona&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479546: &lt;B&gt;Douglas&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479546: &lt;B&gt;Kearny&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479546: &lt;B&gt;Tempe&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;California&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;Fremont&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;551a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;Napa&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;San Francisco&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;San Jose&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;561a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;Sonoma&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479548: &lt;B&gt;Colorado&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479548: &lt;B&gt;Denver&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479549: &lt;B&gt;Florida&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479549: &lt;B&gt;Miami&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479549: &lt;B&gt;Orlando&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479550: &lt;B&gt;Georgia&lt;/B&gt;
                &lt;UL&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479551: &lt;B&gt;Hawaii&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479551: &lt;B&gt;Honolulu&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479551: &lt;B&gt;Kailua&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479551: &lt;B&gt;Pearl city&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Illinois&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Chicago&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;561a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Joliet&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Naperville&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Peoria&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;551a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Urbana&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479553: &lt;B&gt;Indiana&lt;/B&gt;
                &lt;UL&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479554: &lt;B&gt;Louisiana&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479554: &lt;B&gt;Baton rouge&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479554: &lt;B&gt;Lafayette&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479554: &lt;B&gt;New Orleans&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479555: &lt;B&gt;Minnesota&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479555: &lt;B&gt;Saint Paul&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479556: &lt;B&gt;Mississippi&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479556: &lt;B&gt;Jackson&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479556: &lt;B&gt;Meridian&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479556: &lt;B&gt;Tupelo&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479557: &lt;B&gt;Oregon&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479557: &lt;B&gt;Eugene&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479557: &lt;B&gt;Portland&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

        &lt;/UL&gt;
    &lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ 
```

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/9a7ae8155274b17881442200437e8793cf08de48.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240516T092812Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=fc8258263d6096d2f701eb38d65e4faa6fa89d0c01ee26a27609522d5602b919)

**Repo:**

-   GitHub repository: `AirBnB_clone_v2`
-   File: `web_flask/8-cities_by_states.py, web_flask/templates/8-cities_by_states.html`

Done? Get a sandbox

### 10\. States and State

mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on `0.0.0.0`, port `5000`
-   You must use `storage` for fetching data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`
-   To load all cities of a `State`:
    -   If your storage engine is `DBStorage`, you must use `cities` relationship
    -   Otherwise, use the public getter method `cities`
-   After each request you must remove the current SQLAlchemy Session:
    -   Declare a method to handle `@app.teardown_appcontext`
    -   Call in this method `storage.close()`
-   Routes:
    -   `/states`: display a HTML page: (inside the tag `BODY`)
        -   `H1` tag: “States”
        -   `UL` tag: with the list of all `State` objects present in `DBStorage` **sorted by `name`** (A->Z) [tip](https://intranet.alxswe.com/rltoken/2y_hunzGCCvSot06EW67UQ "tip")
            -   `LI` tag: description of one `State`: `<state.id>: <B><state.name></B>`
    -   `/states/<id>`: display a HTML page: (inside the tag `BODY`)
        -   If a `State` object is found with this `id`:
            -   `H1` tag: “State: ”
            -   `H3` tag: “Cities:”
            -   `UL` tag: with the list of `City` objects linked to the `State` **sorted by `name`** (A->Z)
                -   `LI` tag: description of one `City`: `<city.id>: <B><city.name></B>`
        -   Otherwise:
            -   `H1` tag: “Not found!”
-   You must use the option `strict_slashes=False` in your route definition
-   Import this [7-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql "7-dump") to have some data

**IMPORTANT**

-   Make sure you have a running and valid `setup_mysql_dev.sql` in your `AirBnB_clone_v2` repository ([Task](https://intranet.alxswe.com/rltoken/v5CSUMU7FY9wj_cnBY7P1A "Task"))
-   Make sure all tables are created when you run `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`

```
guillaume@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.9-states
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In another tab:

```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/states ; echo ""
&lt;!DOCTYPE html&gt;
&lt;HTML lang="en"&gt;
    &lt;HEAD&gt;
        &lt;TITLE&gt;HBNB&lt;/TITLE&gt;
    &lt;/HEAD&gt;
    &lt;BODY&gt;

        &lt;H1&gt;States&lt;/H1&gt;
        &lt;UL&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479545: &lt;B&gt;Alabama&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479546: &lt;B&gt;Arizona&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;California&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479548: &lt;B&gt;Colorado&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479549: &lt;B&gt;Florida&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479550: &lt;B&gt;Georgia&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479551: &lt;B&gt;Hawaii&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Illinois&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479553: &lt;B&gt;Indiana&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479554: &lt;B&gt;Louisiana&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479555: &lt;B&gt;Minnesota&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479556: &lt;B&gt;Mississippi&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479557: &lt;B&gt;Oregon&lt;/B&gt;&lt;/LI&gt;

        &lt;/UL&gt;

    &lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ curl 0.0.0.0:5000/states/421a55f4-7d82-47d9-b54c-a76916479552 ; echo ""
&lt;!DOCTYPE html&gt;
&lt;HTML lang="en"&gt;
    &lt;HEAD&gt;
        &lt;TITLE&gt;HBNB&lt;/TITLE&gt;
    &lt;/HEAD&gt;
    &lt;BODY&gt;

        &lt;H1&gt;State: Illinois&lt;/H1&gt;
        &lt;H3&gt;Cities:&lt;/H3&gt;
        &lt;UL&gt;
                &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Chicago&lt;/B&gt;&lt;/LI&gt;

                &lt;LI&gt;561a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Joliet&lt;/B&gt;&lt;/LI&gt;

                &lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Naperville&lt;/B&gt;&lt;/LI&gt;

                &lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Peoria&lt;/B&gt;&lt;/LI&gt;

                &lt;LI&gt;551a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Urbana&lt;/B&gt;&lt;/LI&gt;
        &lt;/UL&gt;

    &lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ curl 0.0.0.0:5000/states/holberton ; echo ""
&lt;!DOCTYPE html&gt;
&lt;HTML lang="en"&gt;
    &lt;HEAD&gt;
        &lt;TITLE&gt;HBNB&lt;/TITLE&gt;
    &lt;/HEAD&gt;
    &lt;BODY&gt;

        &lt;H1&gt;Not found!&lt;/H1&gt;

    &lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ 
```

**Repo:**

-   GitHub repository: `AirBnB_clone_v2`
-   File: `web_flask/9-states.py, web_flask/templates/9-states.html`

Done? Get a sandbox

### 11\. HBNB filters

mandatory

Write a script that starts a Flask web application:

-   Your web application must be listening on `0.0.0.0`, port `5000`
-   You must use `storage` for fetching data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`
-   To load all cities of a `State`:
    -   If your storage engine is `DBStorage`, you must use `cities` relationship
    -   Otherwise, use the public getter method `cities`
-   After each request you must remove the current SQLAlchemy Session:
    -   Declare a method to handle `@app.teardown_appcontext`
    -   Call in this method `storage.close()`
-   Routes:
    -   `/hbnb_filters`: display a HTML page like `6-index.html`, which was done during the project [0x01. AirBnB clone - Web static](https://intranet.alxswe.com/rltoken/EG-iGbr_iPTlHrQQSNho1g "0x01. AirBnB clone - Web static")
        -   Copy files `3-footer.css`, `3-header.css`, `4-common.css` and `6-filters.css` from `web_static/styles/` to the folder `web_flask/static/styles`
        -   Copy files `icon.png` and `logo.png` from `web_static/images/` to the folder `web_flask/static/images`
        -   Update `.popover` class in `6-filters.css` to allow scrolling in the popover and a max height of 300 pixels.
        -   Use `6-index.html` content as source code for the template `10-hbnb_filters.html`:
            -   Replace the content of the `H4` tag under each filter title (`H3` States and `H3` Amenities) by `&nbsp;`
        -   `State`, `City` and `Amenity` objects must be loaded from `DBStorage` and **sorted by name** (A->Z)
-   You must use the option `strict_slashes=False` in your route definition
-   Import this [10-dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql "10-dump") to have some data

**IMPORTANT**

-   Make sure you have a running and valid `setup_mysql_dev.sql` in your `AirBnB_clone_v2` repository ([Task](https://intranet.alxswe.com/rltoken/v5CSUMU7FY9wj_cnBY7P1A "Task"))
-   Make sure all tables are created when you run `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`

```
guillaume@ubuntu:~/AirBnB_v2$ curl -o 10-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 10-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.10-hbnb_filters
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In the browser:

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/4f993ec8ca2a2f639a80887667106ac63a0a3701.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240516T092812Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=881c83f8b9b8bb44a4ed499797d6108b8a44ff3672aeb1ad6cf463dc683acab3) ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/1549b553d726cc37f64440be910cb6b858aa32ae.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240516T092812Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=46d8128dd22c51b8028c90285248312044ac7935b596efe62e8b6cdd627f3982) ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/94b3a416ba1551c59701eb6672ac0a36fbebba14.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240516T092812Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=58d74f016f5f21a89c06f8dc397b37279603b281994fda1f3a1cf0b2d2b2507b) ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/1e559707dd34a37564dc10e54b707815a516d363.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240516T092812Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f4d59538f8990d688a8ee712aa3c3607437cc15ae5148476a793d3573548ed00)

**Repo:**

-   GitHub repository: `AirBnB_clone_v2`
-   File: `web_flask/10-hbnb_filters.py, web_flask/templates/10-hbnb_filters.html, web_flask/static/`

