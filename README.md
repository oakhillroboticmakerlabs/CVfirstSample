# CVfirstSample
CSI Clue Challenge 2015 initial notes, code, how-to, samples, tests, on Robotic Vision, Pattern and Image Recognition

Cool website Sample: http://oakhillroboticmakerlabs.github.io/CVfirstSample/
Click wiki above or submit an issue for a bug, question, or improvement. 

Description of the Oak Hill Robotics Makerspace 

The Oak Hill Robotics Makerspace provides a publicly accessible  robotics makerspace  for  Northeast Ohio that will encourage and support efforts to increase public awareness, understanding, and implications  of  new and upcoming trends and innovations in robotics-based technologies that have the potential to impact the daily lives of all citizens. ORM will provide a public space where individuals  can come  together to learn how to build, program, and  collaborate on low-cost, open-source robots and robotics-based projects that will benefit the community.  The ORM will also serve as an external space and resource for robotics education programs and projects at state universities, and technical schools and groups in Northeast Ohio.


The  ORM will achieve its vision by fostering and supporting these three initial community-based robotics  projects:

1. Biennial  NEOACM  CSI-CLUE  Robotics Challenge
2. MCPLP (Mill Creek Park Lakes Project Robotics Video Survey)
3. Critical M.A.S.S.  Robot simulation  Video Game

## NEOACM CSI-CLUE  Robotics Challenge

The NEOACM (Northeast Ohio Association for Computing Machinery)  CSI-CLUE Robotics Challenge is a biennial event designed to identify practical, safe, open-source, low-cost approaches to programming autonomous  robots. The challenge pits new trends in bio-inspired artificial intelligence against classical approaches in artificial intelligence to build robot controllers.  The challenge will also serve to showcase  the innovative engineering ability that is untapped in Northeast Ohio. ORM will be used as an outlet for this Challenge in collaboration with NEOACM. ORM will be used as a site to design, assemble, and test robots that will be in the Challenge. ORM will be utilized as the "community outreach" for the Challenge.

## MCPLP (Mill Creek Park Lakes Project  Robotics  Video  Survey)

MCPLP will endeavor to  build and  deploy low-cost, open-source  underwater robots to perform a video survey of the bottom of Lakes Glacier, Cohasset, and Newport.  These convenient natural resources offer an excellent opportunity to explore and possibly innovate underwater robotic applications. We believe that a total underwater video survey (using robots) of the bottom of our precious lakes has never been done before and will serve as a interesting and fun project for robot enthusiasts, students, and researchers in the area. The artifacts of this project will be accessible to the Northeast Ohio Community. 

## Critical MA.S.S.  Project

The Critical MA.S.S.  Project  is an open-source robot simulation game that will support the CSI/CLUE robotics challenge.  The project will bring together members of the community that are interested in video game development,  and will teach and share skills involved video game programming and production with the goal of releasing an open-source robotics simulation game.

In addition to these projects the ORM will host presentations, talks, workshops, and a web site that will serve as resources to engage, educate and inform the public on trends, innovations, and implications of robotics-based technologies. To aid in accomplishing our mission, we have engaged Ctest Laboratories and NEOACM to help us direct and coordinate the ORM.

## Farm Bots 

Two projects one builds on the other complementary: 

#1> Animal feeder (fish, chickens, etc, not necessarily a robot, but all the working parts) 
#2> Weeder bot for blue berry field. 

There are simple time based feeders that are available, commercially very affordable from Walmart/Sporting goods stores. These have simple IC electric circuits, with programmable interface LED and buttons. Somewhat universal look similar to the link below.  These are effective at broadcast feeding, bulk amounts, fairly exact times.  Except many animals like to be feed in the mornings and/or evenings.  Which given the seasonal nature of the earth, changes all year long, further more, based on temperature, dissolved oxygen, and visual feedback, hand feeding provides a more exact portioning of feed. The objective of this project is to take multiple inputs, use a simple algorithm (either ML, MAUT, or simple limit controllers). Input variables could be a variety of items and the output would be a simple Solid State Relay (SSR) for on-off on a motor, as this simple design does.  These controller are very lower power and can run off a simple 6V Lead acid rechargable battery for days, months, and by adding a simple solar panel unlimited. 

