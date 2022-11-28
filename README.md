# Sentry Log

This is a web application which can be accessed through a browser and is intended to be used by those providing access control security services. This application allows a security service provider to do away with paper, pens and clipboards traditionally used to log deliveries to a premises and instead use a mobile device to capture all details electronically.
This application as many advantages over the traditional paper, pen and clipboard. This application eliminates the challenge of poor legibility of handwritten records, vastly improves the time taken to retrieve records, no longer having to rummage through paper records. A security service provider no longer has to store and safeguard large quantities of paper records. Also, paper records are cumbersome when being used for the purposes of roll calls in the event of an emergency.  All of the challenges can be overcome with Sentry Log. 

The web application can be accessed here - https://sentry-log.herokuapp.com/

![Sentry Log Mock Up]( /media/access_form.JPG)

## Existing Features:
Landng Page:
Here the user is met with a brief description of the application's purpose and aims to grab the user's attention with 4 core aspects of the app with 'Record Retrieve Monitor Protect'. The user is then invited to sign up to, "access this powerful application". A large image of a security officer makes it apparent to the user who this application is aimed at. 

![Landing Page]( /media/landing_page.JPG)

## Sign Up:

Users can sign up by clicking on the 'Sign Up' link at the top of the landing page. Log in/ Log out is confirmed with a message displayed after each action.


## Log in/ Out:
Once signed up, the user can then log in. Feed back is provided to the user informing them they have successfully signed in and returning them to the landing page from which they can now use previously hidden navigation links.
![Sign In Page]( /media/sign_in_page.JPG)

Logging out brings the user back to the home page with a message confirming the user has logged out.
![Sign Out Page]( /media/sign_out.JPG) 

## Navigation Bar:
The navigation bar consists of a 'Home', ' Sign Up' and 'Login' link prior to logging in. However, once logged in, the user now has access to 4 more links, 'Access form', 'Access Log', 'Roll Call', and "Search Page'.
For medium screens and smaller, the navigation bar changes to a mobile-friendly drop down menu containing all of the links.
![Navigation Bar]( /media/navigation_links.JPG)

## Footer:
The footer is a simple copyright message against a black background.
![Footer]( /media/footer.JPG)


## Access Form:

Allows the user to record all required details of deliveries, such as name, phone number, time in/ out , point of entry and destination, etc.
Data validation preventing access forms from being submitted without all required information.

![Access Form]( /media/access_form.JPG)

The access form can be expanded to add in details of any passengers.

![Expanded Form]( /media/expanded_form.JPG)


## E-Signature:
Capture signatures electronically. Visitors can sign an NDA or site rules upon entry. Signature data is converted to JPEG, which is then converted to and stored as a string. The user must confirm their signature before the form can be submitted.

![Signature]( /media/signature_pad.JPG)

## Access Log:
A core component of the application is the Access Log. Here, the security service provider can see all of the deliveries that have accessed the premises, what time they entered and exited, etc. The Access Log will highlight any deliveries that have overstayed the parkign time limit allocated by the security officer assisting the officer in monitoring compliance.

![Access Log]( /media/access_log.JPG)

## 'More' button:
In order to prevent information overload or a cluttered presentation, only key information is initially displayed to the user. Extra information can be displayed to the user by pressing the 'more' button, which will open a hidden element and provide more detail on the delivery driver, such as a phone number, the name of the officer who granted entry, and a copy of the driver's signature, for example. Clicking the more button also reveals an edit and delete button, which, of course, allows the user to edit or delete the selected record, however, these buttons are only visible to those with 'staff' or 'superuser' access. This restriction allows administrators to safeguard records by preventing deletion or tampering with valuable data.

![More button]( /media/more.JPG)

## 'Check Out' button:
Security service providers can process a large number of deliveries each day, and often, must do so quickly, every click counts. The check out brings the user to a page asking for confirmation that the user wants to check out a delivery. The officer can then confirm, and the web application will automatically fill in the time and date the delivery left the site. Two clicks are all it takes. No maunal input of date or time required.

