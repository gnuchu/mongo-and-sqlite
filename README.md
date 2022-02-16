# Requirements

### Homebrew

If its not already installed follw the instructions at:

> https://brew.sh/

### MongoDB

> brew tap mongodb/brew
>
> brew install mongodb/brew/mongodb-community mongodb/brew/mongodb-community-shellbrew install
>
> brew services start mongodb/brew/mongodb-community
>
> brew install robo-3t (optional - install neat front end for mongo that makes viewing data easier)

### Python packages

(Assuming you have a working python install)

> pip install -r requirements.txt

### Process

* Run seed_mongo_db.py
  * This should give you records in your MongDB
    * ![1645045751386.png](image/README/1645045751386.png)
* Run read_and_convert.py
  * This should give you records in your sql DB (test.db)

    ![1645045832725.png](image/README/1645045832725.png)
