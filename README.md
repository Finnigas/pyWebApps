# App Engine Standard Flask Tutorial App

Please complete these steps ahead of the first tutorial.
At the end of these steps you will have:
- A new Google App Engine project set up in your Google account
- A correctly set up local Python environment including the necessary Python packages
- The Google Cloud SDK installed and configured to make use of your new Google App Engine project

This means you'll have everything set up for your local development and then to later deploy your application to the Google Cloud. This will take about an hour, but is totally worth it!

If at any point you get stuck, you can email me (see email from Miranda for address).
If some of the steps feel a little mysterious or arbitrary, don't worry we can go through what they mean during our first session together.


1. Set up your Python environment using the instructions at: https://cloud.google.com/appengine/docs/standard/python/quickstart . Along the way you will need to install the Google Cloud SDK and to create a new project. During installation you will need to log in to your Google account.
2. Set up your virtual environment using the instructions at https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env#setting_up_libraries_to_enable_development (step 4) - make sure it's for python 2.7. (Using virtual environments is good practice when doing Python development as it allows you to keep each Python project in an isolated reproducible environment.) 
3. cd into this project directory. If you've followed the instructions correctly you should see `(env)` in your Bash command line prompt. You will need to _activate_ your virtual environment every time you want to work on the project:

    source env/bin/activate

4. install the dependencies using [pip](http://pip.readthedocs.io/en/stable/). This will install the necessary Python dependencies into your virtual environment.

    pip install -t lib -r requirements.txt
    
5. Run the project on your local computer. Note, if you have not added the executables of the Google Cloud SDK to your `PATH`, you will need to specify the location of the `dev_appserver.py` executable (i.e. `/path/to/google-cloud-sdk/bin/dev_appserver.py app.yaml`). The first time you run this, the SDK will download everything it needs to give you a local development environment that contains development versions of the various Google Cloud services.

    dev_appserver.py app.yaml
    
6. Voila. You are now ready to look at your first web app which is locally hosted on your machine. Go to [localhost:8080](http://localhost:8080) in your browser to see the live project. If all is working correctly you will see the words Hello world.

7. Besides creating and locally hosting your website, the Google Cloud SDK has also set up a control panel for you to configure settings for your website. Go to [localhost:8000](http://localhost:8080) in your browser to see the it's all working OK.
8. Well done, it's all easier from now on. Treat yourself to a cup of coffee!

This sample shows how to use [Flask](http://flask.pocoo.org/) to handle
requests, forms, templates,  static files and data stores within the Google App Engine runtime.

Files that we may need during our further development can be found in `snippets` and `templates/snippets`.
