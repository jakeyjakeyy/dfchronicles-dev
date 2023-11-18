# Dwarf Fortress Chronicles

Generate stories from Dwarf Fortress legends data.

## Distinctiveness and Complexity

The Dwarf Fortress Chronicle Generator is a unique and complex project that stands apart from earlier projects such as our e-commerce and social media web applications.

- **Unique Domain:** Unlike common domains such as e-commerce or social media, this project operates in the niche domain of game world history narration. It required a deep dive into the data of Dwarf Fortress, and its world history files. It posed many questions such as how to interpret this data into engaging narratives.

- **Complex Data Processing:** The project involves complex data processing tasks. It requires converting XML files into JSON, interpreting the data, and generating narratives using AI. This is a more complex task than handling standard data types in other applications.

- **AI Integration:** The use of AI to generate narratives adds a layer of complexity. It requires knowledge of AI, communication with a third-party API, and how to integrate it into a web application.

- **Advanced Search Functionality:** The search and filter functionality goes beyond standard search features in e-commerce or social media apps. It allows users to search for specific stories or historical events, requiring a more complex search algorithm.

- **User Feedback and Ratings:** Implementing a system for user feedback and ratings adds another layer of complexity. It requires creating a system for users to rate and review generated stories, and a way to handle and store this data.

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

- **AI:** By default there will not be any communication with OpenAI API, and the server will return a preset response.

If you would like a real generation from the OpenAI API, follow these steps:

- Create a `.env` file in `dfchronicles/backend` if it doesn't exist.
- Add the following line to the `.env` file: `OPENAI_API_KEY=your_openAI_API_key`.

### 2. **Accessing the Site**

- **Frontend:** `localhost:3000`
- **Backend:** `localhost:8000`

### 3. **Creating your data**

- **Register:** Create an account via the link in the nav bar.
- **XMLs:** You can download sample data to use [here].
- **Upload:** Upload the XMLs on the Upload page via the nav bar.
- **Generation:** Select your preferred category, and any event that piques your interest. The app will shortly respond with a unique story specific to your selected event.
