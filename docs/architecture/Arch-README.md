
# General Architecture Discussions 

* Overall Architecture, distributed ephemeral connections 
* Data generation, propagation, and archival 
* Controls 
* Logic, AI, & Decision making 

This document is meant to be a concrete guide to implementation, standards, and educational reuse. The sections are break out details about the main component itemes with a master reference at the bottom annotated with key URLs or refernce materials useful to understanding or implementing the overall or specific areas. 

## Overall Architecture, distributed ephemeral connections
The overall architecture is guided by the CSI-Clue challange, this section may become a bit recursive, in that some elements of the design will find their origin here and others genisis are from the CSI-Clue documents (somewhat of chicken & egg paradigm.) The objective of this section is capture and extend both the strategy and tactics of the system architecture. The attempt is to create a common platform approach for future iterations. 

The system is built upon a component based approach.  Using a communication layer like Bluetooth, each component will have the ability to communicate with the other. 

## Data generation, propagation, and archival
Data can be generated from a variety of sources (aka: sensors), a brief list is below: 

* Visual Light Cameras
* Infra-red IR cameras (LIDR) or  FIR
* Sonar imagery 
* Chemical Sensors: pH (acid aklalinity), dissolved O2, Ammonia, N, K, P, Clorides, Redox, etc... 
* Physical Sensors: Temperature, Flow, Turbity, Conductivity, Magnetic fields, etc
* 

All the data is spatial and time based. This poses some challenges. 
Here's a good discussion at:  http://www.opengeospatial.org/standards/sensorthings


### Questions about Sensor/Source Data: 

What to do with RAW data? 
	How much to keep? 
	What to cache? 
	What / how / when to summarize or condense (average etc)? 
	Propagation, truncation, cleanup? 
How to format data? 
How to classify the data? 
How / when / what to apply ontology to the data? 
What base format to utilize (NVP, XML, JSON, some open KML style standards)?

##  Controls

## Logic, AI, & Decision making 

## Reference: 

* http://www.opengeospatial.org/docs/is
* http://www.academia.edu/21704898/Adjusting_the_Frequency_of_Automated_Phosphorus_Measurements_to_Environmental_Conditions
* 


## Un-structured notes from Emails & convos, that have not been digested into the table of contents: 

That's this site here for the (NCWQR): 

Tributary Data Download

Tributary Data Download
Tributary Loading Program Funding Financial support for the Tributary Loading Program has come from many sources...


Ok, that's formatted into a massive Excel data files thingy. 

The variables they are measuring are for rivers, creeks, streams, and tributaries are: 

1	Flow	(cfs)
2	SS	(mg/l)
3	TP	(mg/l)
4	SRP	(mg/l)
5	NO23	(mg/l)
6	TKN	(mg/l)
7	Chloride	(mg/l)
8	Sulfate	(mg/l)
9	Silica	(mg/l)
10	Conductivity	(μmho)
11	Future	N/A

 ss= suspended solids (turbidity)  or Suspended Sediment (SS)
 TP= Total Phosphorous 
 SRP = plant available phosphorus (soluble reactive phosphorus, SRP

 Conductivity as umho is that mirco-ohms. 

Ahh, good paper here on the references for the data topography (and specific in-depth discussion of P) 

http://www.academia.edu/21704898/Adjusting_the_Frequency_of_Automated_Phosphorus_Measurements_to_Environmental_Conditions

This paper lead me to a dozen other papers, of which the quickest and most beneficial is the: 

http://www.opengeospatial.org/standards/sensorthings

See the list of OGC Standards one of them is the KML that Google uses in Google maps. 

