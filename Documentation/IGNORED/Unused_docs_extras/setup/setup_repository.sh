#!/bin/bash

# Navigate to codebase directory
cd codebase

# Create main directories and files
echo "Creating directory structure..."

# Create main directories
mkdir -p backend
mkdir -p frontend
mkdir -p config/{development,production,testing}
mkdir -p docs/{api,setup,architecture,database}
mkdir -p scripts/{db,deployment}
mkdir -p tests/{unit,integration,e2e}

# Create empty configuration files
touch config/development/config.py
touch config/production/config.py
touch config/testing/config.py

# Create empty documentation files
touch docs/README.md
touch docs/api/README.md
touch docs/setup/README.md
touch docs/architecture/README.md
touch docs/database/README.md

# Create empty script files
touch scripts/db/init_db.py
touch scripts/deployment/deploy.sh
chmod +x scripts/deployment/deploy.sh

# Create empty test files
touch tests/unit/README.md
touch tests/integration/README.md
touch tests/e2e/README.md

echo "Repository structure created successfully!"

# Print directory structure
echo -e "\nCreated directory structure:"
tree -L 3