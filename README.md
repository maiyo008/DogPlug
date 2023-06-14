# DogPlug
![Meme](https://imgur.com/CcJcdd9.png)
<br>

## Table of Contents
- [How to run Flask web framework](#how-to-run-flask-web-framework)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact Information](#contact-information)

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

## Installation
To install Dog Plug on your local development environment, follow these steps:

1. Clone the repository from GitHub:
```
git clone https://github.com/maiyo008/DogPlug.git
```
2. This project contains a console program that is used to interact with objects created. Before interacting with the objects, here is how to set up your environment:

   #### Packages used for the project
   ![flask](https://img.shields.io/badge/Flask-2.1.0-important)
   ![sqlalchemy](https://img.shields.io/badge/SQLAlchemy-2.0.6-important)
   #### Database used
   ![myssql](https://img.shields.io/badge/mysql-8.0.33-important)
   ![mysqlclient](https://img.shields.io/badge/mysqlclient-2.1.1-important)
   
   * Before runing the console program, setup mysql using [this](https://github.com/maiyo008/DogPlug/blob/main/setup_mysql_dev.sql)

## Usage
Some examples of how to use DogPlug:

1. **Create Profile:**
![Dog profile](https://i.imgur.com/ypogDTE.png)
   - Navigate to the DogPlug landing page and click on create dog profile.

2. **Search for a groomer near you:**
![Filter groomers](https://i.imgur.com/jbluje1.png)
   - After.

   **Run console**
   * To run the console:
```
vagrant@ubuntu-focal:~/DogPlug$ DOGPLUG_MYSQL_USER=dogplug_dev DOGPLUG_MYSQL_PWD=dogplug_dev_pwd DOGPLUG_MYSQL_HOST=localhost DOGPLUG_MYSQL_DB=dogplug_dev_db DOGPLUG_TYPE_STORAGE=db ./console.py
Welcome to DogPlug
(DogPlug)
```
   1. To create objects:
   `create <Class name> <param 1> <param 2> <param 3>...`
   <br>
   Example:
```
(DogPlug)create County name="Turkana"
2e62d7f6-9674-4dbf-b2c2-52972eeed016
(DogPlug)
```


## Contributing
![flask](https://img.shields.io/badge/WebFramework-Flask-green) 
![Languages](https://img.shields.io/badge/Languages-Python%2C%20HTML%26CSS%2C%20Javascript-orange)
![Libraries](https://img.shields.io/badge/Libraries-JQuery-blueviolet)
<br>
This project was developed using the following technologies:

- **HTML:** The standard markup language for creating the structure and content of web pages. [Learn more](https://developer.mozilla.org/en-US/docs/Web/HTML)

- **CSS:** A stylesheet language used for describing the presentation of a document written in HTML. [Learn more](https://developer.mozilla.org/en-US/docs/Web/CSS)

- **Bootstrap:** A popular CSS framework that provides pre-designed responsive components and styles to simplify web development. [Learn more](https://getbootstrap.com/)

- **Python:** A versatile and powerful programming language used for server-side development, data processing, and automation. [Learn more](https://www.python.org/)

- **JavaScript:** A programming language that enables dynamic and interactive behavior on web pages. [Learn more](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

- **jQuery:** A fast and concise JavaScript library that simplifies HTML document traversal, event handling, and animation. [Learn more](https://jquery.com/)

- **CSS Grid:** A powerful two-dimensional layout system in CSS that allows for the creation of complex grid-based layouts. [Learn more](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout)

- **Flask:** A python framework to create restful api's.
[Learn more](https://flask.palletsprojects.com/en/2.3.x/)

## License
DogPlug is currently not licensed.

## Contact Information
For any inquiries or feedback regarding DogPlug, you can reach out to Tony Maiyo or Purity Muthee using the following contact information:

GitHub: [puritymuthee-code](https://github.com/63brown/) 
GitHub: [tonymaiyo-code](https://github.com/maiyo008/)
LinkedIn: [Purity Muthee](https://www.linkedin.com/in//)
LinkedIn: [Tony Maiyo](https://www.linkedin.com/in//)