# creative-text

This code includes Python functions for tagging creative text by specific keywords or phrases of the user's choice. This allows you to delve into deeper insights on specific creative messaging. 
The creative_text Python package includes functionality for intaking one or more Pathmatics Report Builder CSVs and outputs an identical CSV with added boolean columns for each creative text tag created by the user. 

This walkthrough and installation guide assumes no previous coding knowledge or understanding of Python, however if you would like to learn more about Python and its functionality, I highly recommend [Harvard's free CS50 Introduction to Programming with Python](https://www.edx.org/learn/python/harvard-university-cs50-s-introduction-to-programming-with-python) online course.

## Table of Contents

- Anaconda Installation
- Visual Studio Code Installation
- Example Workbook Download
- creative-text Package Installation

## Step 1: Anaconda Installation

I recommend installing Python through Anaconda which is an open source package and environment management tool commonly utilized in the data science field. I recommend installing Anaconda because it comes pre-installed with Python as well as a variety of commonly used packages. Additionally it provides a convenient UI that you can use to access much of the functionality that you normally would through the command line. The below link connects to the official Anaconda website where you can then install the 64Bit Graphical Installer for whichever operating system you are using.

[Anaconda Download Webpage](https://www.anaconda.com/download#downloads)

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

   Your terminal should look something like this (I am on Windows so your terminal will look slightly different on Mac, but the following commands remain the same between the two).

   ![image](https://github.com/BrandonCuy/pathmatics_creative_text_tagger_v2/assets/73131313/814f7620-3cab-4fa0-b9fb-43cb4cf72e83)

2. After you have a new terminal window open, copy and paste the following command into your terminal and click "enter".

    ```bash
    conda create --name creative_text
    ```

    It will ask you "Proceed ([y]/n)?. Simply type 'y' and then hit enter. What we have just done was create a new Python environment named "creative_text" which is a way for us to isolate specific packages that we need to make our code work.

3. After we have successfully created our virtual environemnt, we need to activate it by simply copying and paste the following command into your terminal and click "enter".

    ```bash
    conda activate creative_text
    ```

    You will notice that the words (creative_text) will now appear in parenthesis on your screen. This means that we have successfully activated our environment.

    ![image](https://github.com/BrandonCuy/pathmatics_creative_text_tagger_v2/assets/73131313/3a3d5ff4-370f-47f5-84d5-77ad255f7aa0)

4. Now that we have our environment activated, we first need to install a package called 'pip' which will allow us to install the Creative Text Tagger. To do this, simply copy and paste the following command into your terminal and click "enter".

    ```bash
    conda install pip
    ```

    It will again ask you "Proceed ([y]/n)?. Simply type 'y' and then hit enter.
   
5. The last thing we need to do is install the creative-text package by copying and pasting the following command into your terminal and click "enter". This will install the most recent stable version v1.1.0 of the creative-text package as well as all of its dependencies (packages that this package is built on). It might take some time to finish downloading everything, but once it is complete, we should be good to go.

    ```bash
    pip install git+https://github.com/BrandonCuy/pathmatics_creative_text_tagger_v2.git@v1.1.0
    ```

6. The last thing we need to do is install the creative-text package by copying and pasting the following command into your terminal and click "enter". This will install the most recent stable version v1.1.0 of the creative-text package as well as all of its dependencies (packages that this package is built on). It might take some time to finish downloading everything, but once it is complete, we should be good to go.

    ```bash
    pip install -r https://github.com/BrandonCuy/pathmatics_creative_text_tagger_v2/raw/v1.1.0/requirements.txt
    ```