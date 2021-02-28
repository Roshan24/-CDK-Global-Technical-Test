# -CDK-Global-Technical-Test
CDK Global Customer Portal Technical Test

Dependencies:
- Python Flask
> $ pip install Flask
- Python version 3.9
https://www.python.org/downloads/



Instructions:
1. Open Command Prompt (Windows)/ Terminal (macOS)
2. Navigate to the directory that the solution "CDK_global_test" is stored in using command "cd"
> *e.g* - cd desktop/CDK_global_test

4. Once in Directory run the command
> python app.py

*This will run the script and host a local server on port: 5000*

6. To access the solution, navigate to a browser of your choice and enter the IP address:  127.0.0.1:5000




Reasoning:

"app.py" - Python Flask -

Python Flask is a web app framework based on the Jinja2 template engine, this allowed me to create a lightweight, reliable web application with a fast debugger. Reasoning for choosing Flask as a micro-framework is that it provides a scalable platform and simple development with flexibility enabling me to alter the program to suit the needs of the client and providing the perfect platform for this small lightweight web application task. In this case a form for the client to be able to enter in comments. This framework acted as the server side handler as well as  hosting communication between the html page and the .json data store.  Flask provided me with the simple and efficient tools to easily handle the json data and the ability to write and read from the case.json file whilst maintaining formatting. I was able to use “request.form” as a way of communicating data from the html form to the server side handler where i was able to use “jsondump()” which is the method used for writing data to the json file.

"home.html" - HTML / JS -

HTML-

Hosting the form on as HTML provides the perfect platform for a client in a real-world scenario, I was able to create a lightweight design that catered for the main functionality of the task, to add a comment to the record, update the last modified date and show the updated record. This enables me to have a form that communicates with python flask, acting as the server side handler to send data using POST functions to the handler for data storage to the .json file. It also enabled communication with flask that enables the reading of the .json file to visually show the record on the html page. The Design was intuitive by introducing simple animations, icons and features from the materialize js that was used as a stylesheet.

Materialize CSS-

I chose to use materialize js as the front-end framework, this allowed me to use responsive designs and animations and provide standard CSS with minimal space used. Allowed me to choose design for the input form and include Icons for client intunivity. Materialize provided a simple styling solution for this web application.
