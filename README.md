# Car Generator
## Core Project

Contents
* Resources
* Breif
  * Requirements
  * My Approach
* Architecture
  * App Architecture
  * Database Structure
  * CI Pipeline
  * Cluster
* Project Tracking
* Risk Assessment
* Testing
* Git
* Docker
* Ansible
* Nginx
* Jenkins
* Front-End Design
* Issues
* Future Improvements


### Resources
[Trello Board](https://trello.com/b/EonadklO/core-project)  
[Risk Assessment](https://docs.google.com/spreadsheets/d/1-UdjCUO-fQm1SgKLLMErl-8Uanb5s3N-4sEWApghpvM/edit?usp=sharing)

### Brief

#### Requirements
The minimum viable product (MVP) was to create an application that utilises a service-orientated
architecture with at least 4 micro-services working together using supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training so far. We also had to include:
* A Trello board with full expansion
on user stories, use cases and tasks needed to complete the project.
* An application that follows a service-oriented architecture which must be deployed using containerisation and an orchestration tool.
* A relational database used to store data persistently for the
project
* Documentation from a design phase describing the application architecture
and a detailed Risk Assessment
* Fully designed test suites for the application, as
well as automated tests for validation of the application
* A functioning front-end website and integrated API's, using Flask
* Code fully integrated into a Version Control System using the
Feature-Branch model which will subsequently be built through a CI
server and deployed to a cloud-based virtual machine.
* Webhooks emplaced to automatically recreate and redeploy through CI server Jenkins when changes are made.
* An Ansible Playbook that will provision the environment that the application needs to run.
* A reverse proxy to make the application accessible to the user.

#### My Approach
To fulfil these requirements I decided to make an application with 4 services which
communicate with each other and will return a random Car Manufacturer and Car Type
and will return a price of the Car.
Below is the structure of my services:
* Service 1: Renders a template which displays results from other 3 services
* Service 2: Returns a random Car Manufacturer 
* Service 3: Returns a random Car Type
* Service 4: Returns the price of the car generated which is calculated using the output of both Service 2 and 3 
(each Car Manufacturer and Type were assigned a price)

### Architecture

#### App Architecture
Service 1 runs as the core which communicates with the other 3 services, and has a relation to an SQL database. 
Service 2 and 3 will act as generators, producing a random Car Manufacturer and Car Type (objects), that service 
4 will use to create the total Price (outcome), in which service 1 will display to the user.
Data entries stored in the MySQL database are connected to a database volume (used to persist data created and used by the MySQL container).  
![app-arc](https://github.com/kirankalsi/core_project/blob/main/images/app-arc.png)

#### Database Structure
I have created an entity relationship diagram (ERD) to show the structure of my database.
As my database only stores the generated Car Manufacturers, Types and calculated Price; it 
only requires one table.
##### ERD Diagram
The image below shows my ERD diagram.  
![erd](https://github.com/kirankalsi/core_project/blob/main/images/vehicle-db.png)

#### CI Pipeline
When starting my application I had not yet learnt about all the technologies required for this project.
The image below shows my inital thoughts on the CI Pipeline.
##### Initial CI Pipeline
![initial-pipeline](https://github.com/kirankalsi/core_project/blob/main/images/CI-pipeline2.png)  
The next image below represents my final continuous integration pipeline with the associated frameworks and services related to them.
It is a breakdown of the services and tools used to develop and deploy a well-tested, functioning program.
The services I have chosen within the pipeline provide the most efficient method of rapid development to be automated and tested.
##### Final CI Pipeline
![final-pipeline](https://github.com/kirankalsi/core_project/blob/main/images/CI-pipeline3.png)

#### Cluster
In my cluster (group of virtual machines). Initially I wanted to have one Swarm manager with 2 Swarm workers. As presented in the diagram below.  
![ideal-cluster](https://github.com/kirankalsi/core_project/blob/main/images/cluster.png)  
Unfortunately, when configuring my cluster I had issues with deploying worker1 in the Ansible playbook,
so I decided to have one swarm manager and only one worker. As shown in the diagram below.  
![actual-cluster](https://github.com/kirankalsi/core_project/blob/main/images/actual-cluster.png)  
Using Docker Swarm made it easier for me to manage multiple containers deployed across the cluster.

### Project Tracking
Before starting on the code of my application a Trello board 
was set up and used to track the progress of the project and to demonstrate my workflow, from planning to testing and finally to completion.
Throughout this project I ran 2 sprints. Below is a screenshot of my first sprint which encased the development side of the project, where my aim was 
to build the essential software functionality.  
![trello1](https://github.com/kirankalsi/core_project/blob/main/images/sprint1.PNG)  
Below is a screenshot of my second sprint which encased the operations side of the project.  
![trello2](https://github.com/kirankalsi/core_project/blob/main/images/sprint2.PNG)  
You can find the full Trello Board [Here](https://trello.com/b/EonadklO/core-project)

### Risk Assessment
It is always important to carry out a risk assessment for any project.
Below is a screenshot of my risk assessment for the project. This is where I have outlined potential risks, their impacts and mitigation techniques that I may need.  
![riskassessment](https://github.com/kirankalsi/core_project/blob/main/images/riskassessment.PNG)  
The full document can be found [here](https://docs.google.com/spreadsheets/d/1-UdjCUO-fQm1SgKLLMErl-8Uanb5s3N-4sEWApghpvM/edit?usp=sharing)

### Testing
I used Pytest to run unit tests on my application in which I tested all of my services.
When running pytest --cov --cov-report term-missing I could see which parts of my application were are not tested.
After updating my tests, the unit testing on my application folder in each service came to 100% coverage overall.
You can also see these coverage reports in the jenkins logs as I have used Jenkins to automatically run Pytest.
Below are summaries of the tests for each service:
* Service 1
Initially I found it difficult when testing service 1 as it required inputs from the other services. To get round this I imported a mock module, 
that allowed me to mock the get requests sent. Therefore a mock unit test was conducted to replicate 
API results from the application (without it being live) to check if the same results were produced in order to pass the test.  
![test-app1](https://github.com/kirankalsi/core_project/blob/main/images/test-app1.PNG)
* Service 2
A unit test was conducted to ensure a random Car Manufacturer was generated from a list of 7 options using a get request 
and asserting it back to check if the result would pass.  
![test-app2](https://github.com/kirankalsi/core_project/blob/main/images/test-app2.PNG)
* Service 3
A unit test was conducted to ensure a random Car Type was generated from a list of 7 options using a get request 
and asserting it back to check if the result would pass.  
![test-app3](https://github.com/kirankalsi/core_project/blob/main/images/test-app3.PNG)
* Service 4
Unit tests were conducted to ensure the post request returned the correct price.  
![test-app4](https://github.com/kirankalsi/core_project/blob/main/images/test-app4.PNG)  
I then made a container to run these tests in my Jenkins Pipeline (lightweight virtual environments used to package up code with its necessary dependencies).

### Git
I used Git as a version control system with GitHub as the provider. Github has allowed me to checkout different branches of the project 
 and focus on features individually. I would merge code into my main branch once I know everything is functioning properly. Usually I would delete
my branch after it has been merged, but for the purpose of this project I have kept them to show I was following the
Feature-Branch model. Below is a screenshot of my branches.  
![branches](https://github.com/kirankalsi/core_project/blob/main/images/branches.PNG)

I also implemented GitHub's webhooks feature so my code can be polled by Jenkins' build triggers (automatic builds).

### Docker
I used Docker and Docker-compose as the containerisation tools. Docker allowed me to build the environments I needed to allow the application to run
 in an automated and consistent manner - this was great as if I made any changes to the code it did not impact the performance of the app as it ran.
Providing the application with its own environment allows it to be recreated across any machine with Docker on it.
Docker-compose allowed me to run multiple containers using a configuration file which made the process of 
launching each service itself much easier and alot more efficient.
I used Docker Swarm as the orchestration tool. ...

### Ansible
I used Ansible as my configuration management tool to set up my cluster. I did this by creating a playbook, inventory & roles - 
in order to install Docker and configure my virtual machines which are eventually deployed as a Swarm. Ansible was very handy as 
it helped to automate and simplify repetitive tasks.

### Nginx
I used Nginx as a reverse proxy, which handled all traffic and requests before being sent to the application.
Each VM used Nginx as a web server to connect to the application on port 80, instead of the Flask port 5000.

### Jenkins
I used Jenkins as my CI Server. This allowed me to deploy my application very easily by creating a Jenkins Pipeline job 
using a multi-stage pipeline script.
The GitHub webhook feature was particularly useful as whenever I commited a change to my source code 
GitHub informed Jenkins and would automatically start a build, this is something I will be demonstrating in the demo.
My build logs are stored in Jenkins. During the initial attempt of deploy the application experienced some problems as reported below, 
but eventually all successfully passed.  
![jenkinslogs2](https://github.com/kirankalsi/core_project/blob/main/images/jenkinslogs2.PNG)
![jenkinslogs1](https://github.com/kirankalsi/core_project/blob/main/images/jenkinslogs1.PNG)  
After many more commits (approx. 60) I managed to create a build including ansible to run successfully aswell.  
![ansible-success](https://github.com/kirankalsi/core_project/blob/main/images/ansible-success.PNG)

### Front-End Design
My front-end design is still in its early stages as it is built using basic HTML. However it meets the MVP
and I am happy with its functionality. Below is the main page which provided by service 1. 
It generate a random Car Manufactuer and Type then displays the price of it.  
![homepage](https://github.com/kirankalsi/core_project/blob/main/images/website.PNG)

### Future Improvements
This application successfully implemented ...with 4 services. However there are a number of improvements I would like to implement:
* Nginx to run as a load balancer
* Fixing the second worker node
* Integrate project tracking with VCS to automatically keep track the project
* Set up email server to send messages when build fails
* Include forms so users can input their own Car Manufacturers/Types to be add to the list of random options
* Make the application more user friendly to improve the overall user experience (eg: include images)
