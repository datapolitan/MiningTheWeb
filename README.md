#XSAVI 750<a id='top'></a> – Mining the Web: How to Scrape, Analyze & Map Open Data

###Pratt Institute, Center for Continuing and Professional Studies Spatial Analysis and Visualization Initiative (SAVI)

Instructor: [Richard Dunks](http://www.datapolitan.com)

Location: [ISC Building, Lower Level, Room 003](https://www.dropbox.com/s/ilkyk0f7ojfbvcz/FindPratt_090915.jpg?dl=0)

Continuing Education Units (C.E.U.s): 3.0

[Click for more information and to register](bit.ly/1rksh3S)

----
###Navigation
+ [Course Overview](#course-overview)
+ [Learning Objectives](#learning-objectives)
+ [Course Requirements](#course-requirements)
+ [Course Readings](#course-readings)
+ [Class Format](#class-format)
+ [Submitting Assignments](#submitting-assignments)
+ [Class Policies](#class-policies)
	+ [Attendance and Tardiness](#attendance)
	+ [Participation](#participation)
	+ [Late Assignments](#late-assignments)
	+ [Office Hours](#office-hours)
+ [Resources](#resources)
+ [Course Outline](#course-outline)
	+ [Class 1](#class1)
		+ [Topics](#c1-topics)
		+ [Readings](#c1-readings)
		+ [Assignments](#c1-assignments)
		+ [Resources](#c1-resources)
	+ [Class 2](#class2)
		+ [Topics](#c2-topics)
		+ [Readings](#c2-readings)
		+ [Assignments](#c2-assignments)
		+ [Resources](#c2-resources)
	+ [Class 3](#class3)
		+ [Topics](#c3-topics)
		+ [Readings](#c3-readings)
		+ [Assignments](#c3-assignments)
		+ [Resources](#c3-resources)
	+ [Class 4](#class4)
		+ [Topics](#c4-topics)
		+ [Readings](#c4-readings)
		+ [Assignments](#c4-assignments)
		+ [Resources](#c4-resources)
	+ [Class 5](#class5)
		+ [Topics](#c5-topics)
		+ [Readings](#c5-readings)
		+ [Assignments](#c5-assignments)
		+ [Resources](#c5-resources)
	+ [Class 6](#class6)
		+ [Topics](#c6-topics)
		+ [Readings](#c6-readings)
		+ [Assignments](#c6-assignments)
		+ [Resources](#c6-resources)
	+ [Class 7](#class7)
		+ [Topics](#c7-topics)
		+ [Readings](#c7-readings)
		+ [Assignments](#c7-assignments)
		+ [Resources](#c7-resources)
	+ [Class 8](#class8)
		+ [Topics](#c8-topics)
		+ [Readings](#c8-readings)
		+ [Assignments](#c8-assignments)
		+ [Resources](#c8-resources)
	+ [Class 9](#class9)
		+ [Topics](#c9-topics)
		+ [Readings](#c9-readings)
		+ [Assignments](#c9-assignments)
		+ [Resources](#c9-resources)
	+ [Class 10](#class10)
		+ [Topics](#c10-topics)
		+ [Readings](#c10-readings)
		+ [Resources](#c10-resources)
+ [Suggested Reading](#suggested-reading)

----
##Administrivia

<a id='course-overview'></a>
###Course Overview
This course introduces the tools, techniques, and general approaches used to acquire, clean, analyze, and visualize open data, with particular emphasis on using web-based technologies and open-source tools at each step of the process.

######[back to top](#top)

<!--
This repository is a resource for code samples and other resources throughout the class.
-->
<a id='learning-objectives'></a>
###Learning Objectives
+ You will learn to formulate and articulate a meaningful research question with public open data, as well as meaningfully critique the work of others
+ You will learn how to acquire data through open data portals, application programmer interfaces (APIs), and scraping data from web sites
+ You will learn how to clean data using open source tools in preparation for analysis and visualization
+ You will learn how to conduct exploratory data analysis using descriptive statistics
+ You will learn to visualize your analytical findings in meaningful and visually-engaging graphics, as well as meaningfully critique the work of others
+ You will learn the basics of cartographic design as it relates to visualizing open data

######[back to top](#top)

<a id='course-requirements'></a>
###Course Requirements 
All students will need to bring their own laptop for exercises during class. Time will be set aside to help install, configure, and run the programs necessary for all assignments, projects, and exercises. Where possible, all programs will be free and open-source. All assigned work using services hosted online can be run using free accounts.

You will be required to have free accounts with the following services:

+ [Github](https://github.com/)
+ [CartoDB](http://cartodb.com/)
+ [Google](https://accounts.google.com/signup?service=mail)
<!--+ [Twitter](https://twitter.com/signup)-->


<!--
+ [Slack](
Tumblr - https://www.tumblr.com/register
-->

Time will be set aside to help you register and setup these accounts, but please try to come to the first session having already registered for these servies.

######[back to top](#top)

<a id='course-readings'></a>
###Course Readings 
The required readings for this course consist of book chapters, newspaper articles, and short blog posts. The intention is to help give you a foundation in the critical skills ahead of class lectures. All required readings are available online or will be made available through the class portal. Recommended readings are suggestions if you wish to study further the topics covered in class. The books listed in the Suggested Readings section below offer even more depth and an extended discussion of the material we cover in class.

######[back to top](#top)

<a id='class-format'></a>
###Class Format 
Class runs from 6pm to 9pm, with the class time broken up into two 85-minute blocks with a single 10-minute break around the half-way point of the class. Class will be a mix of lecture and practical exercise work, emphasizing the application of skills covered in the lecture portion of the class. 

I will also be available for questions or further assistance before and after class. You will have ample time in class to work on practical exercises based on the information presented in lectures. When possible, the final half hour of class will be set aside for any additional questions or additional tutorials in tools, skills, or techniques. Please plan on attending the full class time.

######[back to top](#top)

<a id='submitting-assignments'></a>
###Submitting Assignments
All assignments will be submitted by adding your content to the [class page](https://github.com/datapolitan/MiningTheWeb) and issuing a "[pull request](https://help.github.com/articles/using-pull-requests/)" in the [class repository](https://github.com/datapolitan/MiningTheWeb). All of this will be explained, setup, and otherwise clarified on the first day of class. **Assignments aren't considered submitted until the pull request has been issued.** We will have ample time in class to address any technical issues and a reference guide for the process.

######[back to top](#top)

###Assessment
Area | Percentage
--- | ---
Attendance | 20%
Class Participation | 20%
Visualization Critiques | 20%
Project Presentations & Visualization | 40%

######[back to top](#top)

<a id='class-policies'></a>
###Class Policies 
<a id='attendance'></a>
####Attendance and Tardiness  
I expect you to attend every class, arriving on time and staying for the entire duration of class. Absences will only be excused for extreme circumstances coordinated in advance and you are responsible for making up any missed work.
<a id='participation'></a>
####Participation 
I expect you to be fully engaged while you’re in class. This means asking questions when necessary, engaging in class discussions, participating in class exercises, and completing all assigned work. Learning will occur in this class only when you actively use the tools, techniques, and skills described in the lectures. I will provide you ample time and resources to accomplish the goals of this course and expect you to take full advantage of what’s offered.
<a id='late-assignments'></a>
####Late Assignments
All assignments are to be due before the start of class. Assignments submitted after class will be marked down 10% and assignments posted at the end of the next will be marked down 20%. No assignments will be accepted for a grade more than one day late.
<a id='office-hours'></a>
####Office hours
I won’t be holding regular office hours, but I’m happy to set up a time to meet in person, over the phone, or via Skype/Google Hangout if you have any problems. Please use [Slack](http://datapolitan.slack.com) to reach out to me. I will also be available before or after class to provide any assistance you may need.

######[back to top](#top)

<a id='resources'></a>
###Resources 
+ Technical
	+ [Stack Overflow](http://stackoverflow.com/) Q&A community of technology pros
	+ [GIS Stack Exchange](http://gis.stackexchange.com/) (same as above but just for mapping)
+ (Some) Open Data Sources
	+ [New York City Open Data Portal](https://nycopendata.socrata.com/)
	+ [New York State Open Data Portal](https://data.ny.gov/)
	+ [Hilary Mason’s Research Quality Data Sets](https://bitly.com/bundles/hmason/1)
	+ [Kirk Bourne's list of open data sources](http://www.datasciencecentral.com/profiles/blogs/a-plethora-of-open-data-repositories-i-e-thousands)
+ Visualizations
	+ [Flowing Data](http://flowingdata.com/)
	+ [Tableau Visualization Gallery](http://www.tableausoftware.com/public/gallery)
	+ [Visualizing.org](http://www.visualizing.org/)
	+ [IQuantNY](http://iquantny.tumblr.com/)
	+ [Data is Beautiful](http://www.reddit.com/r/dataisbeautiful/)
+ Reference
	+ [Get LatLon](http://teczno.com/squares/)

######[back to top](#top)

----
<a id='course-outline'></a>
##Course Outline
####Topics will be covered that day in class. Reading Assignments are to be read before class in preparation of the lecture and exercises. Assignments are due before the start of the next class and build on the information presented in class.

######[back to top](#top)
<a id='class1'></a>
####[Class 1 - January 25, 2016](http://www.datapolitan.com/MiningTheWeb/class1/)
<a id='c1-topics'></a>
####Topics 
+ What is open data?
+ Data on the web
+ Introduction to mapping
+ Introduction to open source tools and services for mapping and visualization

<a id='c1-assignments'></a>
####Assignments

<a id='c1-resources'></a> 
####Resources 
+ [A tutorial for getting started with Git and Github](http://bit.ly/1zlMfhK)
+ [CartoDB “Online Mapping for Beginners”](http://bit.ly/1CyXW7p)

----
<a id="suggested-reading"></a>
###Suggested Reading
+ Fry, Ben. *Visualizing Data: Exploring and Explaining Data with the Processing Environment*. O'Reilly Media, Inc., 2007.
+ Garrad, Chris. *Geoprocessing with Python*. Manning Publications Co., forthcoming. Janert, Philipp K. Data analysis with open source tools. O'Reilly Media, Inc., 2010.
+ McCallum, Q. Ethan. *Bad Data Handbook: Cleaning Up The Data So You Can Get Back To Work*. O'Reilly Media, Inc., 2012.
+ McKinney, Wes. *Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython*. O'Reilly Media, Inc., 2012.
+ Munzner, Tamara. *Visualization Analysis and Design*. AK Peters, 2014.
+ Murray, Scott. *Interactive data visualization for the Web*. O'Reilly Media, Inc., 2013.
+ Tufte, Edward R., and P. R. Graves-Morris. *The visual display of quantitative information*. Vol. 2. Cheshire, CT: Graphics press, 1983.

######[back to top](#top)