# Citizen Feedback Survey System

## Overview

This application is a web-based survey system designed to collect structured feedback from users on public infrastructure, environment, safety, and community-related aspects. The system captures user responses through a form-based interface and stores the data in a cloud database for further use.

---

## Project Structure

```
project/
│── app.py
│── requirements.txt
│── README.md
│── .streamlit/
    └── secrets.toml
```

---

## Prerequisites

* Python 3.10 or 3.11 installed
* Git installed
* MongoDB Atlas account
* GitHub account

---

## Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## MongoDB Setup

1. Create a cluster in MongoDB Atlas
2. Create a database user with username and password
3. Whitelist network access:

```
0.0.0.0/0
```

4. Copy the connection string

---

## Configuration

Create a folder named `.streamlit` in the root directory.

Inside it, create a file `secrets.toml` and add:

```
MONGO_URI = "your_mongodb_connection_string"
```

---

## Running the Application

```
streamlit run app.py
```

The application will be available locally at:

```
http://localhost:8501
```

---

## Deployment (Streamlit Community Cloud)

1. Push your project to GitHub
2. Go to Streamlit Community Cloud
3. Click on "New App"
4. Select your repository and branch
5. Set the main file path as:

```
app.py
```

6. Open app settings and add Secrets:

```
MONGO_URI = "your_mongodb_connection_string"
```

7. Deploy the application

---

## Data Storage

* Data is stored in MongoDB Atlas
* Each survey response is saved as a structured document
* Includes user input fields and timestamp

---

## Validation Rules

* Name is required
* City is required
* At least one issue must be selected
* User must confirm data accuracy before submission

---

## Security Considerations

* Database credentials are managed using Streamlit Secrets
* Sensitive information is not stored in source code
* Public repositories should not contain credentials

---

## Troubleshooting

**Application not loading**

* Check if all dependencies are installed

**Database connection error**

* Verify MongoDB connection string
* Ensure IP access is enabled

**Deployment failure**

* Confirm `requirements.txt` is present
* Check Streamlit logs for errors

---

## Future Enhancements

* Data analytics dashboard
* Export responses to CSV or Excel
* Role-based access (admin/user)
* Multi-page application structure

---


