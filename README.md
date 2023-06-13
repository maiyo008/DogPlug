# DogPlug
Documentation here

## How to run Flask web framework
```
DOGPLUG_MYSQL_USER=dogplug_dev DOGPLUG_MYSQL_PWD=dogplug_dev_pwd DOGPLUG_MYSQL_HOST=localhost DOGPLUG_MYSQL_DB=dogplug_dev_db DOGPLUG_TYPE_STORAGE=db python3 -m web_flask.index
```

Example here below;
```
vagrant@ubuntu-focal:~/DogPlug$ DOGPLUG_MYSQL_USER=dogplug_dev DOGPLUG_MYSQL_PWD=dogplug_dev_pwd DOGPLUG_MYSQL_HOST=localhost DOGPLUG_MYSQL_DB=dogplug_dev_db DOGPLUG_TYPE_STORAGE=db python3 -m web_flask.index
 * Serving Flask app 'index' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://10.0.2.15:5000
Press CTRL+C to quit
```
