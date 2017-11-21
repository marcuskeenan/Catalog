<p align="center">
  <h1>A catalog app created with Python and Flask</h1>
  <img src="static/CatalogDemo.gif" width="460"/>
</p>


## Description
This project was created as part of my coursework for the Udacity [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004). The project is a basic catalog application that provides a list of items within a variety of categories as well as a user registration and authentication system. Registered users have the ability to post, edit and delete their own categories and items.

## Features
1. CRUD functionality using a Flask webserver and sqlite database with sqlalchemy
2. RESTful JSON endpoints
3. Third-party OAuth 2.0 authentication using google sign in

## Prerequisites
1. [Python](https://www.python.org/downloads/) installed
2. VirtualBox
3. Vagrant
4. Git


# Getting Started

## Install VirtualBox

VirtualBox is the software that actually runs the VM. [You can download it from virtualbox.org, here.](https://www.virtualbox.org/wiki/Downloads)  Install the *platform package* for your operating system.  You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it.

**Ubuntu 14.04 Note:** If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center, not the virtualbox.org web site. Due to a [reported bug](http://ubuntuforums.org/showthread.php?t=2227131), installing VirtualBox from the site may uninstall other software you need.

## Install Vagrant

Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem.  [You can download it from vagrantup.com.](https://www.vagrantup.com/downloads) Install the version for your operating system.

**Windows Note:** The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

## Get the Udacity fullstack-nanodegree-vm Configuration

**Windows:** Use the Git Bash program (installed with Git) to get a Unix-style terminal.  
**Other systems:** Use your favorite terminal program.



## Run the virtual machine!

Using the terminal, change directory to fullstack-nanodegree-vm/vagrant (**cd fullstack-nanodegree-vm/vagrant**), then type **vagrant up** to launch your virtual machine. (This could take a few minutes)

## SSH to the Vagrant VM
Once it is up and running, type **vagrant ssh**. This will log your terminal into the virtual machine, and you'll get a Linux shell prompt. When you want to log out, type **exit** at the shell prompt.  To turn the virtual machine off (without deleting anything), type **vagrant halt**. If you do this, you'll need to run **vagrant up** again before you can log into it.

Change to the Vagrant shared folder, type **cd /vagrant**.
Type **ls** to see the contents of the directory. **catalog forum  tournament  Vagrantfile**

Remove the existing **catalog** folder by typing: ("catalog" will be replaced by "Catalog" in the next step"
```
  rm -rf catalog
```
## Get the catalog app code
While in the **/vagrant** directory clone this repo.
```
  git clone https://github.com/marcuskeenan/Catalog.git
```
This will create a new folder inside the catalog directory called **Catalog**.

# Setup the application
Change to the Catalog directory **cd Catalog** and **ls** and **ls** to make sure the directory contains **application.py**, **database_setup.py**, and **seed_database.py**.

## Set up the database
Run:
```
  python database_setup.py to initialize the database.
```
This will create a sqlite database called catalog.db.

## Add fake data to the database
Run:(Optional)
```
python seedatabase.py
```
This will seed the database with some catalog categories and associated items.

## Run the application
Run:
```
python application.py
```
This will run the Flask web server. In your browser visit **http://localhost:5000** to view the catalog app. After loggin in, you should be able to view, add, edit, and delete catalog items and categories.
