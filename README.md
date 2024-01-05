# Blog Management

## Installation

Prerequisite: *Python version 3.6 or higher is required.*

1. Clone the repository:

   ```bash
   git clone https://github.com/rahult017/blog_api.git
   cd blog_api

2. Set up the virtual environment and install dependencies:

    To create virtual environment: python -m venv venv

    # For Unix/Linux
    source venv/bin/activate

    # For Windows
    .\venv\Scripts\activate

    pip install -r requirements.txt

3. Apply migrations and create a superuser account:
   
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser


4. Run the development server

    python manage.py runserver
   
5. Create Sample Data for project:

    python manage.py create_sample_data 10 # create 10 record in database 

   
6. Run test case :

    ```bash
    python manage.py test blog.tests.test_views
    python manage.py test blog.tests.test_serializers
    python manage.py test blog.tests.test_models
    
   
## API Documentation.

To understand how to utilize the API mentioned below, please refer to the tutorial video titled "how_to_test_api_in_postman.mp4" 

1.Blog Management

    ```bash
   1.Register a New User

    Endpoint: /api/register/
    Method: POST
    Description: Register a new user by providing the necessary information.
    Usage: Send a POST request with user registration data to create a new account.

    2.Obtain JWT Token for Authentication

    Endpoint: /api/login/
    Method: POST
    Description: Obtain a JSON Web Token (JWT) by providing valid credentials (username and password).
    Usage: Send a POST request with user credentials to get an authentication token.
    
    3.Retrieve a List of All Blog Posts

    Endpoint: /api/blogs/
    Method: GET
    Description: Retrieve a list of all blog posts.
    Usage: Send a GET request to fetch a list of blog posts.
    
    4.Retrieve Details of a Specific Blog Post

    Endpoint: /api/blogs/{id}/
    Method: GET
    Description: Retrieve detailed information about a specific blog post identified by its ID.
    Usage: Send a GET request with the blog post ID to fetch specific details.
    
    5.Create a New Blog Post

    Endpoint: /api/blogs/
    Method: POST
    Description: Create a new blog post by providing the necessary information.
    Usage: Send a POST request with the data for the new blog post.

    6.Update an Existing Blog Post

    Endpoint: /api/blogs/{id}/
    Method: PUT
    Description: Update an existing blog post identified by its ID.
    Usage: Send a PUT request with the updated data for the specified blog post.

    7.Delete a Blog Post

    Endpoint: /api/blogs/{id}/
    Method: DELETE
    Description: Delete a blog post identified by its ID.
    Usage: Send a DELETE request to remove the specified blog post

