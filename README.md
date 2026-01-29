# creative-text

This code includes Python functions for tagging creative text by specific keywords or phrases of the user's choice. This allows you to delve into deeper insights on specific creative messaging. 
The creative_text Python package includes functionality for intaking one or more Pathmatics Report Builder CSVs and outputs an identical CSV with added boolean columns for each creative text tag created by the user. 

This walkthrough and installation guide assumes no previous coding knowledge or understanding of Python, however if you would like to learn more about Python and its functionality, I highly recommend [Harvard's free CS50 Introduction to Programming with Python](https://www.edx.org/learn/python/harvard-university-cs50-s-introduction-to-programming-with-python) online course.

## Video Tutorial

To make things easier for first time users, I have also recorded a tutorial video where I walk through the installation process of everything you will need in order to get the Creative Text Tagger up and running. I highly recommend taking a look at the tutorial video found at the link below.

[Brandon's Creative Text Tagger Package Installation Tutorial Video](https://sensortower.zoom.us/rec/share/XJwRXKfljwZRdCny4TMPJyD4B8WSXxKvtRTiBIbL5IPfOodZGy7m1H6Yaztq2XGS.4z87TanSMObfAhnL?startTime=1711142606000)

## Table of Contents

- Python Installation
- Visual Studio Code Installation
- Example Workbook Download
- creative-text Package Installation
- Using the Text Tagger in VS Code

## Step 1: Python Installation

In order to use this Python package, we have to obviously download Python first. You can download the latest version from the official Python website linked below:

[Official Python Download Webpage](https://www.python.org/downloads/)

## Step 2: Visual Studio Code Installation

Next we will want to install a text editor that will allow us to write and interact with our code. My text editor of choice is Visual Studio Code or VS Code for short. VS Code is developed by Microsoft and is one of the most popular text editors. The below link connects to the official VS Code website where you can install it on whichever operating system you are using.

[Visual Studio Code Download Webpage](https://code.visualstudio.com/Download)

## Step 3: Creative Text Example Workbook Download

In order to make the process of using these functions easier, I have created a sample that lives in a Google Drive folder. You can find the example in the following link and copy the entire folder to your own computer:

[Creative Text Example Workbook Google Drive](https://drive.google.com/drive/folders/1wZpnN7AM1UlJ8BVbpq2RHduL73Pm-_Zl?usp=drive_link)

## Step 4: creative-text Package Installation

Next we need to install the creative-text package and its dependencies (other Python packages needed in order for creative-text to run). We need to do this via the command line (can be scary to interact with at first but all you will need to do is just some copying and pasting).

1. Open up a new terminal window

   - On Windows, click on the search bar and type "Command Prompt" to pull up a new terminal window.
   - On Mac, use the keyboard shortcut "Command + Space" and then type "Terminal" to pull up a new terminal window.

   Your terminal should look something like this (I am on Mac so your terminal will look slightly different on Windows, but the following commands remain mostly the same between the two).

   <img width="564" height="110" alt="image" src="https://github.com/user-attachments/assets/39703bc1-9715-4942-9ecd-36993f40e094" />

2. Navigate to the Creative Text Example Workbook folder that you downloaded earlier

   Next we will need to change our current working directory to wherever you downloaded the Creative Text Example Workbook. To do this, you simple need to use the "cd" command followed by the path to where the folder lives.

   For me, that command looks like the following, but your path will be different depending on where you saved the "Creative Text Tagger Example" folder:
   
   ```bash
    cd Documents/brandon_projects/"Creative Text Tagger Example"
    ```

   You will notice that the words "Creative Text Tagger Example" will now appear in your terminal. This means you are in the correct folder now.

   <img width="463" height="48" alt="image" src="https://github.com/user-attachments/assets/de36ec3c-663f-4ffa-8a36-f3babc3082a0" />


3. Create a new venv virtual environment

   After you have a new terminal window open and are inside the directory of the "Creative Text Tagger Example" folder, we now need to create a venv virtual environment. To do this, copy and paste the following command into your terminal and click "enter".

    ```bash
    python3 -m venv creative_text_env
    ```

4. Activate the venv environment

   After we have successfully created our virtual environemnt, we need to activate it by simply copying and pasting the following command into your terminal and click "enter".

   For Mac:
   
    ```bash
    source creative_text_env/bin/activate
    ```
   

   For Windows
    ```bash
    .\creative_text_env\Scripts\activate
    ```

    You will notice that the words (creative_text_env) will now appear in parenthesis on your screen. This means that we have successfully activated our environment.

    <img width="1206" height="108" alt="image" src="https://github.com/user-attachments/assets/35beceb2-28dd-42a9-a6e6-28c9252bf525" />


5. Install the creative-text Package

   Now that we have our Conda environment activated, the next thing we need to do is install the creative-text package by copying and pasting the following command into your terminal and click "enter". This will install the most recent stable version v1.1.1 of the creative-text package. It might take some time to finish downloading everything.

    ```bash
    pip install git+https://github.com/BrandonCuy/pathmatics_creative_text_tagger_v2.git@v1.1.1
    ```

6. Install the creative-text Package Dependencies

   The last thing we need to do is install the dependencies of the Creative Text package (other packages that the Creative Text packages requires to run). We can do this by copying and pasting the following command into your terminal and clicking "enter".

    ```bash
    pip install -r https://github.com/BrandonCuy/pathmatics_creative_text_tagger_v2/raw/v1.1.1/requirements.txt
    ```

    And with that you should be good to go! You can now exit out of your command prompt.

## Step 5: Using the Text Tagger in VS Code

Once you have completed all of the previous steps, we just need to set up VS Code. Follow the below instructions to get everything set up to use:

1. Open up the VS Code program and Install Required Extensions

   VS Code is a text editor that has support for many different coding languages. In order to set our program up to use Python, we need to install some extensions first. To do this, first click on the square Tetris like symbol on the left hand side bar to open up the Extensions Tab.

   ![image](https://github.com/BrandonCuy/pathmatics_creative_text_tagger_v2/assets/73131313/7d04efa6-4edc-4e2b-815c-7ddbd806e733)

   Then you will want to install the "Python" extension
   ![image](https://github.com/BrandonCuy/pathmatics_creative_text_tagger_v2/assets/73131313/0bd10ba1-5081-416c-be24-2a9e008271c8)

   Lastly, you will also want to install the "Jupyter" extension
   ![image](https://github.com/BrandonCuy/pathmatics_creative_text_tagger_v2/assets/73131313/8dc1a992-2d9e-4294-944b-f3cdb74bed41)

2. Open up the Example Folder that You Downloaded in Step 3

   Next, we will want to open up the example that I have provided in the Google Drive link in Step 3. To do this, simply click on the document icon on the left side bar and then click "Open Folder". Then simply navigate to where you downloaded contents from the Google Drive.

   ![image](https://github.com/BrandonCuy/pathmatics_creative_text_tagger_v2/assets/73131313/01569bda-67ff-4fa9-8151-cfda501142d8)

   Once you have opened the folder, you should see a file directory appear in the Explorer tab on the left hand side bar. You will then want to click on the file titled "creative_text_tagger_template.ipynb". Once you do that, it should open up the file and look something like the below screenshot.

   ![image](https://github.com/BrandonCuy/pathmatics_creative_text_tagger_v2/assets/73131313/4de151d8-e679-488a-854e-686333efb5c1)

3. Select a Python Interpreter

   The last thing we need to do before running code, is select our Python interpreter. To do this click on the area cirlced in red in the screenshot below. Mine says "Python" but yours will likely say "Select Notebook Kernel"

   ![image](https://github.com/BrandonCuy/pathmatics_creative_text_tagger_v2/assets/73131313/7a0beda6-6a08-4665-8e5f-eaed15ec7d23)

   This will open up a dropdown at the top. Next what you want to do is click "Select Another Kernel..."

   ![image](https://github.com/BrandonCuy/pathmatics_creative_text_tagger_v2/assets/73131313/0a72db37-8188-40aa-b98f-b497a6920e01)

   Then select "Python Environments"

   ![image](https://github.com/BrandonCuy/pathmatics_creative_text_tagger_v2/assets/73131313/f5d0524f-3ac7-4bb5-a030-76377ddf4687)

   And lastly, you will notice that the "creative_text" Conda environment that we created in the terminal earlier will appear. This is what we want to use in order to run the package that we downloaded earlier.

   ![image](https://github.com/BrandonCuy/pathmatics_creative_text_tagger_v2/assets/73131313/32bc31d9-be1a-4343-8577-cf9303a61544)

   And with that you should be all set!


   

   



