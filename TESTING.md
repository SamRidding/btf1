# Testing 

## Table of contents.

- [Unit Testing](#unit-testing)
- [Manual Testing](#manual-testing)
- [Security](#security)
- [Code Validation](#code-validation)
- [Responsivity](#responsiveness)
- [Accessibility](#accessibility)
- [Issues](#issues)

# Unit Testing

I tested the relevent forms, models, urls & views for each app in the project using the Django Testing framework. The report attached used the python coverage package to show how what was covered by the automated testing, with a total of 93%:

<img src="readme-images/testing/coverage.png" width=600>

# Manual Testing

Manual testing was performed on for normal user usage, admin usage, and general site usage with on all pages. The record of these tests are below:

<img src="readme-images/testing/manualtesting.png" width=1000>

# Security

- Environment variables: these are stored in the env.py file during development and in the Heroku 'config variables during production

- User account: Used the python packed Django Allauth to handle user accounts

# Code Validation 

- #### CSS

    - All the website's CSS code has been passed through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) all custom code passes however errors and warnings are thrown regarding CSS delivered from the fontawseome CDN.

    <img src="readme-images/testing/csserrors.png" width=600>
    <img src="readme-images/testing/csswarnings.png" width=600>

- ## Javascript

     - JavaScript has been passed through the [JSHint Validator](https://jshint.com/) and it has passed without errors.

- ## Python

     - All custom Python code passed the [PEP8 online check](http://pep8online.com/)
     - The settings.py file does contain lines which are too long for pep8 compliancy however I have left these so as not to effect their functionality.


- ## HTML

     - HTML code passed the [W3C Markup Validator](https://validator.w3.org/)

     <img src="readme-images/testing/htmlvalid.png" width=600>







