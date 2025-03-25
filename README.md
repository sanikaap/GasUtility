# Gas Utility Customer Service Portal

A comprehensive Django-based application designed to streamline gas utility service request management between customers and service staff.

![Gas Utility Service Portal](https://example.com/gas-utility-screenshot.png)

## 🌟 Features

### Customer Features
- **Account Dashboard**: View customer details and service history.
- **Service Request Management**: Create, track, and cancel service requests.
- **Request Timeline**: View detailed history of service request status updates.
- **File Attachments**: Upload supporting documents and images with service requests.

### Staff Features
- **Request Management**: View, assign, and update the status of all customer service requests.
- **Status Updates**: Communicate progress through status changes and comments.
- **Customer Management**: Access customer information and service history.

### Security Features
- **Authentication System**: Secure login and user session management.
- **Role-Based Access**: Different capabilities for customers and staff.
- **Permission Controls**: Customers can only view and manage their own requests.

## 🛠️ Technical Stack
- **Backend**: Django (Python web framework)
- **Database**: SQLite (development) / PostgreSQL (production)
- **Frontend**: Bootstrap 5 for responsive design
- **Forms**: `django-crispy-forms` for improved form rendering
- **File Storage**: Django's file storage system for attachments

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- Git

### Setup Steps

1. **Clone the repository**
   ```sh
   git clone https://github.com/your-repo/gas-utility-portal.git
   cd gas-utility-portal
   ```

2. **Create and activate a virtual environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Create environment variables file**
   Create a `.env` file in the project root with the necessary configurations.

5. **Run database migrations**
   ```sh
   python manage.py migrate
   ```

6. **Create an admin superuser**
   ```sh
   python manage.py createsuperuser
   ```

7. **Create service request types**
   - Log in to the Django admin panel.
   - Navigate to "Service Request Types".
   - Add common request types (e.g., "Gas Leak", "Billing Issue", "New Connection").

8. **Run the development server**
   ```sh
   python manage.py runserver
   ```

9. **Access the application**
   - Web application: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Admin interface: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## 📝 Usage Guide

### Customer Flow
1. **Register/Login**: Create an account or sign in with existing credentials.
2. **Dashboard**: View account information and service request history.
3. **Create Request**: Submit a new service request with description and optional attachments.
4. **Track Progress**: Monitor service request status and view updates from staff.
5. **Cancel Request**: Cancel a request if it's no longer needed.

### Staff Flow
1. **Login**: Sign in with staff credentials.
2. **View Requests**: See all customer service requests.
3. **Update Status**: Change request status and add comments/timeline events.
4. **Resolve Issues**: Mark service requests as resolved when complete.

---

