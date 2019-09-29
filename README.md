# RPi API

An API for your Raspberry Pi.

## About

RpiAPI is a lightweight [WSGI](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface) [API](https://en.wikipedia.org/wiki/Application_programming_interface) built on top of the [RPi GPIO](https://pypi.org/project/RPi.GPIO/) library. It provides endpoints so you can interact with your Raspberry PI over the internet. With an API you can design your very own apps without having to worrying too much about the backend.

## Endpoints

### rpiapi/ - [GET]

The root end point of the API will return a dictionary with the values for the GPIO.RPI_INFO, GPIO.VERSION and MODE ( GPIO.setmode() ). By Default the RPiAPI is set as [BOARD](https://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering).

### rpiapi/activate/{pin_number} - [GET]  

The activate endpoint will output a - HIGH | 1 | True - value on the pin.

### rpiapi/deactivate/{pin_number} - [GET]  

The deactivate endpoint will output a - LOW | 0 | False - value on the pin.

### rpiapi/read/{pin_number}/{up|down} - [GET]  

The read enpoint will set the pin as an INPUT and read the value of the pin. You can specify **up** or **down** after the pin.

Giving a button as example: if you want your button to read 0 when it's pressed, you should pass an **up** argument to the endpoint, so it will sustaing the pin as 1 until it's pressed.

Read more about it [here](https://raspberrypi.stackexchange.com/questions/14680/raspberry-pi-gpio-input-pins-give-random-values).

### rpiapi/mode/{pin_number} - [GET]  

The read endpoint will return the current mode of the pin. The values might be:
GPIO.IN,  
GPIO.OUT,  
GPIO.SPI,  
GPIO.I2C,  
GPIO.HARD_PWM,  
GPIO.SERIAL,  
GPIO.UNKNOWN  

### toggle/{pin_number} - [GET]  

The toggle endpoint will toggle the pin. If it's active it will deactivate it. If it's deactive it will activate it. (if it's 0 it becomes 1, if it's 1 it becomes 0).


