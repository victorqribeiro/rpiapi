#!/bin/bash

[[ $(id -u) = "0" ]] || { echo "Please run the script as root user. sudo $0"; exit; }

# Install wsgi module for Python 3 (since Python 2 will be deprecated soon)
apt-get -y install apache2 libapache2-mod-wsgi-py3

# Enable module wsgi
a2enmod wsgi

# Copy api folder to /var/www/ (don't put it under html folder, or the source code might be exposed)
cp rpiapi/ /var/www/

# Copy configuration file to apache2 directory conf-enabled
cp mod-wsgi.conf /etc/apache2/conf-enabled/

# Add user www-data to the gpio group (So that the API can access the GPIO pins)
adduser www-data gpio

# Restart apache2 ir order to reload configurations
systemctl restart apache2

# Change the password for the admin user (default: admin)
htpasswd /var/www/rpiapi/.htpasswd admin
