....PET-SHOP-GITOPS PROJECT...

THIS PROJECT WAS SELF INITIATED

ALL FILES SELF CODED WITH THE OF GEMINI

------Deployment------
What is a Virtual Environment?
A virtual environment in Python is an isolated environment on your computer, where you can run and test your Python projects.

It allows you to manage project-specific dependencies without interfering with other projects or the original Python installation.

Think of a virtual environment as a separate container for each Python project. Each container:

Has its own Python interpreter
Has its own set of installed packages
Is isolated from other virtual environments
Can have different versions of the same package
Using virtual environments is important because:

It prevents package version conflicts between projects
Makes projects more portable and reproducible
Keeps your system Python installation clean
Allows testing with different Python versions

Creating a Virtual Environment

To create a virtual environment on your computer, open the command prompt, and navigate to the folder where you want to create your project, then type this command: "python -m venv pet-shop-gitops"

This will set up a virtual environment, and create a folder named "pet-shop-gitops" with subfolders and files, like this:
pet-shop-gitops
  Include
  Lib
  Scripts
  .gitignore
  pyvenv.cfg
  
Activate Virtual Environment: "pet-shop-gitops\Scripts\activate"

now in the working enviroment i install flask with: "pip install flask"

ran the app: "python app.py" port 5000

Deactivate Virtual Environment: "Deactivate"

then git push to my main branch in github.

TO CONTAINIRIZE THE APPLICATION

Ran: "docker build -t my-python-app" .(this build the image)

Ran: "docker images" to view the built image

run and a container:

Ran: "docker run -d -p 5000:5000 my-python-app"

NOTE: ensure your docker desktop is up and running or you install docker on your virtual machine.

on the browser: "localhost:5000".
