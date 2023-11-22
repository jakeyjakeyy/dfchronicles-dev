# Dwarf Fortress Chronicles

Generate stories from Dwarf Fortress legends data with GPT-4.

- [Distinctiveness and Complexity](#distinctiveness-and-complexity)

- [File System Architecture](#file-system-architecture)

  - [Chronicle Compiler](#chronicle-compiler)

  - [Frontend](#frontend)

    -[Browser](#browser)

    - [Navbar](#navbar)

    - [Utils](#utils)

- [Running the web app](#running-the-web-app)

  -[Build](#1-build)

  -[Accessing the site](#2-accessing-the-site)

  -[Creating your data](#3-creating-your-data)

  -[Note](#note)

# Distinctiveness and Complexity

- **Unique Domain:** Unlike common domains in earlier projects such as e-commerce or social media, this project operates in the unique domain of game world history narration. It required a deep dive into the data of Dwarf Fortress, and its world history files. It posed many questions such as how to interpret this data into engaging narratives while staying within the constraints posed by dealing with large amounts of data.

- **Complex Data Processing:** The project involves processing large amounts of data into a more desirable and succinct format. It requires converting XML files into JSON, interpreting the data, and generating narratives using AI. This introduced more challenges compared to purely handling standard data types in other applications.

- **AI Integration:** The use of AI to generate narratives adds a layer of complexity, mostly relating to the quirks of working with a third-party API. It required knowledge and research into the OpenAI API and how to seamlessly integrate it into a web application.

- **Stack:** This application was built with React and Django, and put together with Docker. It does not use any third-party CSS libraries, to reduce the overhead as well as improve my skills and familiarity with styling a web app. Using React in the front end also allowed me to use Django REST API and simplejwt for token-based authentication, further enhancing my understanding of the Django framework and working with APIs.

# File System Architecture

- **docker-compose.yml**

  - Instructions for docker to build the database, frontend, and backend images.

- **README.md**

  - This file!

## Chronicle Compiler

- **.env**

  - _Not included in the submission._
  - Contains the OpenAI API key. Follow the instructions in the [Build](#1-build) section for adding, else a default generation will be returned from the backend.

- **Dockerfile**

  - Provides instructions for Docker to create and install backend dependencies.

- **chronicle_compiler/models.py**

  - Defines database models for Generations, Ratings, Comments, and Favorites.

- **chronicle_compiler/views.py**
  - API functions for retrieving database information and forwarding user event data to the OpenAI API for generations.

## Frontend

- **Dockerfile**

  - Docker instructions for building the frontend image.

- **src/App.css & src/App.js**

  - Initialization of Navbar, Browser, and application-wide functions and variables.

- **src/index.css & src/root.css**
  - Defines fonts and colors used throughout the application.

### Browser

- **browser.css & browser.js**

  - Style and function of the main browser div for displaying apps.

- **listitem.css & listitem.js**

  - Reusable app to display various information on a card.

- **rating.js**

  - Simple app for handling user rating of a generation.

- **viewgen.css & viewgen.js**

  - App for displaying a generation's information, including comments and ratings.

- **upload/upload.css & upload/uploadxmlform.js**

  - Style and function of the upload form for users to upload game files.

- **userpage/userpage.css & userpage/userpage.js**

  - Style and function for displaying a user's page and relevant information.

- **userpage/card.css & userpage/card.js**

  - Cards for the user page for selecting categories (favorites, comments, generations).

- **world/world.css & world/world.js**

  - Parent div element for displaying events from a world's event data.

- **world/category.js**

  - Displays relevant categories for selecting a generation.

- **world/object.js**

  - Displays information about the state of data collection and generation when an event object is selected.

- **worlds/worlds.css & worlds/worlds.js**
  - Displays user's worlds based on uploaded files.

### Navbar

- **login.js & register.js**

  - Handles login and registration of users.

- **loginform.css & loginform.js**

  - Creates a popup overlay for user login and registration.

- **navbar.css & navbar.js**
  - Main element and functionality of the navbar app, changing what is displayed in the Browser app.

### Utils

- **loadfromclient**

  - Parent folder for processing XMLs, converting XML data into JSON ready for OpenAI API.

- **generations.js**

  - Main file for handling backend API requests related to viewing generations and related actions.

- **getgen.js & getgen.test.js**

  - Handles API calls to create a new generation from user data. Testing file ensures proper functionality with varying API responses.

- **getuser.js**

  - Handles API calls to return relevant user data for the UserPage app.

- **refreshtoken.js & refreshtoken.test.js**
  - Handles API calls to return a valid token to the user. Testing file ensures intended functionality.

# Running the web app

## 1. **Build**

- **Docker:** In the main directory, run the following commands in your terminal.

  ```
  docker-compose build
  docker-compose up
  ```

- **Migrations:** Enter the backend docker image, and run the following commands in your terminal

  ```
  python manage.py makemigrations
  python manage.py migrate
  ```

- **AI:** By default, there will not be any communication with the OpenAI API, and the server will return a preset response.

  If you would like a real generation from the OpenAI API, follow these steps:

  - Create a `.env` file in `dfchronicles/backend` if it doesn't exist.
  - Add the following line to the `.env` file: `OPENAI_API_KEY=your_openAI_API_key`.

## 2. **Accessing the Site**

- **Frontend:** `localhost:3000`
- **Backend:** `localhost:8000`

## 3. **Creating your data**

- **Register:** Create an account via the link in the navigation bar.
- **XMLs:** You can download sample data to use [here](https://drive.google.com/drive/folders/1bzT_DZWI8GDgA5xlQpjv_wxicT6q2BaD?usp=sharing).
- **Upload:** Upload the XMLs on the Upload page via the navigation bar.
- **Generation:** Select your preferred category and an intriguing event. The app will promptly respond with a unique story tailored to your selected event.

## Note:

- Ensure your `.env` file is configured with a valid OpenAI API key for generations to occur. Tiktoken is used to ensure only generations under a reasonable size will be sent to the API.
