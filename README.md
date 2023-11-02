# Github-Training-Repository
This repository is meant to be used to train new hires/volunteers on how to use Github. Reading the material and finishing the exercise should take around 6-8 hours.

Before you get started, please check that your actual name is visible on your Github profile. This way we know which account belongs to whom and when we make repositories citable your real name will be used and not your nickname. 

Also, if you read this and you are not yet part of the ALLFED group on Github, please let Florian know your account name, so it can be added. 

# Preparation Material
Please look at all those materials before you start the exercise.

* [Good enough practices in scientific computing](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510): This gives a good overview of why we need to adhere to good coding practices and what the general idea is
* [Good Research Code Handbook](https://goodresearch.dev/): Explanation of how to implement good coding practices in Python
* [Fundamentals of Git and Github](https://www.youtube.com/watch?v=8Dd7KRpKeaE)
* [How to use Github with Github Desktop](https://www.youtube.com/watch?v=8Dd7KRpKeaE)
* [Getting started with anaconda and conda](https://youtu.be/YJC6ldI3hWk) (if you feel like conda is too slow, check out [mamba](https://mamba.readthedocs.io/en/latest/) instead)
* [ALLFED Repository Template Readme](https://github.com/allfed/ALLFED-Repository-Template)
* [Overview of Python](https://www.youtube.com/watch?v=kqtD5dpn9C8)
* [Automated Testing](https://blog.deepjyoti30.dev/tests-github-python)
* [ChatGPT](https://chat.openai.com/chat) is pretty good at answering programming questions
* It is recommended to use [VS Code](https://www.youtube.com/watch?v=B-s71n0dHUk) as your code editor
* The [Seaweed Growth Model Repository](https://github.com/allfed/Seaweed-Growth-Model) can be seen as an example of how ALLFED repositories should look like. You can check how things are done there, if something here confuses you
* General info: If a repository in the ALLFED group is private, there is a high chance it is not in use anymore. Please check in with the owner before trying to run it. 

# Exercise
1. Fork this repository
2. Clone it to your local computer
3. Recreate the folder structure as described in the [ALLFED Guidelines](https://github.com/allfed/ALLFED-Repository-Template)
4. Create a local virtual environment for the repository
    * When you try to install/change things make sure are [activating it first!](https://goodresearch.dev/setup.html?highlight=activate#conda). If something related to virtual environments isn't working, always make sure that it is really activated. 
5. Create two files in the src folder: numerical.py and plotting.py
6. Write a function in numerical.py that takes at least one argument and returns a numerical value
7. Write a function in plotting.py that creates a scatter plot and uses the [ALLFED Style Sheet](https://github.com/allfed/ALLFED-matplotlib-style-sheet)
8. Make your repository an installable package as described in [Good Research Code Handbook](https://goodresearch.dev/setup.html)
9. Add a Jupyter Notebook in your scripts folder and import numerical.py and call it
11. Write two test for numerical.py
12. Make sure that the documenation of all code follows the [ALLFED Guidelines](https://github.com/allfed/ALLFED-Repository-Template#allfed-python-style-guide)
    * If you set-up automated documentation, you can see the status in the [pages setting](https://github.com/allfed/Seaweed-Growth-Model/settings/pages)
14. Automate the tests, so they run on every commit (you can just copy the files needed for that from [the template](https://github.com/allfed/ALLFED-Repository-Template)
    * The files used for testing in Github Actions are hidden files. You might need to change the settings of your operation system to show you the hidden files. 
    * you can play around with pytest in your terminal in VS Code
15. Create an environment.yml that specifies how your virtual environment can be recreated and save it in the repository
16. Send back a pull request, so we know you have finished this training
17. Check back in with Morgan or Florian if you have any questions (florian@allfed.info or morgan@allfed.info) 

If you get stuck at any point please reach out to one of the data scientists (either florian@allfed.info or morgan@allfed.info). 
