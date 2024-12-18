#!/bin/bash

# Navigate to backend directory
cd backend

# Create directory structure
echo "Creating backend directory structure..."

# Create app directory and subdirectories
mkdir -p app/routes
mkdir -p app/services
mkdir -p app/database

# Create __init__.py files
echo "Creating Python package files..."
touch app/__init__.py
touch app/routes/__init__.py
touch app/services/__init__.py
touch app/database/__init__.py

# Create route files
echo "Creating route files..."
touch app/routes/auth.py
touch app/routes/main.py

# Create service files
echo "Creating service files..."
touch app/services/census.py

# Create database files
echo "Creating database files..."
touch app/database/db_manager.py

# Create main application file
echo "Creating main application file..."
touch app.py

# Create empty __init__.py files with basic content
echo '"""Flask application package."""' > app/__init__.py
echo '"""Routes package."""' > app/routes/__init__.py
echo '"""Services package."""' > app/services/__init__.py
echo '"""Database package."""' > app/database/__init__.py

# Create basic app.py content
cat > app.py << EOL
"""
Main application entry point.
Import and create the Flask application.
"""

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
EOL

echo "Backend structure created successfully!"

# Print directory structure
echo -e "\nCreated backend structure:"
ls4