![Checkout button]( /media/checkout.JPG)


## Roll Call:
The roll call page allows the user to see all of the deliveries currently still on the premises and is intended to be used in the event of an emergency. The information displayed on this page is stripped down to the bare essentials so that the user can quickly see the name, company, and contact phone number of each driver on site. Though more detailed information can still be accessed via the 'more' button. The Roll Call page will display only records that do not currently have a 'time out' value.

![Roll Call]( /media/roll_call.JPG)


## Search Page:
As mentioned previously, paper records can be difficult to locate, sift through, and read. The search page allows for the quick retrieval of records and eliminates challenges around legibility and storage of files. Currently, the search functionality consists of searching by first name, last name, and company,  though it will also include searching by time and date range. The search terms must be exact and are case-insensitive.

![Search Page]( /media/search_results.JPG)


## Features Left To Implement:
* Search by time and date range
* Audio notification for deliveries that have overstayed
* Display Access Log data on a chart for analysis.
* Excel export for Access Log data
* Shift handover functionality
* Operating Procedures page
* Head count dsiplayed on Roll Call page

## Testing:
* All links were tested.
* All pages were viewed on all screen sizes.
* Edit/ Delete buttons tested on Access Log, Roll Call and Search Page.
* Check out button tested on Access Log, Roll Call and Search Page.
* Checked messages are displayed to user after each log in, log out, edit, delete, search or use of check out button.
* Check links bring user to the correct page.
* Checked that confirm or cancel buttons redirect user to the correct page.
* Checked that the signature pad can be written on.
* Checked that forms actually save data and signatures.
* Checked that data updates correclty when edited.
* Checked that data from database is rendered correctly.
* Checked that vehicle logs change color correctly when a delivery overstays. 
* Checked that form data validation works correctly by attempting to pass strings into integer fields.
* Checked that only 'staff' or 'superusers' can access the delete and edit buttons.
* Checked that only log in and sign up pages can be accessed when the user is not logged in.
* Checked that search feature returns results correctly when matching names are entered into the search fields.

## Wireframes:
Below are the wireframes used to conceptualise Sentry Log. I chose to dsiplay the apps data in a list or table like format with key inforation available at a glance, with teh option to access more detail by expaning an element to reveal more innformation if required. This helps to keep the overall layout of information clear and not cluttered.
![Wire Frame 1]( /media/wireframe_1.JPG)
![Wire Frame 2]( /media/wireframe_2.JPG)

## Database Schema:
Below is the schema for the database used in Sentry log. Given that I wanted to ensure records were retained even if a user was deleted, I chose not to use on delete cascade. 
![Database schema]( /media/schema.JPG)

## Epics & User Stories:
The goal in develpoing Sentry Log was to create an app that allows the user to be fully aware of who is on their premisis, when they were on their premises, where they went while they were on their premisis and be able to contact them quckly in the event of an emergency and also be notified if they stayed too long. The following user stories were used to break down this epic:
* As a security officer, I can edit entry/ exit times/ so that I can correct errors.
* As a security officer, I can allocate an amount of time the delivery is permitted to be on site so I can receive a notification if a delivery has exceeded their permitted time on site.
* As a user, I can view records of deliveries so that I can see all delivery records.
* As a security officer, I can filter records by key word so I can quickly see when someone visited site, what company they work for etc.
* As a security officer, I can filter a report to see all deliveries currently on site so all personnel can be accounted for in emergencies.
* As a security officer, I can record a deliveries details electronically (name, company, reg., destination etc) so that I don't have to store and file paper logs.
* As as delivery driver, I can provide a signature so that I can confirm that i have read the site rules to gain entry.
* As a manager, I can delete records so that I can comply with companies data retention periods.
* As a security officer, I can use a toggle button to mark a delivery as "exited/ offsite" so that I can auto fill exit time.

![User Stories]( /media/user_stories.JPG)


