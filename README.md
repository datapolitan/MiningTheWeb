# XSAVI 750<a id='top'></a> – Mining the Web: How to Scrape, Analyze & Map Open Data

### Pratt Institute, Center for Continuing and Professional Studies Spatial Analysis and Visualization Initiative (SAVI)

Instructor: [Richard Dunks](http://www.datapolitan.com)

Location: [ISC Building, Lower Level, Room 003](https://www.dropbox.com/s/ilkyk0f7ojfbvcz/FindPratt_090915.jpg?dl=0)

Continuing Education Units (C.E.U.s): 3.0

[Click for more information and to register](http://bit.ly/1rksh3S)

----
### Navigation
+ [Course Overview](#course-overview)
+ [Learning Objectives](#learning-objectives)
+ [Course Requirements](#course-requirements)
+ [Course Readings](#course-readings)
+ [Class Format](#class-format)
+ [Submitting Assignments](#submitting-assignments)
+ [Assessment](#assessment)
+ [Class Policies](#class-policies)
	+ [Attendance and Tardiness](#attendance)
	+ [Participation](#participation)
	+ [Late Assignments](#late-assignments)
	+ [Office Hours](#office-hours)
+ [Resources](#resources)
+ [Course Outline](#course-outline)
	+ [Class 1 - April 11, 2016](#class1)
		+ [Topics](#c1-topics)
		+ [Assignment](#c1-assignments)
		+ [Resources](#c1-resources)
	+ [Class 2 - April 13, 2016](#class2)
		+ [Topics](#c2-topics)
		+ [Readings](#c2-readings)
		+ [Assignments](#c2-assignments)
		+ [Resources](#c2-resources)
	+ [Class 3 - April 18, 2016](#class3)
		+ [Topics](#c3-topics)
		+ [Readings](#c3-readings)
		+ [Assignments](#c3-assignments)
		+ [Resources](#c3-resources)
	+ [Class 4 - April 20, 2016](#class4)
		+ [Topics](#c4-topics)
		+ [Readings](#c4-readings)
		+ [Assignments](#c4-assignments)
		+ [Resources](#c4-resources)
	+ [Class 5 - April 25, 2016](#class5)
		+ [Topics](#c5-topics)
		+ [Readings](#c5-readings)
		+ [Assignments](#c5-assignments)
		+ [Resources](#c5-resources)
	+ [Class 6 - April 27, 2016](#class6)
		+ [Topics](#c6-topics)
		+ [Readings](#c6-readings)
		+ [Assignments](#c6-assignments)
		+ [Resources](#c6-resources)
	+ [Class 7 - May 2, 2016](#class7)
		+ [Topics](#c7-topics)
		+ [Readings](#c7-readings)
		+ [Assignments](#c7-assignments)
		+ [Resources](#c7-resources)
	+ [Class 8 - May 4, 2016](#class8)
		+ [Topics](#c8-topics)
		+ [Readings](#c8-readings)
		+ [Assignments](#c8-assignments)
		+ [Resources](#c8-resources)
	+ [Class 9 - May 9, 2016](#class9)
		+ [Topics](#c9-topics)
		+ [Readings](#c9-readings)
		+ [Assignments](#c9-assignments)
		+ [Resources](#c9-resources)
	+ [Class 10 - May 11, 2016](#class10)
		+ [Topics](#c10-topics)
		+ [Readings](#c10-readings)
		+ [Resources](#c10-resources)
+ [Suggested Reading](#suggested-reading)

----
## Administrivia

<a id='course-overview'></a>
### Course Overview
This course introduces the tools, techniques, and general approaches used to acquire, clean, analyze, and visualize open data, with particular emphasis on using web-based technologies and open-source tools at each step of the process.

We will be working with the community preservation group [Save Harlem Now!](http://www.saveharlemnow.org/) to help collect, organize, and visualize data related to historic preservation in Harlem. There is no requirement to participate in this project and each student is free to pursue their own projects in class. The work with Save Harlem Now! is an opportunity to work on a real-world problem related to the collection, analysis, and visualization of data.

###### [back to top](#top)

<!--
This repository is a resource for code samples and other resources throughout the class.
-->
<a id='learning-objectives'></a>
### Learning Objectives
+ You will learn to formulate and articulate a meaningful research question with public open data, as well as meaningfully critique the work of others
+ You will learn how to acquire data through open data portals, application programmer interfaces (APIs), and scraping data from web sites
+ You will learn how to clean data using open source tools in preparation for analysis and visualization
+ You will learn how to conduct exploratory data analysis using descriptive statistics
+ You will learn to visualize your analytical findings in meaningful and visually-engaging graphics, as well as meaningfully critique the work of others
+ You will learn the basics of cartographic design as it relates to visualizing open data

###### [back to top](#top)

<a id='course-requirements'></a>
### Course Requirements 
**All students will need to bring their own laptop for exercises during class.** Time will be set aside to help install, configure, and run the programs necessary for all assignments, projects, and exercises. Where possible, all programs will be free and open-source. All assigned work using services hosted online can be run using free accounts. **Please update your system to the latest version of your prefered operating system prior to the first day of class to ensure you're able to successfully install and use the tools in class.**

You will be required to have free accounts with the following services:

+ [Github](https://github.com/)
+ [CartoDB](http://cartodb.com/)
+ [Google](https://accounts.google.com/signup?service=mail)

<!-- + [Twitter](https://twitter.com/signup)-->


<!--
+ [Slack](
Tumblr - https://www.tumblr.com/register
-->

Time will be set aside to help you register and setup these accounts, but please try to come to the first session having already registered for these servies.

In addition, please install the following applications prior to class:

+ [Slack](https://slack.com/)
+ [OpenRefine](https://github.com/OpenRefine/OpenRefine/releases/tag/2.6-rc.2)
+ A free text editor of your choice
	+ [Sublime Text](https://www.sublimetext.com/) (All systems)
	+ [TextWrangler](http://www.barebones.com/products/textwrangler/) (All systems)
	+ [Notepad++](https://notepad-plus-plus.org/) (Windows)

###### [back to top](#top)

<a id='course-readings'></a>
### Course Readings 
The required readings for this course consist of book chapters, newspaper articles, and short blog posts. The intention is to help give you a foundation in the critical skills ahead of class lectures. All required readings are available online or will be made available through the class portal. Recommended readings are suggestions if you wish to study further the topics covered in class. The books listed in the Suggested Readings section below offer even more depth and an extended discussion of the material we cover in class. **Readings are due for the class under which they're listed.**

###### [back to top](#top)

<a id='class-format'></a>
### Class Format 
Class runs from 6:30pm to 9:30pm, with the class time broken up into two 85-minute blocks with a single 10-minute break around the half-way point of the class. Class will be a mix of lecture and practical exercise work, emphasizing the application of skills covered in the lecture portion of the class. 

I will also be available for questions or further assistance before and after class. You will have ample time in class to work on practical exercises based on the information presented in lectures. When possible, the final half hour of class will be set aside for any additional questions or additional tutorials in tools, skills, or techniques. Please plan on attending the full class time.

###### [back to top](#top)

<a id='submitting-assignments'></a>
### Submitting Assignments
All assignments will be submitted by adding your content to the [class page](https://github.com/datapolitan/MiningTheWeb) and issuing a "[pull request](https://help.github.com/articles/using-pull-requests/)" in the [class repository](https://github.com/datapolitan/MiningTheWeb). All of this will be explained, setup, and otherwise clarified on the first day of class. **Assignments aren't considered submitted until the pull request has been issued.** We will have ample time in class to address any technical issues and a reference guide for the process.

###### [back to top](#top)

<a id='assessment'></a>
### Assessment
Area | Total Points
--- | ---
Attendance | 20
Class Participation | 20
Visualization Critiques | 20
Visualizations | 20
Final Project | 20
**Total** | **100**

###### [back to top](#top)

<a id='class-policies'></a>
### Class Policies 
<a id='attendance'></a>
#### Attendance and Tardiness  
I expect you to attend every class, arriving on time and staying for the entire duration of class. Daily attendance counts 2 points toward your final grade. Excused absences won't result in points being lost. 
<a id='participation'></a>
#### Participation 
I expect you to be fully engaged while you’re in class. This means asking questions when necessary, engaging in class discussions, participating in class exercises, and completing all assigned work. Learning will occur in this class only when you actively use the tools, techniques, and skills described in the lectures. I will provide you ample time and resources to accomplish the goals of this course and expect you to take full advantage of what’s offered. Daily participation counts 2 points toward your final grade.
<a id='late-assignments'></a>
#### Late Assignments
All assignments are to be due before the start of class to be presented in class. Points will be taken off late assignments.
<a id='office-hours'></a>
#### Office hours
I won’t be holding regular office hours, but I’m happy to set up a time to meet in person, over the phone, or via Skype/Google Hangout if you have any problems. Please use [Slack](http://miningtheweb.slack.com) to reach out to me. I will also be available before or after class to provide any assistance you may need.

###### [back to top](#top)

<a id='resources'></a>
### Resources 
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

###### [back to top](#top)

----
<a id='course-outline'></a>
## Course Outline
#### Topics will be covered that day in class. Reading Assignments are to be read before class in preparation of the lecture and exercises. Assignments are due before the start of the next class and build on the information presented in class.

###### [back to top](#top)

----
## Week 1 - Acquiring Data
<a id='class1'></a>
### [Class 1 - April 11, 2016](http://www.datapolitan.com/MiningTheWeb/class1)
<a id='c1-topics'></a>
#### Topics 
+ What is open data?
+ Data on the web
+ Introduction to mapping
+ Introduction to open source tools and services for mapping and visualization

<a id='c1-assignments'></a>
#### Assignment
1. Complete the visualization started in class with data from an open data portal. Style the map in CartoDB and have it ready to present in class.
2. Find an interesting or visually compelling visualization online and write 2-3 paragraphs on the visualization, discussing the data source(s), the visual style, and how well the data was represented. Feel free to use the visualization resources listed above. Submit your text to the class page following the example shown.

<a id='c1-resources'></a> 
#### Resources
+ [CartoDB Academy](http://academy.cartodb.com/)

###### [back to top](#top)
----
<a id='class2'></a>
### [Class 2 - April 13, 2016](http://www.datapolitan.com/MiningTheWeb/class2)
<a id='c2-topics'></a>
#### Topics 
+ Introduction to HTML and CSS
+ Introduction to Git and [Github](http://github.com)
+ Guest lecture on [Save Harlem Now](http://www.saveharlemnow.org/)

<a id='c2-readings'></a>
#### Readings
+ Interactive Data Visualization for the Web, pg 15 – 23 
+ Matt A.V. Chaban, "[Much to Save in Harlem, but Historic Preservation Lags, a Critic Says](http://www.nytimes.com/2016/03/01/nyregion/much-to-save-in-harlem-but-historic-preservation-lags-a-critic-says.html?_r=0)" 

<a id='c2-assignments'></a>
#### Assignments
1. Complete the online [CartoDB “Online Mapping for Beginners”](http://bit.ly/1CyXW7p) course.
2. Create a second visualization or improve on your first, using new data or explore a data set from Save Harlem Now Project. Write 2-3 paragraphs discussing any challenges you encountered working with the data and/or creating your visualization in CartoDB.


<a id='c2-resources'></a>
#### Resources 
+ [Codecademy HTML and CSS Course](https://www.codecademy.com/en/tracks/htmlcss)
+ [W3Schools HTML Tutorial](http://www.w3schools.com/html/default.asp)
+ [A tutorial for getting started with Git and Github](http://bit.ly/1zlMfhK)

###### [back to top](#top)
----
## Week 2: More Acquiring Data/Data Cleaning

<a id='class3'></a>
### [Class 3 - April 18, 2016](http://www.datapolitan.com/MiningTheWeb/class3)
<a id='c3-topics'></a>
#### Topics 
+ Web scraping
+ Introduction to APIs
+ Introduction to OpenRefine

<a id='c3-readings'></a>
#### Readings
+ Chris Whong "[Foiling NYC's Taxi Trip Data](http://chriswhong.com/open-data/foil_nyc_taxi/)"
+ Thomas Levine, [Introduction to web scraping](https://thomaslevine.com/!/web-sites-to-data-tables/)
+ [Introduction to APIs ch 1-5](https://zapier.com/learn/apis/)

<a id='c3-assignments'></a>
#### Assignments
1. Find an interesting or visually compelling visualization online and write 2-3 paragraphs on the visualization, discussing the data source(s), the visual style, and how well the data was represented. Feel free to use the visualization resources listed above. Submit your text to the class page following the example shown.
2. Identify a question or topic you'd like to explore in this class, with the intention of creating a map related to the topics as part of your final project in this class. Write 2-3 paragraphs on why the topic is interesting to you, what data you'd like to explore using, and what you hope to contribute with your work.

<a id='c3-resources'></a>
#### Resources 
+ [School of Data: Cleaning Data with OpenRefine](http://schoolofdata.org/handbook/recipes/cleaning-data-with-refine/)
+ [Enipedia OpenRefine Tutorial](http://enipedia.tudelft.nl/wiki/OpenRefine_Tutorial)

###### [back to top](#top)
----

<a id='class4'></a>
### [Class 4 - April 20, 2016](http://www.datapolitan.com/MiningTheWeb/class4)
<a id='c4-topics'></a>
#### Topics 
+ Overview of social media data
+ Collecting social media data from APIs
+ Introduction to Python for querying APIs

<a id='c4-readings'></a>
#### Readings
+ TBD

<a id='c4-assignments'></a>
#### Assignments
1. Using an API, either of an open data portal such as the [NYC Open Data Portal](https://data.cityofnewyork.us/data) or some other open data source, create a visualization of the data in CartoDB. Write a short (2-3 paragraph) description of the data, the API you used to access it, how you styled it, and the resulting visualization. Discuss other data you'd like to use or other techniques of cleaning the data to get your desired result. Submit your API code via the Slack channel in the format "lastname-assignment2.py" if you do your API query in Python or "lastname-assignment2.txt" if you did you query in OpenRefine.
2. Update your project plan for your final project with additional questions, data sources, ideas for visualizing, or other issues/challenges you've discovered.

<a id='c4-resources'></a>
#### Resources 
+ [CartoDB Academy](http://academy.cartodb.com/)
+ McKinney, Wes. Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython. O'Reilly Media, Inc., 2012, "Appendix Python Language Essentials"
+ [Codecademy Python Course](https://www.codecademy.com/learn/python)
+ [MIT Introduction to Computer Science and Programming with Python](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/index.htm) (free course)
+ [Codecademy Learn to Code for APIs](https://www.codecademy.com/apis)


###### [back to top](#top)
----
## Week 3: Cleaning/Analyzing Data
<a id='class5'></a>
### [Class 5 - April 25, 2016](http://www.datapolitan.com/MiningTheWeb/class5)
<a id='c5-topics'></a>
#### Topics 
+ Introduction to SQL for cleaning data
+ Cleaning Data with APIs

<a id='c5-readings'></a>
#### Readings
+ Obe, Regina, and Leo Hsu. PostGIS in action. Manning Publications Co., 2011, Pg 3-8.

<a id='c5-assignments'></a>
#### Assignments
1. Find an interesting or visually compelling visualization online and write 2-3 paragraphs on the visualization, discussing the data source(s), the visual style, and how well the data was represented. Feel free to use the visualization resources listed above. Submit your text to the class page following the example shown.
2. Complete the [SQL and PostGIS in CartoDB](http://academy.cartodb.com/courses/04-sql-postgis.html) course.

<a id='c5-resources'></a>
#### Resources 

###### [back to top](#top)
----

<a id='class6'></a>
### [Class 6 - April 27, 2016](http://www.datapolitan.com/MiningTheWeb/class6)
<a id='c6-topics'></a>
#### Topics 
+ Python for querying Geoclient API
+ SQL for cleaning and analysis


<a id='c6-readings'></a>
#### Readings
+ TBD

<a id='c6-assignments'></a>
#### Assignments
1. Create a new visualization or improve on your previous visualization with additional data and provide analysis of the data you've found. Write 2-3 paragraphs on the visualization, discussing the data source(s), the visual style, and how well the data was represented.

<a id='c6-resources'></a>
#### Resources 

###### [back to top](#top)
----
## Week 4: Visualizing Data

<a id='class7'></a>
### [Class 7 - May 2, 2016](http://www.datapolitan.com/MiningTheWeb/class7)
<a id='c7-topics'></a>
#### Topics 
+ A (re-)introduction to statistics
+ Introduction to visualization design

<a id='c7-readings'></a>
#### Readings
+ Hon, Keone. “[An Introduction to Statistics.](http://www.fd.cvut.cz/department/k611/PEDAGOG/THO_A/A_soubory/statistics_firstfive.pdf)” Ch. 1 and 2.
+ Ben Wellington "[Mapping the Sharing Economy](http://iquantny.tumblr.com/post/110747103479/mapping-the-sharing-economy-an-in-depth-view-of)"

<a id='c7-assignments'></a>
#### Assignments
1. Find an interesting or visually compelling visualization online and write 2-3 paragraphs on the visualization, discussing the data source(s), the visual style, and how well the data was represented. Feel free to use the visualization resources listed above. Submit your text to the class page following the example shown.

<a id='c7-resources'></a>
#### Resources 

###### [back to top](#top)
----

<a id='class8'></a>
### [Class 8 - May 4, 2016](http://www.datapolitan.com/MiningTheWeb/class8)
<a id='c8-topics'></a>
#### Topics 
+ Advanced CartoDB (guest lecture)

<a id='c8-readings'></a>
#### Readings
+ Heer, Jeffrey, Michael Bostock, and Vadim Ogievetsky. "[A tour through the visualization zoo.](http://hci.stanford.edu/jheer/files/zoo/)" Commun. ACM 53.6 (2010): 59-67. 
+ Munzer, Tamara. Chapter 27 – “[Visualization](http://www.cs.ubc.ca/labs/imager/tr/2009/VisChapter/akp-vischapter.pdf)”, p 675-707, of Fundamentals of Graphics, Third Edition. by Peter Shirley and Steve Marschner. AK Peters, 2009. 
+ [CartoDB “Introduction to Map Design”](http://bit.ly/1ugu0tA)


<a id='c8-assignments'></a>
2
<a id='c8-resources'></a>
#### Resources 

###### [back to top](#top)
----
## Week 5: Advanced Topics/Final Presentations

<a id='class9'></a>
### [Class 9 - May 9, 2016](http://www.datapolitan.com/MiningTheWeb/class9)
<a id='c9-topics'></a>
#### Topics 
+ Course review
+ Advanced topics, to possibly include:
	+ Introduction to Interactive Visualization of Data with D3 and Leaflet
	+ Introduction to Spatial Databases
	+ Visualizing social media data

<a id='c9-readings'></a>
#### Readings

<a id='c9-assignments'></a>
#### Assignments
1. Find an interesting or visually compelling visualization online and write 2-3 paragraphs on the visualization, discussing the data source(s), the visual style, and how well the data was represented. Feel free to use the visualization resources listed above. Submit your text to the class page following the example shown.

<a id='c9-resources'></a>
#### Resources 

###### [back to top](#top)
----

<a id='class10'></a>
### [Class 10 - May 11, 2016](http://www.datapolitan.com/MiningTheWeb/class10)
<a id='c10-topics'></a>
#### Topics 
+ Final presentations


###### [back to top](#top)

----
<a id="suggested-reading"></a>
### Suggested Reading
+ Fry, Ben. *Visualizing Data: Exploring and Explaining Data with the Processing Environment*. O'Reilly Media, Inc., 2007.
+ Garrad, Chris. *Geoprocessing with Python*. Manning Publications Co., forthcoming. Janert, Philipp K. Data analysis with open source tools. O'Reilly Media, Inc., 2010.
+ McCallum, Q. Ethan. *Bad Data Handbook: Cleaning Up The Data So You Can Get Back To Work*. O'Reilly Media, Inc., 2012.
+ McKinney, Wes. *Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython*. O'Reilly Media, Inc., 2012.
+ Munzner, Tamara. *Visualization Analysis and Design*. AK Peters, 2014.
+ Murray, Scott. *Interactive data visualization for the Web*. O'Reilly Media, Inc., 2013.
+ Tufte, Edward R., and P. R. Graves-Morris. *The visual display of quantitative information*. Vol. 2. Cheshire, CT: Graphics press, 1983.

###### [back to top](#top)