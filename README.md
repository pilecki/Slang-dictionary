# Slang Dictionary
Practical Python and Data-Centric Development Milestone Project for Code Institute. This dictionary was created for the purpose to demonstrate both potential future employers and tutors skills acquired during my study at Code Institute. 

# Demo
A live demo can be found [here:]()

# UX
The purpose of the site is allowing users browsing, adding, editing and deleting entries in the dictionary.

A primary aim in creating the design was the simplicity of the form so that the users know how to use the dictionary without being instructed. I used as less as possible elements to obtain such an effect. The website is divided into sections to meet user expectations, which are:
1.	As a user, I want to be able to get every part of the site so that I could discover content quickly.
2.	As a user, I want a home button, so that if I got lost, I could go back to the homepage. 
3.	As a user, I want to be able to edit entries so that I could help correct mistakes in the dictionary.
4.	As a user, I want to be able to delete entries so that I could remove inappropriate entries.
5.	As a user, I want to be able to add entries so that I could contribute to developing the dictionary.
6.	As a user, I want to be able to search the dictionary so that I could find entires that interest me.
7.	As a user, I want a brief description of the dictionary so that I know the purpose of the dictionary. 
8.	As a user, I want entries divisions into words ordered alphabetically as well as divided in regard category so that I could find words quickly. 
9.	As a user, I want the website to have calm colours so that my eyes not get tired quickly.

 

# Technologies
- This project uses HTML, CSS, Javascript and Python programming languages.
- [Cloud9](https://c9.io) - This developer used **Cloud9** for their IDE while building the website.
- [Bootstrap](https://www.getbootstrap.com/)
    - The project uses **Bootstrap4** to simplify the structure of the website and make the website responsive easily.
- [Google Fonts](https://fonts.google.com/)
    - The project uses **Google fonts** to style the website fonts.
- [jQuery](https://jquery.com/)
    - The project uses **jQuery** to reference Javascript needed for the responsive navbar.
- [Popper.js](https://popper.js.org/)
    - The project uses **Popper,js** reference Javascript needed for the responsive navbar.
- [Flask]()
    - The project uses **Flask** to build the website application.
- [MongoDB](https://www.mongodb.com/)
    - The project uses **MongoDB** to host the dictionary with its entries.
- [Python](https://www.python.org/)
    - The project uses **Python** to build the website application.
# Features

- The site uses the navbar feature provided by the Bootstrap framework, which is responsive regardless of what device user use. 

- An edit entry function that allows for editing the entry.
- An add entry function that allows for inserting the new entry.
- A delete function that allows for deleting the entry.
- A search function that allows for finding words in regard category or the first letter of the entry.
- A function that adds the date automatically while editing or inserting the entry in the dictionary. 
- A function that shows last added words into the dictionary.
- A function that provides how many words the dictionary contains. 


# Features left to implement

- A like button for each entry
- A validation of input data. 



# Testing

The developer used **W3C CSS Validation Service** and **W3C  Markup Validation Service** to check the validity of the website code.

- [W3C CSS validation](https://jigsaw.w3.org/css-validator/)
- [W3C Markup Validation]( https://validator.w3.org/)


**UX testing**
- As a user, I want to be able to get every part of the site so that I could discover content quickly.
    - The website is contained on a single website. The information provided is reasonably placed and well-sized. 
    - The Navbar occupies the whole width of the website and contains links to entries divided into categories and the first letter of the entry. 
    - Below the navbar, there are all letters of the alphabet leading to entries starting with the particular letter.
    - In mobile devices all the letters are hidden, avoiding the cluttering of the screen. 
    - Under the horizontally lined letters, there is the search bar with the search and the add entry button.

- As a user, I want a home button, so that if I got lost, I could go back to the homepage. 
    - The name of the dictionary is a link that takes the user to the main page. 
    - Another means to get to the main page is the home button in the navbar which in comparison to the name-link is also available on mobile devices.

- As a user, I want to be able to edit entries so that I could help correct mistakes in the dictionary.
    - When the entry is chosen at the bottom of each table, there is the edit button. 
    - When clicked the edit entry form is shown where information about the entry can be edited.
    - After editing, the user can submit changes using the submit button provided.  
- As a user, I want to be able to delete entries so that I could remove inappropriate entries.
    - When the entry is chosen at the bottom of each table, there is the delete button.
    - After pressing the delete button, the entry is removed from the database.
- As a user, I want to be able to add entries so that I could contribute to developing the dictionary.
    - Next to the search bar, the add entry button is placed. 
    - When clicked the add entry form is shown where information about the entry can be added.
    - After filling all the fields, the user can submit changes using the submit button provided.  

- As a user, I want to be able to search the dictionary so that I could find entires that interest me.
    - The search bar is easily accessible, being placed in the middle of the page.
    - In the input field, the user is required to provide the name of the entry and click the search button to get information about the entry.
    - Each entry is returned in the form of the table.

- As a user, I want a brief description of the dictionary so that I know the purpose of the dictionary. 
    - The main page contains a short description of the website and its primary purpose.

- As a user, I want entries divisions into words ordered alphabetically as well as divided in regard category so that I could find words quickly. 
    - Both functionalities are contained in the navbar.
    - In addition to that, the letters-links leading to the words starting with a particular letter are placed on top of the search bar. 
- As a user, I want the website to have calm colours so that my eyes not get tired quickly.
    -   The colour scheme used is easy on the eye. Cool colours are not tiring the eyes, giving a sense of peace to the user.


A website was manually tested on various mobile devices(iPhone5,6,7, Ipad, Samsung Galaxy, Sony Xperia) and multiple web-browsers (Chrome, Mozilla Firefox, Opera, Internet Explorer, Edge, Safari) to ensure compatibility and responsiveness. 





# Deployment
The website is published using hosting service Heroku taking files straight from a repository on GitHub. The site is updated automatically after new commits pushed.

To deploy this page to Heroku from its GitHub repository, the following steps were taken:

1. Log into your Heroku Account and Create a New App
2. Use Heroku (Web) UI to Deploy the Application
3. In the deployment method connect your Heroku app to the GitHub Repository you created.
    1. Click on the "Connect to GitHub" button
    2. Search for the repository Slang-dictionary
    3. Click on "Connect" button.


To deploy this page using CLI, the folowing steps can be taken:
1.  Download and install the Heroku CLI.
2. ```heroku login``` 

3.  Use Git to clone slang-dictionary's source code to your local machine.
4.  ```heroku git:clone -a slang-dictionary```
5.  ```cd slang-dictionary```
6.  Make some changes to the code you just cloned and deploy them to Heroku using Git.

7.  ```git add. ```
8.  ```git commit -am "make it better"```
9. ```git push heroku master```

## Content
The developer translated the a description of the dictionary which was taken from [here](https://www.miejski.pl/)

Definitions for words were taken from the [Cambridge dictionary](https://dictionary.cambridge.org/).

## Acknowledgements

The inspiration for making the dictionary was taken from [here](https://www.miejski.pl/).