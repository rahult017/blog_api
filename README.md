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
   
3. Create Sample Data for project:

   
$. Run test case :
    
   
## API Documentation.

To understand how to utilize the API mentioned below, please refer to the tutorial video titled "how_to_test_api_in_postman.mp4" 

1.Blog Management

    - /api/register/ (POST): Register a new user.
    - /api/login/ (POST): Obtain a JWT token for authentication.
    - /api/blogs/ (GET): Retrieve a list of all blog posts.
    - /api/blogs/{id}/ (GET): Retrieve details of a specific blog post.
    - /api/blogs/ (POST): Create a new blog post.
    - /api/blogs/{id}/ (PUT): Update an existing blog post.
    - /api/blogs/{id}/ (DELETE): Delete a blog post.

