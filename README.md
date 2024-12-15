# what_should_i_do
A starter web app for indecisiveness. 
Overview
The Decision Maker is a Django-based web application designed to help users make choices from predefined categories such as restaurants, games, movies, or activities. Users can also add their own options and use a coin toss feature for random decision-making.

This project was created as part of a class assignment to demonstrate proficiency in web application development using Django.

Features
Browse Categories: View options grouped by categories like Restaurants, Games, Movies, and Activities.
Add New Options: Extend categories with your own choices.
Coin Toss Tool: Get a randomized decision with a virtual coin toss.


Here's an updated Bug List section for your README file based on the issues you mentioned:

Bug List
Coin Toss CSS Issues:
The styling for the coin toss page is inconsistent. The CSS does not apply correctly.

"Add Option" Functionality:
The "Add Option" feature does not work as expected. User submissions do not update the database, and no options are saved.

General CSS Inconsistencies:
Pages within the app occasionally display with inconsistent styles.

Hardcoded Categories:
Current implementation uses hardcoded categories, limiting user flexibility. Users cannot create or delete categories dynamically.

Before you start, ensure you have the following installed on your system:
Python (version 3.8 or later)
Pip (Python package installer)

Download the Project

Click the green Code button in the repository.
Select Download ZIP.
Extract the ZIP file to your desired directory.
Navigate to the Project Directory Open a terminal and move to the project folder:

cd path/to/your/extracted/folder
Set Up a Virtual Environment (Optional)

python -m venv venv
source venv/bin/activate   
venv\Scripts\activate     
Install Dependencies Use pip to install the required Python packages:

pip install -r requirements.txt
Set Up the Environment Variables Create a .env file in the project’s root directory and add the following:

DJANGO_SECRET_KEY=your-secret-key
DEBUG=True in settings.py

Apply Database Migrations Initialize the database and apply migrations:
python manage.py migrate

Run the Development Server Start the Django development server:
python manage.py runserver




