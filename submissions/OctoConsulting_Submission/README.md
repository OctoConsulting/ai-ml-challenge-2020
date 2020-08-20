# Background Information

An EULA is a legal contract between the manufacturer of a software and it's End User.  EULA's are legal documents and are written in formal language.  This makes them unaccessible to users who have a hard time understanding legal language and can leave them vulnerable to unacceptable clauses.

# The Solution

A machine learning, artificial intelligence driven, user friendly application that is easy to understand and run on your computer.


# Description of Solution 

A user navigates to the webpage, uploads a EULA pdf or word doc via drag and drop or via the upload button, the document is processed using our AI/ML pipeline, and then the user is presented with a results page which contains the original document and cards containing the clause, the percent acceptable score, and the classification of acceptable or unacceptable.

# Architecture Diagram
![GSA EULA Architecture Diagram (1)](https://user-images.githubusercontent.com/17444067/90678596-e3697880-e22c-11ea-9280-f3f33c943c47.png)










# Installation steps: 
## To Run the Flask Server

Install Docker from [here.](https://docs.docker.com/desktop/). To get the docker image, you can either build from source or download from dockerhub

**To run from dockerhub (easier), run the command `docker run -p5000:5000 mee42/octo-gsa-ai flask_app.py`.**

To build from source, Open a different terminal and path to the backend folder in the submissions. Checkout the works branch, navigate to the backend directory, and build the DockerFile using the command `docker build -t gsa-ai:latest .` To run, do `docker run -p5000:5000 gsa-ai:latest flask_app.py`.

### go to https://octoconsulting.github.io/GSA-AI and click upload in the top right corner

If you want to build from source: 
1. Download/Clone this GSA-AI github repo to your local computer.
2. Download and install these dependencies: python3 and npm (pip install npm) 
3. Open your terminal and path to the frontend folder in the submissions folder
    and run `npm install` in your terminal.
4. Then run `npm start` and after it finishes open your web browser and go to localhost:4200




# For more information: 
Checkout our Wiki. 