## Solved Bugs:
1. I couldn't update my database because 'no changes were detected'. I fixed it by running python3 manage.py flush followed by python3 manage.py migrate MyApp zero.
2. Messages were displaying twice when I logged in/out. I had placed code for message in the index template, which was extended to all other templates. So when code for messages was included in individual templates, the result was two messages displayed. Removing the code for messages from the index template resolved the issue.
3. I changed how the time for parkign time limit was displayed so that hours and inutes were dispalyed with seconds. Though I had some JS code that calculated how many seconds were left until expiry. This changed how the expiration time was calculated, causing all of the recorded deliveries to be flagged as "overstayed. Changing the format back to hours, minutes and seconds resolved this iusse. 


## Remaining Bugs:
* Deliveries will not show as overdue if the expiration time has passed by 24 hours, this is because the time code is not linked to a date value.
The signature pad accepts a blank signature, so I need to code to prevent the signature input from accepting the todata value that is equal to a blank canvas. 

## Validator Testing:
* Code for all pages was passed through the W3 Markup validator with no errors detected.
* Javascript code was passed through the JShint validator. While several warnings were detected, the javascript code works fine.
* PEP8 validator was used within the gitpod workspaces and found no Python problems.

## Deployement:
I deployed the Sentry log app by doing the following:
1. Create Heroku App.
2. Attached the database.
3. Prepared environment adn settings.py files.

Then I set up static and media files that are stored on Cloudinary:
1. Go to heroku
2. got to config vars and add a key 'DISABLE_COLLECTSTATIC' and input a value of 1.
3. sign up to cloudinary
4. copy cloudinary API environment variable.
5. In envy.py file add os.environ["CLOUDINARY_URL"] = "past cloudinary API environment variable here". Ensure you delete 'CLOUDINARY_URL='.
6. Go to heroku dashboard > config vars  add a new key 'CLOUDINARY_URL' with the value same as the cloudinary API environment variable.
7. Add new key DISABLE_COLLECTSTATIC and add a value of 1.
8. Go to settings.py > INSTALLED_APPS and add'cloudinary'.
9. go to end of settings page and add ' STATICFILES_STORAGE = 'cloudinary_storage.StaticHashedCloudinaryStorage'
10. STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
11. On the line below ass 'os.path.join(BASE_DIR, 'staticfiles')
12. Add on rthe line below MEDIA_URL = '/media/'
13. On teh line below add, DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
14. Under BASEDIR add TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
15. Go to templates and add [TEMPLATES_DIR] as the valuef or 'DIRS'
16. Go to ALLOWED_HOSTS and add 'sentry-log.herokuapp.com', 'localhost' into the square brakets.
17. create 3 folders in the top directory, static, media and templates.
18. Create profile.
19. Inside procfile type 'web: gunicorn codestar.wsgi'
20. Save, add , commit (deployement commit) and push files to github.
21. Go to heroku dash board > deploy and click github for deployment method.
22. Search for repo.
23. Click connect beside your app.
24. Click 'deploy branch'.
25. When aHeroku states that app has been deployed successfully, click on 'open app' to view the app.
26. Set DEBUG to False.
27. Type "'X_FRAME_OPTIONS = 'SAMEORIGIN'"
28. Save, add , commit and push to repo.
29. Go to Herok > config vars and delete DISABLE_COLLECTSTATIC.
30. Click 'Deploy'
31. Scroll to end of page and click, 'deploy branch'.
32. Click Open app.

## Credits:

* DivByDiv for code used to develope a signature pad. His tutorial can be found here https://www.youtube.com/watch?v=U0qJG5DZ5_U.
* Greyscale template from Startbootstrap which can be found here https://startbootstrap.com/theme/grayscale
* My mentor Gurjot Singh for the great guidance.
* W3Schools.com for quick refreshers.
* Code for paginating was from Fahadul Shadhin and can be found at https://python.plainenglish.io/how-to-implement-pagination-in-django-with-function-based-views-8f6462554930.
* stackoverflow for code for perfoming filtering for database searches.
* Code intitute for providing the knowledge to allow me to code and keeping me on track regarding deadlines.
