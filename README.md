# The Cool Beans @ Make OHI/O 2023

At Make OHI/O 2023, our project is a demonstration of our goal to bring more energy and cost effective heating and cooling to homes. We built a mock house that contains two separate rooms (however these rooms are identical) with features to maximize our goal. It contains (per room):

*   Two heating pads at the bottom of each room, simulating radiant floor heating.
*   A tubing system with fans and ice water (to simulate chilled water air conditioning)
*   An automated window system
*   A through-wall ventilation fan
*   A rotatory sensor to identify the wind direction

All these features allow complete control of the temperature of the environment in the best way possible.

*   Want to cool down one room?
    - The system will choose the best way to do it as cheap and efficient as possible. For example, if outside is colder and the other room is hotter it will open the       window and shut the fan.
*   Want to heat up one room?
    - The system will choose the best way to do it. For example, if the other room is hotter, transfer the air over.
*   Want to cool both rooms and it's hotter outside? 
    - The system will use the air conditioning to adjust both rooms to the same temperature.
*   Want to balance the temperatures between the rooms? 
    - The system will turn on the fan to allow air flow inbetween.
*   Want to warm up only one room? 
    - Then the system will turn on the heat in the desired room only if the other room is colder.
*   If a room needs to be coooled, and the outside temperature is cold with a cross breeze.
    - Then the system will open the window to create an effective draft.

Instead of making each of these decisions ourselves, our goal is to have the program decide to do the best possible solution based on the desired temperature requested by the client. However, in just 24 hours this is a little ambitious so we have created the functionality of each aspect but it still requires manual input. The temperature display is shown using a simple python GUI with each situation to showcase the functionalities and how they work. Looking at existing smart AC systems, they estimate saving users between 10% - 25% on costs. With our hyper-efficient project using AC and heating as minimally as possible, we're estimating saving our users 20% - 30%. 

How does it work?

All the sensors used (temperature, photoresistors, and a rotatory encoder) are read through the Arduino using its analog inputs. Once read, we send the information over to the Raspberry Pi using a serial connection. Based on the given information and picked scenario, we control the fans, servos, and heating pads that are all operated using the Pi. The main program allows customized use of our programmed scenarios with the hardware to simulate our project inside the mock house.

NEXT STEPS:

*   Develop an interface for the program for easy use
*   Integrate with Home Assistant (open source home automation program)
*   Saving presets (possibly with facial recognition)
