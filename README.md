# Cross-Safe-Road-Sensor-System

[README.docx](https://github.com/user-attachments/files/34110601/README.docx)

Cross Safe is a physical computing prototype designed to explore the relationship between coding and sensor technology. The project uses BBC micro v2, an ultrasonic sensor and LED warning lights to simulate a pedestrian crossing system. When a pedestrian is detected within a specified distance, the system activates a flashing red LED to represent a warning to approaching drivers.
This prototype was developed for 52685 Creative Coding at the University of Technology Sydney (UTS), Spring 2026.

Table of Contents
Project Aim
Technologies Used
Features
Screenshots
Setup
Usage
Project Status
Room for Improvement
Acknowledgements
Contact

Project Aim
The aim and purpose of Cross Safe is to demonstrate how physical computing, as simple as a BBC Micro:bit can receive information from a sensor and circuit, to solve real life problems involved with road safety. The project utilises an ultrasonic distance sensor for LED lights to respond when a pedestrian approaches the crossing. The reason for this is to warn cars of the pedestrian approaching to help reduce crossing accidents, and enhance the safety of pedestrians on roads.
Technologies Used
Programming and development tools:
MicroPython
BBC micro Python Editor
Microsoft MakeCode
Tinkercad Circuits
Hardware components:
X1 BBC micro:bit v2
X1 SparkFun micro breakout board
X1 HC-SR04 ultrasonic distance sensor
X1 Breadboard
X 1 red LED
X1 1 green LED
X2 330 Ω resistors
Multiple Jumper wires
X1 External 5V power supply for the ultrasonic distance sensor
X1 Battery pack for the micro:bit

Features
Some features of Cross Safe include: 
Pedestrian detection: An ultrasonic sensor measures the distance between the crossing and an approaching object.

Automatic warning system: A flashing red LED activates when an object is detected within 35 cm to warn cars to stop.

Clear crossing indicator: A steady green LED remains illuminated when no pedestrian is detected to notify cars to keep driving.

Conditional programming: MicroPython processes sensor readings to determine which LED should activate.

Continuous monitoring: The system repeatedly measures distance and updates its warning signals.

Detection buffer: A 40 cm clearance threshold helps prevent the warning lights from rapidly switching between states.

Screenshots
The below images demonstrate the final outcome of Cross Safe: 


<img width="322" height="397" alt="Screenshot 2026-10-29 at 10 13 19 pm" src="https://github.com/user-attachments/assets/f1beb20b-2e6a-4683-b35f-8fbf5f969904" />


Setup

Requirements

To recreate Cross Safe, the hardware components listed under Technologies Used are required. The project uses the BBC micro:bit v2 and MicroPython. No additional Python packages need to be installed.

Hardware Connections
Ultrasonic sensor TRIG: micro:bit P0
Ultrasonic sensor ECHO: micro:bit P1
Red LED: micro:bit P8 through a 330 Ω resistor
Green LED: micro:bit P13 through a 330 Ω resistor
Ultrasonic sensor VCC: External 5V power supply
Ultrasonic sensor GND: Ground
LED cathodes: Ground

Installation

Assemble the circuit using the hardware connections above.
Open the BBC micro:bit Python Editor.
Open the Cross Safe MicroPython code from this repository.
Copy the code into the Python Editor.
Connect the BBC micro v2 to your computer.
Transfer the code to the micro:bit.
Connect the micro:bit to its battery pack.
Press the switch on the external 5V power supply for the ultrasonic distance sensor to ensure the blue LED turns on.
Test the prototype by moving an object of decent width and length towards the sensor. The red LED should be flashing once you are within 35cm of the distance sensor.
If the above step is successful, you have completed the creation of Cross Safe!


Usage
Cross Safe operates automatically once the 5V power supply is turned on and the MicroPython program is running in the micro:bit.

Scenario 1: No pedestrian detected

When no object is detected within the activation range:

The green LED remains ON.

The red LED remains OFF.

The system continues monitoring the ultrasonic sensor.

Scenario 2: Pedestrian detected

When an object moves within 35 cm of the sensor:

The green LED switches OFF.

The red LED begins flashing.

The flashing light represents a warning to approaching drivers.

Scenario 3: Pedestrian moves away

When the object moves beyond 40 cm:

The red LED stops flashing.

The green LED switches ON.

The system returns to its normal monitoring state.




Code Example: 

The following MicroPython conditional statements determine the pedestrian detection state:

<img width="304" height="110" alt="Screenshot 2026-10-29 at 10 14 08 pm" src="https://github.com/user-attachments/assets/f836f1b3-e111-4870-adfd-d35e240dd56b" />



Project Status

Project status: Completed on 22nd of October 2026

The final Cross Safe prototype is successful in completing its goal of detecting objects using an ultrasonic distance sensor and automatically activates the appropriate LED warning signal.

Cross Safe is an educational prototype and has not been designed or tested for use on public roads.


Room for Improvement

Whilst the finished prototype did achieve its desired function, there is still some room for improvement:

Room for improvement:

Sensor accuracy: The ultrasonic distance sensor struggled to detect smaller objects, requiring cardboard to increase their reflective surface area.
Limited detection: The use of only one ultrasonic distance sensor limits the area that can be monitored.
Environmental reliability: The prototype has not been tested under different outdoor weather or lighting conditions.
To do:

Add another distance sensor to increase accuracy 
Test the prototype in different lighting, and environments to assess how successful it really is in detecting a pedestrian.
Work out how to get the sensor to accurately detect objects of all widths and heights (if possible).

Acknowledgements
This project was inspired by my own experience with dangerous pedestrian and development was assisted and guided by the following:

Berry, D. M. (2011). *The philosophy of software: Code and mediation in the digital age*. Palgrave Macmillan. https://doi.org/10.1057/9780230306479
Downey, A. B. (2015). *Think Python: How to think like a computer scientist* (2nd ed.). O'Reilly Media.
GeeksforGeeks. (n.d.). Boolean data type in Python. https://www.geeksforgeeks.org/python/boolean-data-type-in-python/
GeeksforGeeks. (n.d.-b). Loops in Python. https://www.geeksforgeeks.org/python/loops-in-python/
Halfacree, G. (2018). *The official BBC micro:bit user guide*. Wiley. https://doi.org/10.1002/9781119413752
Kolb, D. A. (1984). *Experiential learning: Experience as the source of learning and development*. Prentice-Hall.
Kuniavsky, M. (2008). User experience design for ubiquitous computing. *Interactions, 15*(6), 20–22. https://doi.org/10.1145/1409040.1409045
Madecraft. (2024). *Python for students* [Video course]. LinkedIn Learning. https://www.linkedin.com/learning/python-for-students-2023/creating-your-first-loop?u=2129308
Matthes, E. (2023). *Python crash course: A hands-on, project-based introduction to programming* (3rd ed.). No Starch Press.
Micro:bit Educational Foundation. (n.d.-a). *Features: Overview*. https://microbit.org/get-started/features/overview/
Micro:bit Educational Foundation. (n.d.-b). *Input/output pins*. BBC micro:bit MicroPython documentation. https://microbit-micropython.readthedocs.io/en/v2-docs/pin.html
Micro:bit Educational Foundation. (n.d.-c). *MicroPython*. BBC micro:bit MicroPython documentation. https://microbit-micropython.readthedocs.io/en/v2-docs/micropython.html
Micro:bit Educational Foundation. (n.d.-d). *Proximity beacon*. https://microbit.org/projects/make-it-code-it/proximity-beacon/
Micro:bit MicroPython. (n.d.-a). *Display*. BBC micro:bit MicroPython documentation. https://microbit-micropython.readthedocs.io/en/v2-docs/display.html
Micro:bit MicroPython. (n.d.-b). *Input/output pins*. BBC micro:bit MicroPython documentation. https://microbit-micropython.readthedocs.io/en/latest/pin.html
Pajankar, A., Saini, S., & Sharma, A. (2022). *BBC Micro:bit in practice: A hands-on guide to building creative real-life projects with MicroPython and the BBC Micro:bit*. Packt Publishing.
Pepperl+Fuchs. (n.d.). *Technology guide: Ultrasonic sensors*. https://files.pepperl-fuchs.com/webcat/navi/productInfo/doct/tdoct3557a_eng.pdf
Science Buddies. (n.d.). *How to use a micro:bit*. https://www.sciencebuddies.org/science-fair-projects/references/how-to-use-a-micro-bit
Tollervey, N. H. (2017). *Programming with MicroPython: Embedded programming with microcontrollers and Python*. O'Reilly Media.
University of Technology Sydney. (2026). Creative coding 03: Hardware [Lecture slides]. Canvas.


Contact
Created by @raneemhraichie-1 

Feel free to contact me for further guidance and questions :)
