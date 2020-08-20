# Background Information

An EULA is a legal contract between the manufacturer of a software and it's End User.  EULA's are legal documents and are written in formal language.  This makes them unaccessible to users who have a hard time understanding legal language and can leave them vulnerable to unacceptable clauses.

# The Solution

A machine learning, artificial intelligence driven, user friendly application that is easy to understand and run on your computer.


# Description of Solution 

A user navigates to the webpage, uploads a EULA pdf or word doc via drag and drop or via the upload button, the document is processed using our AI/ML pipeline, and then the user is presented with a results page which contains the original document and cards containing the clause, the percent acceptable score, and the classification of acceptable or unacceptable.

# Architechture Diagram
![GSA EULA Architecture Diagram (1)](https://user-images.githubusercontent.com/17444067/90678596-e3697880-e22c-11ea-9280-f3f33c943c47.png)










# Installation steps: 
If build from start: 
1. Download/Clone this GSA-AI github repo to your local computer.
2. Open your terminal and path to the frontend folder in the submissions folder
    and run `npm install` in your terminal.
3. Then run `npm start` and after it finishes open your web browser and go to localhost:4200

otherwise use this: 
### go to https://octoconsulting.github.io/GSA-AI and click upload in the top right corner

# Now,
## To Run the Flask Server
Install Docker from [here.](https://docs.docker.com/desktop/)

Open a different terminal and path to the backend folder in the submissions.

Checkout the `works` branch.

Build the DockerFile using the command `docker build -t gsa-ai:latest .`

# For more information: 
Checkout our Wiki. 



