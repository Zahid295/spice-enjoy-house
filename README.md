# Spice Enjoy House - A restaurant Booking system

 Spice Enjoy House is a web-based table booking application designed for a restaurant setting. The application allows users to book a table at their preferred time and date, and manage their bookings with ease. Developed using Python (Django), HTML, CSS, and a PostgreSQL database, this site offers a seamless and user-friendly experience for both customers and restaurant staff.

 ## User Goals and Stories

 ### User Goals

 As a user, I want to:

- Navigate the website easily and intuitively
- Browse the website naturally and with ease
- View the website and read all information on all screen sizes
- Create an account on the website
- Make a table booking at my preferred time and date
- Manage my bookings and change or delete them if needed.

### Business Owner Goals

As the website business owner, I want to:

- Provide users with information about the restaurant and its offerings
- Allow users to easily access and use the site
- Allow users to create table bookings
- Allow users to manage their own bookings
- Allow users to edit and delete their bookings
- Collect user information for booking purposes
- Allow staff to access and manage bookings
- Provide contact information to users

### User Stories

#### As a user:

- I want to visit the website and understand its purpose immediately
- I want to easily understand how to use the website
- I want to be able to contact the restaurant
- I want to create an account easily
- I want to input my information with ease
- I want to create a table booking with ease
- I want the ability to view my bookings
- I want the ability to change my bookings
- I want the ability to delete my bookings
- I want to have an enjoyable experience
- I want to return to the site to create another booking

#### As a Website Business Owner

- As a site owner, I want to provide users with a seamless experience to book a table at our restaurant
- As a site owner, I want to allow users to easily navigate the website without issues
- As a site owner, I want to encourage users to create an account for easy management of their bookings
- As a site owner, I want to allow users to manage their bookings, giving them the ability to edit or delete their bookings as needed
- As a site owner, I want to collect user information for booking purposes and to improve our services
- As a site owner, I want to allow staff to access and manage bookings efficiently
- As a site owner, I want to provide clear and accessible contact information to users
- As a site owner, I want to ensure the website is responsive and looks good on all devices to provide a positive user experience

#### As a New User

- I want to navigate the page intuitively and with ease
- I want to understand the page purpose upon first viewing
- I want to see restaurant contact information
- I want to be able to contact the restaurant directly
- I want to see the restaurant’s social media presence
- I want to easily create an account
- I want to easily create a table booking
- I want to edit or delete a booking
- I want to enjoy the experience and return to make another booking

## Design

### Font

The Spice Enjoy House web app utilizes the Arial font, a classic and widely-used typeface. This font was chosen for its clean, easy-to-read, and versatile characteristics, making it an ideal fit for a restaurant booking website. Arial is used for both the headings and the body to maintain consistency and readability across the site. For the h1 tags, a larger font size is employed to make them stand out and grab attention. This font selection not only pleases the eye but also aligns well with the restaurant market.

## Developement

### Agile Methodology

