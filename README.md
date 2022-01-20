# Arduino based Real Time Air Pollution Monitoring IOT device

<h2 align="center"><a href="http://detect-air-quality.herokuapp.com/" target="_blank">Website</a></h2>

An air quality monitor is a device that measures the level of common air pollutants.
IOT Based Air Pollution Monitoring System monitors the Air Quality over a webserver using internet and will trigger a buzzeer when the air quality goes down beyond a certain level, means when there are amount of harmful gases present in the air like CO2. The system will show the air quality in PPM on the LCD and as well as on webpage so that it can be monitored very easily. Temperature and Humidity is detected and monitored in the system.

## 🎯 Purpose of the Project
Average person spends an estimated 90% of their time indoors so that poor indoor air quality poses a substantial risk to public health. Poor air quality may cause increased short-term health problems such as fatigue and nausea as well as chronic respiratory diseases, heart disease, and lung cancer.

In this project, we are going to present an indoor air quality monitoring system. Our system is connected to the Internet, and as a result, anyone can remotely visualize the air quality index fromm anywhere.

## - 🏃‍Working-principle and Implementaion:
The proposed Air Pollution Monitoring System is based on the block diagram as shown in Fig.1. The data of air is recognized by the MQ135 gas sensor. The MQ135 sensor can sense CO2. So it is dynamic gas sensored for our Air pollution Monitoring system. When it will be connected to Arduino then it will sense gases, and it will give the Pollution level in PPM (parts per million).

The sensor is giving us a value of 90 when there is no gas near it and the air quality safe level is 350 PPM and it should not exceed 1000 ppm. When it will exceed the limit of 1000 PPM, it will cause Headaches, sleepiness, and stagnant, stuffy air.

If it exceeds 2000PPM then it will cause increased heart rate and many different diseases. When the value will be less than1000 PPM, then the LCD and webpage will display **“Fresh Air”.** When the value will increase from 1000PPM, then the buzzer will start beeping and the LCD and webpage will display **“Poor Air, Open Windows”**. And when it will increase 2000, the buzzer will keep beeping and give an alert message on the smartphone through the website. 

The LCD and webpage will display **“Danger! Move to Fresh Air”.** LCD and Buzzer are the output devices. LCD shows the data of the gases in ppm (parts per million) and Buzzer is used when ppm crosses above a threshold limit.

As of now our project will show only the level of **carbon dioxide(CO2)**


### 👨🏻‍💻Software Required:

 This project is built and developed using [Ardunio](https://www.arduino.cc/en/software) and [Python Flask](https://www.python.org/). 


### 🥁 Implementaion Pic:

<p align="center">
<img height="400" width ="600" src = "https://raw.githubusercontent.com/MANOJ-015/Air-Quality-Monitoring/main/images/implemenation.jpeg"></img>
</p>
 

## 🏁 Technology Stack
<p align="center">
<img height="200" width ="200" src = "https://user-images.githubusercontent.com/56405152/125989051-99f28b39-b160-4d7b-ab7b-249479f94890.png"></img>
<img height="200" width ="300" src = "https://user-images.githubusercontent.com/56405152/125989130-6948a657-e059-49c4-85e3-4ec3f90f4deb.png"></img>
<img height="200" width ="200" src = "https://user-images.githubusercontent.com/56405152/125989579-a00eb116-84eb-4bb8-a5e5-5cccfc24de9c.png"></img>
<img height="200" width ="200" src = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/ISO_C%2B%2B_Logo.svg/180px-ISO_C%2B%2B_Logo.svg.png"></img>
</p>


* [Flask](https://github.com/pallets/flask)<br />
* [HTML](https://www.w3.org/TR/html52)<br />
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)<br />
* [Bootstrap](https://getbootstrap.com)<br />
* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
* [C++](https://www.cplusplus.com/)
