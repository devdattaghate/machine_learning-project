# machine_learning-project
This is my first ML project.
CI CD pipeline has been established 

creating conda environment 
'''conda --version'''

'''conda create -p venv python==3.7 -y'''

'''conda activate venv/'''

'''pip install -r requirements.txt'''

To add files to git 
'''git add.'''

OR

'''git add <file name>'''

> NOTE: To ignore file or folder from git we can write name of file/folder in .gitignore file'''

To check git status
'''git status'''

To check all version maintaned by git
'''git log'''

To create version/commit all changes by git 

'''git commit -m "message" '''

To send version/ changes to github

'''git push origin main'''

To check remote URL
'''git remote -v'''

To set CI/CD pipeline in heroku we need 3 information

1.HEROKU_EMAIL = devtempmail91@gmail.com
2.HEROKU_API_KEY = <>
3.HEROKU_APP_NAME = first-ml-regression-app

BUILD DOCKER IMAGE
'''
docker build -t <image_name> : <tag_name> .
'''
> NOTE: Image name for docker must be in lowercase & you required fast internet connection to build image. 

To list docker image
'''
docker images
'''

Run docker image
'''
docker run -p 5000:5000 -e PORT=5000 493ba49c29ea
'''

To check running container in docker 
'''
docker ps
'''

To stop docker container
'''
docker stop <container id>
'''