Digital Timer Controller for Deer, Fish & Hog Feeders
https://www.google.com/search?hl=en&tbm=isch&q=measuring+instrument&oq=&gs_l=#hl=en&tbm=isch&q=digital+feeder+timer&imgrc=zyjsYpQ2mQUveM%3A

### Building on lessons learned from #2 and the other ORM projects: 

Robot weeder would have a more specific function and higher degree of complexity.  Using Computer Vision, train the system using either HAAR cascades, LBP, or SVG-PCA for object detection. Whatever the programming mechanism on the CV side, this to eventually leads be a simple boolean decision, is the object in scope a weed or blue berry stem?  The project items required to complete this involve everything in the robot problem solving space, namely: maneuvering, maps, location, vision, control, command, and refueling. There are numerous problems to solve on this design, many of which are paralleled in the CSI Clue and the environmental bots. 

### Step 1: Read Soil Conditions
An iterative approach to this would be to use the CSI Clue and other teams bot solutions and grow off of these initiatives. The collaboration and lessons learned would be shared, if not just for chemical analysis, simple pH tests of blue berries would be a giant benefit to farmers. Knowing that the plant in row 3, positions 87-99 have a pH higher than +6, would allow a farmer to target their management practices.  Even for a small berry farmer like myself, with only 1,000 plants.  The largest farm in Ohio has over 80,000 plants. Having a self propelled crawler bot to indicate pH would be of value to numerous farmers who have plants in modified soil conditions. 

### Step 2: Weeder Bot
Add other sensors and scissor cutter.  The various ideas that have been brain stormed are scissor cut, whereby the weed is killed via a lever mechanical advantage, the bot position this cutting device so that it only damages to the weed stock and not the targeted plant. The organic community would love this, because it removes the need for chemicals (even organic approaches) or for the back breaking painful aspect of weeding.  Several universities and organizations have looked using traditional gas driven rototillers style approaches.  The concept is here an army of low costs, low power bots, bio-mimicking destructive animals feasting on plants, but in this case, the damage would be targeted to the local weeds. Not tied to the mechanical methods either. 

### Step 2: Fertilizer Bot
Targeted, precise, delivery of fertilizer or pesticides via the weeder bot would benefit the environment and man-kind.  The current main culprit for the dangerous algae blooms in the Great Lakes (Toledo) have been farm run-off.  NPK fertilizer where the P is Phosphorus and likely the main culprit in the blue-green or red algae blooms. From a farmers perspective, excess fertilizer lost to the external environment is a costly problem. Berry, fruit, vegetables farmers could benefit from a sensor based precision delivery of fertilizer, as would the rest of the ecology and ground run-off around them. 

# References Links

## General 

* http://www.trossenrobotics.com/
* https://services.google.com/fb/forms/brilloweaveinviteform/
* 

## How-Tos, tutorials, Instructables: 

* http://www.instructables.com/id/Raspberry-PI-L298N-Dual-H-Bridge-DC-Motor/
* http://www.instructables.com/id/Arduino-Aquaponics-EnvDAQ-Upgrade-with-pH-and-Diss/
* 



## Sensors 

* https://www.ysi.com/
* http://www.exowater.com/sensors
* 

# Computer Vision Samples: 

1. https://cloud.google.com/vision/pricing
2. https://www.microsoft.com/cognitive-services/en-us/computer-vision-api
3. https://www.tensorflow.org/versions/r0.10/get_started/index.html
4. http://deeplearning4j.org/compare-dl4j-torch7-pylearn.html#ml


## Sample Programs (snippets)

* Microsoft Oxford Computer Vision Sample CVfirstSample>C:\Python27\python.exe ImageTesting.py


## Python setup issues on windows elsewhere: 

Add the following modules into python: 

1. C:\Python27\Scripts>pip install numpy
2. C:\Python27\Scripts>easy_install.exe requests

