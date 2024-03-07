# creative-text

This code includes Python functions for tagging creative text by specific keywords or phrases of the user's choice. This allows you to delve into deeper insights on specific creative messaging. 
The creative_text Python package includes functionality for intaking one or more Pathmatics Report Builder CSVs and outputs an identical CSV with added boolean columns for each creative text tag created by the user. 

This walkthrough and installation guide assumes no previous coding knowledge or understanding of Python, however if you would like to learn more about Python and its functionality, I highly recommend [Harvard's free CS50 Introduction to Programming with Python](https://www.edx.org/learn/python/harvard-university-cs50-s-introduction-to-programming-with-python) online course.

## Table of Contents

- [Anaconda Installation](#anaconda)
- [Visual Studio Code Installation](#installation)
- [creative-text Package Installation](#usage)

## Step 1: Anaconda Installation

I recommend installing Python through Anaconda which is an open source package and environment management tool commonly utilized in the data science field. I recommend installing Anaconda because it comes pre-installed with Python as well as a variety of commonly used packages. Additionally it provides a convenient UI that you can use to access much of the functionality that you normally would through the command line. The below link connects to the official Anaconda website where you can then install the 64Bit Graphical Installer for whichever operating system you are using.

[Anaconda Download Webpage](https://www.anaconda.com/download#downloads)

## Step 2: Visual Studio Code Installation

Next we will want to install a text editor that will allow us to write and interact with our code. My text editor of choice is Visual Studio Code or VS Code for short. VS Code is developed by Microsoft and is one of the most popular text editors. The below link connects to the official VS Code website where you can install it on whichever operating system you are using.

[Visual Studio Code Download Webpage](https://code.visualstudio.com/Download)

## Step 3: creative-text Package Installation

Next we need to install the creative-text package and its dependencies (other Python packages needed in order for creative-text to run). We need to do this via the command line (can be scary to interact with at first but all you will need to do is just some copying and pasting).

1. Open up a new terminal window

   - On Windows, click on the search bar and type "Command Prompt" to pull up a new terminal window.
   - On Mac, use the keyboard shortcut "Command + Space" and then type "Terminal" to pull up a new terminal window.

   Your terminal should look something like this (I am on Windows so your terminal will look slightly different on Mac, but the following commands remain the same between the two).

   ![image](https://github.com/BrandonCuy/pathmatics_creative_text_tagger_v2/assets/73131313/814f7620-3cab-4fa0-b9fb-43cb4cf72e83)

2. After you have a new terminal window open, copy and paste the following command into your terminal and click "enter".

    ```bash
    conda activate base
    ```

    You will notice that the word "base" will appear in parentheses at the start of your path.

   ![image](https://github.com/BrandonCuy/pathmatics_creative_text_tagger_v2/assets/73131313/2715f027-bbdc-4eac-8230-945281c3b035)

3. The next thing we need to do is install the creative-text package by copying and pasting the following command into your terminal and click "enter". This will install the most recent stable version v1.0.0 of the creative-text package.

    ```bash
    pip install git+https://github.com/BrandonCuy/pathmatics_creative_text_tagger_v2.git@v1.0.0
    ```
    
4. And lastly, we need to install the project's dependencies (other packages needed in order for the creative-text package to work)

    ```bash
    pip install git+https://github.com/BrandonCuy/pathmatics_creative_text_tagger_v2.git@v1.0.0
    ```