Agile methodology was used in the development of this project. The implementation status of all user stories and epics was monitored using the Github projects Kanban Board, which is accessible [here](https://github.com/users/Zahid295/projects/1)

## Technologies Used

- Python: The backbone of this project is Python.
- HTML: The structure of the website is built with HTML.
- CSS: The visual appeal of the website is achieved with CSS.
- GitHub: The codebase is hosted on GitHub.
- Codenaywhere: The development environment for the website was GitPod.
- Git: Git was the version control system used during development.
- Heroku: The live website is hosted on Heroku.
- PEP8 Validator: The Python code was validated using the PEP8 Validator.
- HTML - W3C HTML Validator: The HTML code was validated using the W3C HTML Validator.
- CSS - Jigsaw CSS Validator: The CSS code was validated using the Jigsaw CSS Validator.
- Chrome Dev Tools: Debugging during the project was done using Chrome Dev Tools.
- LightHouse: The performance of the website was tested using LightHouse.

## Features

### Home Page
The journey begins at the Home Page, the first stop for our users. It is designed to instantly give users a clear understanding of what Spice Enjoy House is all about. With gaining attention users are guided on how to navigate and utilize the website. The intuitive Navigation Bar and informative body section further enhance the user experience.

### Contact Us Page
We believe in open communication channels. The Contact Us Page is designed to facilitate direct interaction between users and our team. Whether it is a query, a concern, or feedback, users can reach out to us online which enhances their overall experience.

### Booking Page
At the heart of Spice Enjoy House is the ability for users to make reservations seamlessly. The Booking Page hosts a user-friendly form that logged-in users can fill out to secure their reservation. For users who are not logged in, they are conveniently redirected to the Login or Register Page.

### Booking Details Page
Transparency and control are key to a great user experience. The Booking Details Page, accessible only to logged-in users, allows users to view, edit, or delete their existing bookings. If a user opts to edit a booking, they are redirected to a pre-filled form where they can modify their reservation details as needed.

### Navigation Menu
The Navigation Menu is a consistent guide available on all pages. It contains links to Home, Contact Us, Make a Booking, and Booking Details. Additionally, it integrates with Django's allauth options to provide Login, Logout, and Register options, depending on the user's authentication status.

Here is a quick rundown of the navigation options:

Home (base.html) - Accessible to all
Contact Us (contact.html) - Accessible to all
Make a Booking (booking_form.html) - Accessible to logged-in users
Booking Details (booking_details.html) - Accessible to logged-in users
Logout (logout.html) - Accessible to logged-in users
Login (login.html) - Accessible to logged-out users
Sign up (signup.html) - Accessible to logged-out users

## Deployment

### Pre-Deployment Checklist

Before deploying on Heroku, ensure the following:

Update requirements.txt: This file should list all Python modules imported in the project, ensuring correct configuration on Heroku.
Create a Procfile: This file is crucial for Heroku to correctly configure the deployment as a gunicorn web app.
Configure settings.py: Update the ALLOWED_HOSTS list to include 'app_name.heroku.com', 'localhost'. Ensure all static files and directories are correctly configured.
Set Environment Variables: All environment variables in the env.py file (which is gitignored) must be correctly configured with the database URL, storage URL, and secret key. The hidden variables include SECRET_KEY, DATABASE_URL, CLOUDINARY_URL, and PORT.
Deploying on Heroku
Follow these steps to deploy Spice Enjoy House on Heroku:

Create a Heroku account. Optionally, sign up with a student account for credits.
Once logged in, select “Create a new app”.
Choose an app name and region.
Select the deployment method as “Connect to GitHub”.
Find the desired repository.
Enable automatic deploys and select the main branch.
In the settings tab, select “Reveal Config Vars”. Input the required hidden variables.
Select Node.js and Python as the buildpacks.
Deploy the app.
Forking the Repository
To create a personal copy of the repository:

Go to the GitHub repository.
Click on the “Fork” button in the upper right-hand corner.
Optionally, edit the repository name and description.
Click the green “Create Fork” button.
Cloning the Repository
To work on the project locally:

Go to the GitHub repository.
Locate the green “Code” button above the list of files and click it.
Select your preferred cloning method (HTTPS, SSH, or GitHub CLI) and copy the URL to your clipboard.
Open Git Bash.
Change the current working directory to where you want the cloned directory.
Type git clone and paste the URL from the clipboard 
Press Enter to create your local clone.
Running the Repository Locally
To run the project locally:

Go to the GitHub repository.
Locate the green “Code” button above the list of files and click it.
From the dropdown menu, select “Download Zip”.
Download and open the zip file to run in an editor.
Create an env.py file and input the environment variables.
Ensure PostgreSQL is installed on your computer and ports are open.
Create a virtual environment for installing the Python modules in the pip file.
Run python3 makemigrations, migrate and runserver.