### Book Collection Tracker

#### Overview
This project is part of Code Savanna’s internship evaluation. It is designed to assess your ability to build a basic full-stack application using Django (backend) and React (frontend).

The goal is to create a web application where users can manage a personal collection of books, including adding, viewing, updating, and deleting books. Additionally, users should be able to filter books based on certain criteria (e.g., genre or read status).

---

#### Project Requirements
- **Backend**: Django REST Framework to create APIs for managing books.
- **Frontend**: React for building a dynamic and interactive user interface.
- **Database**: SQLite (default with Django), but feel free to use PostgreSQL if you’re comfortable with it.
- **Styling**: Bootstrap 5 for responsive design and a professional layout.
- **Version Control**: GitHub for tracking progress and collaboration.

**Note**: Basic setup for both Django and React has been provided in this repository to get you started.

---

#### Learning Objectives
By the end of this project, you will demonstrate the following:
- Setting up and structuring a Django backend with API endpoints.
- Building a React frontend to interact with these endpoints.
- Managing data across a full-stack application.
- Writing clear, professional code following best practices.
- Applying Bootstrap for styling and responsiveness.

---

#### Getting Started

1. **Fork the Repository**  
   Fork this repository to your GitHub account, then clone it to your local machine:
   ```bash
   git clone https://github.com/your-username/book-collection-tracker.git
   ```

2. **Navigate to the Project Directory**  
   ```bash
   cd book-collection-tracker
   ```

#### Set Up the Backend (Django)

1. **Navigate to the backend directory**:  
   ```bash
   cd backend
   ```

2. **Create a virtual environment**:  
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. **Install required dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run initial migrations**:  
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**:  
   ```bash
   python manage.py runserver
   ```

#### Set Up the Frontend (React)

1. **Ensure Node.js and npm are installed**:  
   Before proceeding with the React setup, ensure you have [Node.js](https://nodejs.org/) and npm installed. If not, follow these instructions:

   - **For Windows and macOS**:
     1. Download the LTS version from the [Node.js download page](https://nodejs.org/).
     2. Run the installer and follow the instructions.
     3. Verify installation by running:
        ```bash
        node -v
        npm -v
        ```

   - **For Linux**:
     ```bash
     sudo apt update
     sudo apt install nodejs npm
     ```
     Verify the installation using the same commands as above.

2. **Navigate to the frontend directory**:  
   Open a new terminal window and run:
   ```bash
   cd frontend
   ```

3. **Install frontend dependencies**:  
   ```bash
   npm install
   ```

4. **Add Bootstrap to your React application**:  
   ```bash
   npm install bootstrap
   ```

5. **Import Bootstrap CSS in your index.js or App.js file**:  
   Add the following line:
   ```javascript
   import 'bootstrap/dist/css/bootstrap.min.css';
   ```

6. **Start the React development server**:  
   ```bash
   npm start
   ```

The frontend should now be available at `http://localhost:3000`, and the backend at `http://localhost:8000`.

---

#### Project Goals and Requirements

Below is a list of tasks to guide you through the project. Each task can be tackled one at a time and marked off as you complete it.

**Backend (Django)**
1. **Set up the Book Model and Migrations**  
   - Create a model `Book` with fields like title, author, genre, and read_status (boolean).
   - Make migrations and apply them.

2. **Create REST API Endpoints**  
   - Add API endpoints for:
     - Listing all books (GET)
     - Adding a new book (POST)
     - Updating a book (PUT)
     - Deleting a book (DELETE)
     - Include filtering functionality for genre and read_status.

3. **Implement API Documentation**  
   - Add documentation for each endpoint. Use a simple format like Django Rest Framework’s browsable API or Swagger.

**Frontend (React)**
1. **Design the UI for Book List and Filters**  
   - Utilize Bootstrap components to create a responsive layout.
   - Create a navigation bar using Bootstrap's Navbar component for easy navigation.
   - Build a list view of books using Bootstrap's Card component, displaying title, author, genre, and read_status.

   Example:
   ```javascript
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

   Example:
   ```javascript
   <button className="btn btn-danger" onClick={handleDelete}>Delete</button>
   ```

3. **Connect Frontend to Backend API**  
   - Use Axios to handle HTTP requests between the frontend and backend.
   - Test that all frontend interactions (CRUD operations) work as expected.

---

#### Submission Guidelines

**Code Quality**  
- Write clean, readable code following best practices. Use comments where necessary to explain complex logic or decisions.

**Git Workflow**  
- Commit frequently with clear, descriptive messages.
- Push your changes to your forked repository on GitHub.

**Pull Request**  
When you have completed all tasks, submit a pull request (PR) to the original repository with the following details:
- A summary of the features you implemented.
- Any challenges you encountered and how you overcame them.
- Areas for improvement or additional features you would add with more time.

---

#### Additional Notes
- **Testing**: While not required, we encourage you to write basic unit tests to verify the core functionality of your API endpoints.
- **Documentation**: Ensure your code is well-documented. You may also create a simple `API_Documentation.md` for additional clarity on endpoints.
- **Time Management**: This project is designed to be completed within a period of 10 days. Prioritize core functionalities before adding optional features or refinements.

---

#### Resources
Here are some resources to help you get started if you’re new to any of these technologies:
- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [React Documentation](https://reactjs.org/docs/getting-started.html)
- [Axios for Handling HTTP Requests](https://axios-http.com/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

---


### Important Notice: Use of AI Tools

**Attention Developers:**

As part of the Code Savanna internship evaluation, it is imperative to maintain the integrity and originality of your work. Therefore, the use of AI tools or automated coding solutions is strictly prohibited. Engaging with such tools not only undermines the purpose of this project but may also lead to disqualification from the evaluation process.

**Please note the following:**

- **Originality is Key**: Your submission should reflect your individual skills and understanding of the technologies involved. Use of AI-generated code or assistance will be considered a violation of the guidelines.
  
- **Detection**: There are mechanisms in place to identify the use of AI tools. Any detected usage will result in immediate penalties, including disqualification.

- **Professional Development**: This project is an opportunity for you to grow as a developer. Embrace the challenge, seek guidance when needed, and focus on honing your skills.


#### Contact
If you have any questions or encounter any issues, please reach out to your Code Savanna point of contact or open an issue in this repository.

Good luck, and we look forward to seeing your work!

--- 