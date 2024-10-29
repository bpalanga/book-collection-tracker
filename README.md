# Book Collection Tracker

## Overview
This project is part of Code Savanna’s internship evaluation. It is designed to assess your ability to build a basic full-stack application using **Django** (backend) and **React** (frontend).

The goal is to create a web application where users can manage a personal collection of books, including adding, viewing, updating, and deleting books. Additionally, users should be able to filter books based on certain criteria (e.g., genre or read status).

## Project Requirements
- **Backend**: Django REST Framework to create APIs for managing books.
- **Frontend**: React for building a dynamic and interactive user interface.
- **Database**: SQLite (default with Django), but feel free to use PostgreSQL if you’re comfortable with it.
- **Styling**: Bootstrap 5 for responsive design and a professional layout.
- **Version Control**: GitHub for tracking progress and collaboration.

> **Note:** Basic setup for both Django and React has been provided in this repository to get you started.

## Learning Objectives
By the end of this project, you will demonstrate the following:
- Setting up and structuring a Django backend with API endpoints.
- Building a React frontend to interact with these endpoints.
- Managing data across a full-stack application.
- Writing clear, professional code following best practices.
- Applying Bootstrap for styling and responsiveness.

---

## Getting Started

1. **Fork the Repository**  
   Fork this repository to your GitHub account, then clone it to your local machine:
   ```bash
   git clone https://github.com/your-username/book-collection-tracker.git
   ```
   
2. **Navigate to the Project Directory**
   ```bash
   cd book-collection-tracker
   ```

3. **Set Up the Backend (Django)**

   - Navigate to the `backend` directory:
     ```bash
     cd backend
     ```
   - Create a virtual environment:
     ```bash
     python3 -m venv env
     source env/bin/activate  # On Windows, use `env\Scripts\activate`
     ```
   - Install required dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Run initial migrations:
     ```bash
     python manage.py migrate
     ```
   - Start the development server:
     ```bash
     python manage.py runserver
     ```

4. **Set Up the Frontend (React)**
   - In a new terminal window, navigate to the `frontend` directory:
     ```bash
     cd ../frontend
     ```
   - Install frontend dependencies:
     ```bash
     npm install
     ```
   - Add Bootstrap to your React application:
     ```bash
     npm install bootstrap
     ```
   - Import Bootstrap CSS in your `index.js` or `App.js` file:
     ```javascript
     import 'bootstrap/dist/css/bootstrap.min.css';
     ```
   - Start the React development server:
     ```bash
     npm start
     ```

   The frontend should now be available at `http://localhost:3000`, and the backend at `http://localhost:8000`.

---

## Project Goals and Requirements

Below is a list of tasks to guide you through the project. Each task can be tackled one at a time and marked off as you complete it.

### Backend (Django)

1. **Set up the Book Model and Migrations**
   - Create a model `Book` with fields like `title`, `author`, `genre`, and `read_status` (boolean).
   - Make migrations and apply them.

2. **Create REST API Endpoints**
   - Add API endpoints for:
     - Listing all books (`GET`)
     - Adding a new book (`POST`)
     - Updating a book (`PUT`)
     - Deleting a book (`DELETE`)
   - Include filtering functionality for `genre` and `read_status`.

3. **Implement API Documentation**
   - Add documentation for each endpoint. Use a simple format like Django Rest Framework’s browsable API or Swagger.

### Frontend (React)

1. **Design the UI for Book List and Filters**
   - Utilize Bootstrap components to create a responsive layout.
   - Create a navigation bar using Bootstrap's Navbar component for easy navigation.
   - Build a list view of books using Bootstrap's Card component, displaying `title`, `author`, `genre`, and `read_status`.

   **Example:**
   ```jsx
   <div className="card mb-3">
       <div className="card-body">
           <h5 className="card-title">{book.title}</h5>
           <h6 className="card-subtitle mb-2 text-muted">{book.author}</h6>
           <p className="card-text">Genre: {book.genre}</p>
           <p className="card-text">Read: {book.read_status ? "Yes" : "No"}</p>
       </div>
   </div>
   ```

2. **Implement Book Management Functionality**
   - Build forms for adding and editing books using Bootstrap's Form components.
   - Create delete functionality with a Bootstrap modal confirmation dialog.

   **Example:**
   ```jsx
   <button className="btn btn-danger" onClick={handleDelete}>Delete</button>
   ```

3. **Connect Frontend to Backend API**
   - Use Axios to handle HTTP requests between the frontend and backend.
   - Test that all frontend interactions (CRUD operations) work as expected.

---

## Submission Guidelines

1. **Code Quality**  
   Write clean, readable code following best practices. Use comments where necessary to explain complex logic or decisions.

2. **Git Workflow**  
   - Commit frequently with clear, descriptive messages.
   - Push your changes to your forked repository on GitHub.

3. **Pull Request**  
   When you have completed all tasks, submit a pull request (PR) to the original repository with the following details:
   - A summary of the features you implemented.
   - Any challenges you encountered and how you overcame them.
   - Areas for improvement or additional features you would add with more time.

---

## Additional Notes
- **Testing**: While not required, we encourage you to write basic unit tests to verify the core functionality of your API endpoints.
- **Documentation**: Ensure your code is well-documented. You may also create a simple `API_Documentation.md` for additional clarity on endpoints.
- **Time Management**: This project is designed to be completed within a period of 10 days. Prioritize core functionalities before adding optional features or refinements.

---

## Resources

Here are some resources to help you get started if you’re new to any of these technologies:

- [Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [React Documentation](https://reactjs.org/docs/getting-started.html)
- [Axios for Handling HTTP Requests](https://axios-http.com/docs/intro)
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

---

## Contact

If you have any questions or encounter any issues, please reach out to your Code Savanna point of contact or open an issue in this repository.

---

Good luck, and we look forward to seeing your work!

--- 