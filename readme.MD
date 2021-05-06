# 🌠 Calm - mood diary (SE Foundations project)

Calm is a small project that I worked on for my SE Foundations course at CODE University of Applied Sciences Berlin. It is a web-app which basically allows you to track your mood every day by logging different parameteres, and you can easily reflect back on your days and potentially notice trends of reocurring happiness, stress or other emotions. The app is online and you can access it on https://calm-website-se-foundations.oa.r.appspot.com/

## 📊 Table of contents
* [Technologies](#technologies)
* [Installation Instructions](#installation-instructions)

# Technologies

#### The main technologies used in this project are the following:
- Python 3.8
- Flask 1.1.2
- SQLAlchemy 1.4.7


# 🖥 Installation Instructions

## Running the code locally
If you want to run this code locally, click on the "Code" button and then select download ZIP file. After the download has finished,
unzip the file and open the folder with your preferred choice of IDE.



## Before you launch the app... 
You should have:
- Python 3.8.x installed on your computer 
- Visual Studio Code (or another IDE of your choosing) installed on your computer 
- set up a Python virtual environment on your machine
- Download the Python modules listed in requirements.txt using pip. In case you are running Windows, uwsgi isn't availiable, so uncomment it in the requirements.txt. (uWSGI==2.0.19.1 => #uWSGI==2.0.19.1) before you execute the following command: 

    > pip install -r requirements.txt


### Setting up a virtual environment: 
- Open your IDE, and open the folder containing your locally cloned repository. Before editing the code, make sure everything works as expected, locally at least.  


- Open a terminal in VS Code, too. This should automatically be in the same directory as your repository, if not, you should change directory to be in there. 


- In the terminal, create a new virtual environment for this project, using Python 3.8.x. The exact command will depend on your operating system and setup, but the idea is the same: call the Python executable at the command line (e.g. `python` or `python3.8` or `python3` or maybe `\Python38\python` on Windows). Normally, that will open the Python REPL interface, but we don't want that this time - we want it to create a virtual environment for us. To do that, pass the argument `-m venv`, which tells Python "run the venv module". Then, give it one more argument which is the path to a folder name where the virtual environment will live. For ease and consistency, this should be called `venv` and live in the repository root folder. This command could look like this, in the end, depending on your setup:
    
    > python3.8 -m venv venv 


### Launching the app
**- Activate your virtual environment for this project:** 
   
    macOS/Linux: `source venv/bin/activate`

    Windows: `venv\Scripts\activate.bat`


- Run the local development server and make sure it all works. Instructions can be found at the top of this readme for using Flask's built in development server. Alternatively (only on macOS or Linux), you can use the command `uwsgi` to start your development server: 

> uwsgi --http-socket 127.0.0.1:5000 --wsgi-file calm_app/website.py --callable app --processes 4 --threads 2 --stats 127.0.0.1:8181 -H venv/

You should be able to run the website locally and see it in your local browser! 




