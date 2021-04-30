# FIRSTHAND BOUTIQUE

* This is a project built using, technologies such as  HTML, CSS, Bootstrap framework,Python and Django. A relational database such as MYSQL with STRIPE Gateway payments.

This app contains a header. The header is sub divided into 3 section, a **Logo**, a **Search bar** and an **Account & Shopping Basket**
* The **logo** is the name of the website
* the **search** bar allows users to search for products 
* The **account** allow users to create accounts to save their information and log in and out and reset their password just incase they have forgotten their password. Logged in Users would also have access to personalized user profile where they would be able to store their default payment information and view their other history as well as past order confirmation.
* The **Shopping basket**, displays the users total amount.

 It also has a **Navigation Menu** that contains a Navigatation Menu such as HOME, ALL PRODUCTS, VEHICLES, ELECTRONICS, HOUSEHOLD, BIKES, CLOTHING, OTHERS.
 * **Home**, The home button redirects the user back to the home page. The **Home page** contains **Shop now** button when clicked displays all the products and images displaying the different collections explicitly.
 * **All Products**, Contains all the products listed,
 * **Vehicles**, contains the all the vechiles.
 * **Households**, is subdivided into Kitchen, Carpets, Chairs, Tables, Beds, Fridges, Microwaves, Cupboards.
 * **Electronics**,  is subdivided into Television, Radio, Phones, Labtops.
 * **Bikes**, is subdivided into Motorbikes and Bicycles.
 * **Clothings**, displays all the different outfits.
 * **Others**, displays other items with no category. 

 # UX
 * The site is meant for users who want to view a list of products to purchase
* clicking on the individual products will display in details the **price** of the products, **description** of the products, a **slug** which when clicked displays products of thesame category  and a **quantity selector** to choose how many products the user wants to purchase. A **keep shopping** button and an **add to bag** button.
 * The **keep shopping** button redirects the user to back to the products page to continue shopping while
 * As a user when i click the **add to bag** button it displays a popup with a message indicating that the item was successfully added to the user's bag. It also contains a quanity, and price total. There is also a **go to secure checkout** button which when clicked by the user, redirects the user to the **shopping bag** page.
 * As a user i can view items in the shopping bag page.
 * I can adjust the quantity of individual items in my bag, so that i can easily make changes to my purchase before checkout.
 * As a user i can delete items from my shopping bag if i changed my mind about an item 
 * As a user i can see the grand total price in my bag, so that i can click on the **keep shopping button** to continue shopping or click on the **secure checkout** button to take me to the **checkout page**
 * As a user i want to feel my personal and payment information is safe and secure so as to confidentially provide the needed information to make a purchase
 * As a user i can view the confrimation after checkout with a popup message displaying order successfully processes or order failed to process for further clearification if the process was successful or unsuccessful. 

# put the images here
# FEATURES
* responsive on all device sizes
* Interactive elements

# Technologies Used
## Languages Used
* HTML5
* CSS3
* JAVASCRIPT
* PYTHON
# Frameworks, Libraries & Programs Used 
[Django](https://www.djangoproject.com/):

* Django is a Full framework which comes with prebuild authentication functionality and has built in tools used to create this project.

[Bootstrap 4](https://getbootstrap.com/):
* Boostrap was used to assist with the responsiveness and styling of the website.

[Google Fonts](https://fonts.google.com/):

* The google fonts were used to import Lato font to add into the corecss block in the base.html, which is used on all pages throughout the site.

[Font Awesone](https://fontawesome.com/):
* Font Awesome was used on all pages throughout the website to add icons for UX purposes.

[jQuery](https://jquery.com/):

* jQuery comes with bootstrap with the full version. The minified version contains AJax function like POST.

[Gitpod](https://www.gitpod.io/):

* Gitpod was the workspace used for version control by utilizing the Gitpod terminal to commit and push to Github.

[GitHub](https://github.com/):

* GitHub is used to store the projects after been pushed from gitpod

[Pixabay](https://pixabay.com/images/search/e-commerce/):

* Pixabay is where i got the home image and some product images for the website.

[Photoshop](https://www.adobe.com/):
* Photoshop was used for photo resizing and editing pictures for website.


[Balsamiq](https://balsamiq.com/):

* Balsamiq is used to create the wireframes during the design process.

[AWS](https://aws.amazon.com/):

* AWS is a cloud based service that host the deployed site

# Testing
As a first time user, i want to easily the functionalities of the site.
* Upon entering the site, a user may want to authenticate themselelves by signin in if they already have an account or create an account if they haven't created an account.
* The shopping basket displays the grand totol price of the products selected by the user.
*  The navigation menu contains the menu items which redirects the user to a category of items selected.
* The shop now button is place on the home image for user to view all products to the user.
* The collection section has images of the different category collection links, which when cliced by the user will redirect the user to the collection page.

As a user i want to seclect an item
* A user can select any item by clicking on the item, it opens up to a detail page 
* The detail page contains the name of the item, the slug(a cart with displaying items of the same category when clicked).
* It also contains price, description, quantity selector for the user to add/remove the quantity of the items purchased.
* It has an keep shopping button which redirects the user back to the products page or an add to bag button which when clicked, will display message indicating that the theitem has been added to the users bag.
* The popup also contains a go to secure checkout button which will redirect the user to the shopping bag.

As a user want to see items in my shopping bag
* The user see the item in the shopping bag, the name of the item, can either **update** or **delete** items from the shopping bag
* the usefr can see the subtotal of individual items and the total price of all the items. 
* The user can either continue shopping by clicking on the button or click on the secure checkout button to be redirected to the checkout page.

As a user i want top fill in my personal and payment information to be able to make a purchase.
* As a user in the checkout page fileds, i can fill in my personal and payment informations into the fields to make a payment to the items and i can also see my order detail information.
* As a user i can click on the complete order button to complete the order payment or click on the back to cart button which will take me back to the shopping bag page if i changed my mind to add more products or delete more products from the shopping bag.

As a user i want to be sure the payment was successful
* As a user you will see a popup message indicating that the payment was succesful or wasn't successful.
* As a user, after filling the right imformation, you will be redirected to the success page, that shows the process was successful with a continue button if the user wishes to continue shopping.

## Further Testing
* The website has been tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
* The website was viewd on a variety of devices such as Desktop, Galaxy S5, Iphone 8, Ipad, and Ipad Pro.
* More testing was carried out to ensure that all pages were linking correctly.

# Known Bugs
It was difficult implimenting the 

# Deployment
