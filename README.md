# Back To Front Blog

## Overview

Back To Front is a music blog aimed at fans of all genres/subgenres of electronic music. Admins can post reviews on new music releases, as well as DJ mixes to the site. Admins can add, edit & delete posts from the front end of the site allowing full CRUD functionality from the front end.

For normal users, they can preview the music being reviewed on each post through embedded links to Soundcloud/Youtube as well as read the review. Users can comment on each post to share their thoughts and interact with one another. Users can also save releases to their user account so if they like the release they can easily find it via the saved releases section.

Live link: https://backtofrontblog.herokuapp.com/

## User Stories

### Admin:

1. I want to be able to create an admin account and access its features
2. I want to be able to share posts based on music releases
3. I want to be able to leave posts as drafts so I can post when ready
4. I want to be able to share previews from the music releases on posts
5. I want to be able to add, edit & delete posts from the front end of the site
6. I want to be able to share DJ mixes to the site
7. I want to be able to be able to delete user comments if deemed necessary

### User:

1. I want to be able to read about new music releases
2. I want to be able to listen to music whilst on the site
3. I want to be able to sign up to the site to access features requiring an account
4. I want to be able to be able to comment on reviews/posts and share my thoughts/interact with other users
5. I want to be able to keep a record of music from the site which I like
6. I want to be able to intuitively navigate the site
7. I want to be able to search the site

## Design

### Colour Scheme

The main colour scheme for the website is based on white & black to keep things clean and simple. A very light blue/gray colour was then used to accentuate other features/elements such as hovering over links, or the background colour for blog post images.

<img src="readme-images/design/colourpalette.png" width=600>

There are also the colours used for the 'Mixes' images, however these are not intended to be part of the colour scheme rather they are unique to each mix posted on the site both already and for future posts.

### Fonts

I used google fonts for the site, the logo was done with 'Raleway' in bold & italic. The rest of the site used Hind Madurai. The combination of these fonts maintained the clean contemporary & simplistic look I wanted to achieve.

### Imagery

The imagery on the site is dependent on the music releases which are reviewed as the cover images for these are what is used for each individual post/review. The relevent credits for posts so far can be found in the credits section.

## Wireframes

The wireframes for the site were made from https://wireframe.cc/ and are attahced below:

- Desktop
    - [Homepage](readme-images/wireframe/desktop/homepage.png)
    - [Blog post](readme-images/wireframe/desktop/blogpost.png)
    - [Mix page](readme-images/wireframe/desktop/mixpage.png)

- Tablet
    - [Homepage](readme-images/wireframe/tablet/homepage.png)
    - [Blog post](readme-images/wireframe/tablet/blogpost.png)
    - [Mix page](readme-images/wireframe/tablet/mixpage.png)

- Mobile
    - [Homepage](readme-images/wireframe/mobile/homepage.png)
    - [Blog post](readme-images/wireframe/mobile/blogpost.png)
    - [Mix page](readme-images/wireframe/mobile/mixpage.png)

## Features

### Navigation Bar

- Displays the logo, which can be clicked to get back to the home page.
- Displays naivgation links depending on users authentication status & admin status:

<img src="readme-images/features/nav/loggedoutnav.png" width=1000>
<img src="readme-images/features/nav/usernav.png" width=1000>
<img src="readme-images/features/nav/adminnav.png" width=1000>

- Displays the search icon which can toggle the search bar opening/closing:

<img src="readme-images/features/nav/searchnav.png" width=1000>

- Navigation links are hidden on smaller screens and toggled for opening & closing with a burger menu icon:

<img src="readme-images/features/nav/burgernav.png" width=600>

### Footer

- Displays the site logo and provides links to social accounts. The remains consistant throughout the whole site and on all screen sizes:

<img src="readme-images/features/footer.png" width=1000>

### Featured Post

- Randomly displays one of the six most recent blog posts on the home page and allows users to access the post via clicking like usual:

<img src="readme-images/features/featuredpost.png" width=600>

### Blog

- The blog section on the home screen displays the 6 most recent posts, allowing users to view and open the newest content:

<img src="readme-images/features/blog/bloghome.png" width=600>

- Users can click on 'Blog' on the home screen to be taken to the blog section of site where all blog posts will be displayed:

<img src="readme-images/features/blog/blog.png" width=600>

- Users can also utilse the search bar which will take them to the search results page and display any relevant posts that match their search:

<img src="readme-images/features/blog/blogsearch.png" width=600>

- Admins can add posts via the link in the nav bar once they are signed in, and can also access the edit & delete post functions whilst on the posts themselves:

    - Add post:
    <img src="readme-images/features/blog/addpost.png" width=600>

    - Edit post:
    <img src="readme-images/features/blog/editpost.png" width=600>

### Blog Posts

- Blog posts display the content to the users, with the title, cover image, author & date posted, review/write up and the music preview:

<img src="readme-images/features/blog/blogpost1.png" width=600>

<img src="readme-images/features/blog/blogpost2.png" width=600>

- The comment section allows all users & admins on the site to comment their thoughts/opinions on the music and interact with one another. The delete button allows users to delete their own comment, or so can an admin if they think necessary:

<img src="readme-images/features/blog/blogcomments.png" width=600>

- For signed in admins the following buttons are displayed at the bottoms of posts allowing them to access each ones relevant functionality:

<img src="readme-images/features/blog/adminblogbtns.png" width=600>

- For users the only button displayed will be to add or remove the release to their user account - unauthetnicated users will be redirected to the sign up page if they try to click it

<img src="readme-images/features/user/saverelease.png" width=300> <img src="readme-images/features/user/removerelease.png" width=300>

### User Profile

- The user profile displays any saved releases to the user for their own reference. They can click on the release to be taken to the post, or they can also remove it from their profile:

<img src="readme-images/features/user/userprofile.png" width=600>


### Mixes

- The Mix section on the home screen displays the 4 most recent mixes, allowing users to view and open the newest ones added:

<img src="readme-images/features/mixes/mixeshome.png" width=600>

- Users can click on 'Mixes' on the home screen to be taken to the mixes section of site where all mixes will be displayed:

<img src="readme-images/features/mixes/mixes.png" width=600>

- Mix pages display the image for the mix, any write up and the mix itself to the user:

<img src="readme-images/features/mixes/mixepage1.png" width=600>
<img src="readme-images/features/mixes/mixepage2.png" width=600>