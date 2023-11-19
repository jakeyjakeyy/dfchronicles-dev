# Dwarf Fortress Chronicles

Generate stories from Dwarf Fortress legends data.

## Distinctiveness and Complexity

- **Unique Domain:** Unlike common domains in earlier projects such as e-commerce or social media, this project operates in the unique domain of game world history narration. It required a deep dive into the data of Dwarf Fortress, and its world history files. It posed many questions such as how to interpret this data into engaging narratives while staying within the constraints posed by dealing with large amounts of data.

- **Complex Data Processing:** The project involves processing large amounts of data into a more desirable and succinct format. It requires converting XML files into JSON, interpreting the data, and generating narratives using AI. This introduced more challenges compared to purely handling standard data types in other applications.

- **AI Integration:** The use of AI to generate narratives adds a layer of complexity, mostly relating to the quirks of working with a third-party API. It required knowledge and research into the OpenAI API and how to seamlessly integrate it into a web application.

- **Stack:** This application was built with React and Django, and put together with Docker. It does not use any third-party CSS libraries, to reduce the overhead as well as improve my skills and familiarity with styling a web app. Using React in the front end also allowed me to use Django REST API and simplejwt for token-based authentication, further enhancing my understanding of the Django framework and working with APIs.

## File Descriptions

This only includes declarations and descriptions for files that are not automatically generated by any framework used in the web application, or those that have been heavily modified.

- ### **chronicle_compiler**

  - **.env**

    _.env is not included in the submission_
    _This is where the OpenAI API key is placed. This can be added by following the instructions in the [Build](https://github.com/jakeyjakeyy/dfchronicles#1-build) section below_

  - **Dockerfile**

    Provides instructions to docker for creating and installing dependencies for the backend.

- ### **frontend**

  - ### **src/browser**

    Parent folder for the Browser app, a div that displays most information on the web application.

    - **browser.css & browser.js**

      Style and function of the main browser div to display apps inside.

    - **listitem.css & listitem.js**

      Reusable app to display various information on a card.

    - **rating.js**

      Simple app to handle user rating of a generation.

    - **viewgen.css & viewgen.js**

      App to display a generation's information including comments, ratings, and more.

    - **upload/upload.css and upload/uploadxmlform.js**

      Style and function of the upload form for users to upload their game files to the web application.

    - **userpage/userpage.css & userpage/userpage.js**

      Style and function for displaying a user's page and relevant information.

    - **userpage/card.css & userpage/card.js**

      Cards for the user page for selecting categories (favorites, comments, generations).

    - **world/world.css & world/world.js**

      Parent div element for displaying events from a world's event data that has been uploaded.

    - **world/category.js**

      Displays relevant categories for selecting a generation.

    - **world/object.js**

      Displays information about the state of data collection and generation when an event object has been selected.

    - **worlds/worlds.css & worlds/worlds.js**

      Displays user's worlds based on uploaded files.

  - ### **src/navbar**

    Parent folder for the navbar app.

    - **login.js & register.js**

      Handle login and registration of users

    - **loginform.css & loginform.js**

      Creates a popup overlay for user login and registration.

    - **navbar.css & navbar.js**

      Main element and functionality of the navbar app. This changes what is displayed in the Browser app.

  - ### **src/utils**

    Parent folder for utilities used in the processing of XMLs and making API requests.

    - **loadfromclient**

      Parent folder for processing the XMLs. Converts XML data into succinct JSON data ready to send to OpenAI API.

    - **generations.js**

      The main file for handling backend API requests relating to viewing generations and any other related action such as favoriting and commenting on a generation.

    - **getgen.js & getgen.test.js**

      Handling API calls to the backend server to create a new generation from user data. Testing file to ensure getgen.js works properly with varying responses from the API.

    - **getuser.js**

      Handles API calls to return relevant user data for the UserPage app. Returns a user's favorites, comments, and generations.

    - **refreshtoken.js & refreshtoken.test.js**

      Handles API calls to return a valid token to the user. Testing file to ensure refreshtoken.js is working as intended.

## Running the web app

### 1. **Build**

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

### 2. **Accessing the Site**

- **Frontend:** `localhost:3000`
- **Backend:** `localhost:8000`

### 3. **Creating your data**

- **Register:** Create an account via the link in the navigation bar.
- **XMLs:** You can download sample data to use [here].
- **Upload:** Upload the XMLs on the Upload page via the navigation bar.
- **Generation:** Select your preferred category and an intriguing event. The app will promptly respond with a unique story tailored to your selected event.

### Note:

- Ensure your `.env` file is configured with a valid OpenAI API key for generations to occur. Tiktoken is used to ensure only generations under a reasonable size will be sent to the API.
