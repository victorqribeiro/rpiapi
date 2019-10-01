# RPi API

An API for your Raspberry Pi.

[![RPiAPI](http://img.youtube.com/vi/5tc6QrXklQ0/0.jpg)](http://www.youtube.com/watch?v=5tc6QrXklQ0)

## About

RPiAPI is a lightweight [WSGI](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface) [API](https://en.wikipedia.org/wiki/Application_programming_interface) built on top of the [RPi GPIO](https://pypi.org/project/RPi.GPIO/) library. It provides endpoints so you can interact with your Raspberry PI over the internet. With an API you can design your very own apps without having to worrying too much about the backend.

## Installing

To install the RPiAPI you will need to clone it from GitHub, move the **rpiapi** folder to a place where Apache can access, enable mod-wsgi, create a wsgi configuration file for the **RPiAPI**, add the *www-data* user to the *gpio* group (so the Apache can control the pins on the raspberry pi) and set up a password on the **rpiapi** folder so only authorized people could access it.

Or, you can just call
```bash
sudo ./installer.sh
```
and let the script do all that for you.

Note that I *ALWAYS* recommend reading the code of a script before running it as a root user.

## Endpoints

### [GET] - rpiapi/

The root end point of the API will return a dictionary with the values for the GPIO.RPI_INFO, GPIO.VERSION and MODE ( GPIO.setmode() ). By Default the RPiAPI is set as [BOARD](https://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering).

### [GET] - rpiapi/activate/{pin_number}

The activate endpoint will output a - HIGH | 1 | True - value on the pin and return a **1** if **ok** or a error message.

### [GET] - rpiapi/deactivate/{pin_number}

The deactivate endpoint will output a - LOW | 0 | False - value on the pin and return a **0** if **ok** or a error message.

### [GET] - rpiapi/mode/{pin_number}

The mode endpoint will return the current **mode** of the pin or an error message. The values might be:  
- `GPIO.IN`
- `GPIO.OUT`
- `GPIO.SPI`
- `GPIO.I2C`
- `GPIO.HARD_PWM`
- `GPIO.SERIAL`
- `GPIO.UNKNOWN`

### [GET] - rpiapi/read/{pin_number}/{up|down}

The read enpoint will set the pin as an INPUT and read the value of the pin. You can specify **up** or **down** after the pin.

Giving a button as example: if you want your button to read 0 when it's pressed, you should pass an **up** argument to the endpoint, so it will sustaing the pin as 1 until it's pressed.

Read more about it [here](https://raspberrypi.stackexchange.com/questions/14680/raspberry-pi-gpio-input-pins-give-random-values).

### [GET] - rpiapi/serial/{port_number}

The serial endpoint opens a serial connection the the port especified on the *ports* variable on *views/serial_view.py* file. 

*I created this endpoint with the Arduino on mind, but it should work with other devices.*

By default you have:

```python
ports = [
	('/dev/ttyUSB0', 9600)
]
```

So the port your pass on the path will be index of the ports variable.  
**rpiapi/serial/0** will try to open a communication to the serial deviced connected to the USB0 with the baud rate of 9600. Feel free to change this configurations.

### [GET] - toggle/{pin_number}  

The toggle endpoint will toggle the pin. If it's active it will deactivate it. If it's deactive it will activate it. (if it's 0 it becomes 1, if it's 1 it becomes 0) and return the **current value** of the pin if ok or a error message.

## Making requests to the RPiAPI

Just navigate to http://your_raspberrypi_ip/rpiapi/ or with curl:
```
curl -u username:password http://your_raspberrypi_ip/rpiapi/
```

## Change the password of the RPiAPI

The RPiAPI uses basic HTTP authorization setted with a .htaccess and a .htpasswd so in order to create an user or change a password you'll need the htpasswd command.

### Create an user
```
htpasswd -c /var/www/rpiapi/.htpasswd username
```

### Change the password of an existing user
```
htpasswd /var/www/rpiapi/.htpasswd admin
```
