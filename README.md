# Summary #

This is a simple project building off of Kevin Dryfuse's PySpark starter template [here](https://github.8451.com/k200745/pyspark-starter-template).
The purpose of it, is to have an easy way to clone the general structure of Kevin's project, while still being able to rename folders and 
insert author information, and any other information you want to specify at time of project creation. 

# Dependencies #
* python
* python-pip
* cookiecutter

# Installation #

Assuming you already have python and pip installed, run the following command to install the cookiecutter library:

```bash
pip install cookiecutter
```

# Description #

Cookiecutter is basically a piece of software that lets you use template variables that will be initialized at time of project 
creation based on defaults, or user specified input. These variable are easy to see. They all appear within double braces and have 
dot notation prepended with 'cookiecutter'. So, in this project you will see variables like `cookiecutter.project_name`, or `cookiecutter.first_name`.
These are template variables that initialize themselves based on what is set up in the `cookiecutter.json` file in the root of this project directory.
When you set up your project structure, anything you want to be fluid, just name it `{{cookiecutter.varibale_name}}`, and in `cookiecutter.json` file
make sure you set that variable's default value.

# Execution #

To copy this project structure to your local machine, naming it whatever you want and specifying the other information at creation time,
simple execute the following command:

```bash
cookiecutter <link-to-cookiecutter-project-in-github>
```

So, for this project, you would run the following specific command:

```bash
cookiecutter https://github.8451.com/comms-data/comms-pyspark-cookiecutter
```

When you run this in your terminal, it will display all defaults configured for the variables in the `cookiecutter.json` file one by one.
Something like:

```bash
project_name[comms-pyspark]:
```

If you just hit enter, it will use the default (in this case comms-pyspark). But, if you want to change that, type whatever name you want
to change it to next to the colon, then hit enter. So on, and so forth. 

# coockiecutter
