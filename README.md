# The Cool Beans @ Make OHI/O 2023

At Make OHI/O 2023, our project is a demonstration about our goal to bring more energy and cost effective heating and cooling to homes. We built a mock house that contains two separate rooms (however these rooms are identical) with features to maximize our goal. It contains (per room):

*   Two heating pads at the bottom
*   A tubing system with fans and ice water (to simulate air conditioning)
*   An openable and closable window system
*   A fan inbetween the rooms to move air between them
*   A rotatory sensor to identify the wind direction

All these features allow complete control of the temperature of the environment in the best way possible.

*   Want to cool both rooms and it's hotter outside? Use the air conditioning
*   Want to balance the temperatures between the rooms? Turn on the fan to allow air flow between the rooms
*   Want to warm up only one room? Turn on the heat in that desired room only
*   Want to cool a room and it's cooler outside and wind is blowing in it's direction? Open the window to create drafts

Instead of making each of these decisions ourselves, our goal is to have the program decide to do the best possible solution based on the desired temperature requested by the client. However, in just 24 hours this is a little ambitious so we have created the functionality of each aspect but it still requires manual input. The temperature display is shown using an LCD with each situation to showcase each functionality and how it works.

How does it work?

All the sensors used (temperature, photoresistors, and a rotatory encoder) are read through the Arduino utilizing the Arduino over the Raspberry Pi for analog input. Once read, we send the information over to the Raspberry Pi from the Arduino. Based on the given information and picked scenario, we control the fans, servos, heating pads, and LCD are all operated using the Pi. TALK ABOUT MAIN PROGRAM ONCE CREATED

NEXT STEPS:

*   Develop an interface for the program for easy use
*   Integrate with Home Assistant (open source home automation program)
*   Saving presets (possibly with facial recognition)
