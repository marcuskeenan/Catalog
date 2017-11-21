<p align="center">
  <h1>A basic catalog app built with Python and Flask</h1>
  <img src="static/CatalogDemo.gif" width="460"/>
</p>


## Description
This project was created as part of my coursework for the Udacity [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004). The project is a basic catalog application that provides a list of items within a variety of categories as well as a user registration and authentication system. Registered users have the ability to post, edit and delete their own items.

## Features
1. CRUD functionality using a Flask webserver and sqlite database
2. RESTful JSON endpoints
3. Third-party OAuth authentication with google

## Prerequisites
1. [Python](https://www.python.org/downloads/) installed
2. VirtualBox
3. Vagrant
4. Git


# Getting Started

2. Clone the [fullstack-nanodegree-vm repository](https://www.google.com/url?q=http://github.com/udacity/fullstack-nanodegree-vm&sa=D&ust=1511258266705000&usg=AFQjCNEC2oPNAVAmHxADfWPmbm_5QrD5XQ). There is a catalog folder provided for you, but no files have been included. If a catalog folder does not exist, simply create your own inside of the vagrant folder.
Launch the Vagrant VM (by typing vagrant up in the directory fullstack/vagrant from the terminal). You can find further instructions on how to do so here.

## Install VirtualBox

VirtualBox is the software that actually runs the VM. [You can download it from virtualbox.org, here.](https://www.virtualbox.org/wiki/Downloads)  Install the *platform package* for your operating system.  You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it.

**Ubuntu 14.04 Note:** If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center, not the virtualbox.org web site. Due to a [reported bug](http://ubuntuforums.org/showthread.php?t=2227131), installing VirtualBox from the site may uninstall other software you need.

## Install Vagrant

Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem.  [You can download it from vagrantup.com.](https://www.vagrantup.com/downloads) Install the version for your operating system.

**Windows Note:** The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

# Get the VM Configuration

**Windows:** Use the Git Bash program (installed with Git) to get a Unix-style terminal.  
**Other systems:** Use your favorite terminal program.

From the terminal, run:

    git clone https://github.com/udacity/fullstack-nanodegree-vm.git

This will give you a directory named **catalog** complete with the source code for the flask application, a vagrantfile, and a bootstrap.sh file for installing all of the necessary tools. 

# Run the virtual machine!

Using the terminal, change directory to Catalog (**cd Catalog**), then type **vagrant up** to launch your virtual machine.


# Running the Catalog App
Once it is up and running, type **vagrant ssh**. This will log your terminal into the virtual machine, and you'll get a Linux shell prompt. When you want to log out, type **exit** at the shell prompt.  To turn the virtual machine off (without deleting anything), type **vagrant halt**. If you do this, you'll need to run **vagrant up** again before you can log into it.


Now that you have Vagrant up and running type **vagrant ssh** to log into your VM.  change to the /vagrant directory by typing **cd /vagrant**. This will take you to the shared folder between your virtual machine and host machine.

Type **ls** to ensure that you are inside the directory that contains application.py, database_setup.py, and two directories named 'templates' and 'static'

Now type **python database_setup.py** to initialize the database.

Type **python seeddatabase.py** to populate the database with categories and items. (Optional)

Type **python application.py** to run the Flask web server. In your browser visit **http://localhost:8000** to view the catalog app.  You should be able to view, add, edit, and delete catalog items and categories.
