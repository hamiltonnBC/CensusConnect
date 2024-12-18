#!/usr/bin/env python3
"""
Frontend Directory Setup Script
------------------------------
Creates the complete directory structure and empty files
for the ACS Data Application frontend using direct path creation.
"""

import os

def create_directories():
    """Create all required directories"""
    directories = [
        'templates/components/layout',
        'templates/components/forms',
        'templates/components/alerts',
        'templates/components/cards',
        'templates/components/modals',
        'templates/components/loaders',
        'templates/account',
        'templates/errors',
        'templates/status',
        'templates/email',
        'templates/security',
        'templates/projects'
    ]

    for directory in directories:
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
                print(f"Created directory: {directory}")
        except Exception as e:
            print(f"Error creating directory {directory}: {str(e)}")

def create_files():
    """Create all required template files"""
    files = {
        # Layout components
        'templates/components/layout/base.html': '',
        'templates/components/layout/header.html': '',
        'templates/components/layout/footer.html': '',
        'templates/components/layout/sidebar.html': '',

        # Form components
        'templates/components/forms/password_form.html': '',
        'templates/components/forms/search_form.html': '',
        'templates/components/forms/project_form.html': '',

        # Alert components
        'templates/components/alerts/error.html': '',
        'templates/components/alerts/success.html': '',
        'templates/components/alerts/info.html': '',

        # Card components
        'templates/components/cards/project_card.html': '',
        'templates/components/cards/search_card.html': '',

        # Modal components
        'templates/components/modals/confirm.html': '',
        'templates/components/modals/delete.html': '',

        # Loader components
        'templates/components/loaders/spinner.html': '',
        'templates/components/loaders/progress.html': '',

        # Account pages
        'templates/account/profile.html': '',
        'templates/account/change_password.html': '',
        'templates/account/settings.html': '',

        # Error pages
        'templates/errors/401.html': '',
        'templates/errors/404.html': '',
        'templates/errors/429.html': '',
        'templates/errors/500.html': '',

        # Status pages
        'templates/status/email_sent.html': '',
        'templates/status/reset_link_expired.html': '',

        # Email templates
        'templates/email/activation_email.html': '',
        'templates/email/reset_password_email.html': '',
        'templates/email/notification_email.html': '',

        # Security pages
        'templates/security/locked_account.html': '',
        'templates/security/verify_device.html': '',
        'templates/security/two_factor.html': '',

        # Project pages
        'templates/projects/new_project.html': '',
        'templates/projects/edit_project.html': '',
        'templates/projects/project_details.html': ''
    }

    for filepath, content in files.items():
        try:
            if not os.path.exists(filepath):
                with open(filepath, 'w') as f:
                    f.write(content)
                print(f"Created file: {filepath}")
        except Exception as e:
            print(f"Error creating file {filepath}: {str(e)}")

def main():
    """Main execution function"""
    print("Starting directory and file creation...")
    print(f"Working directory: {os.getcwd()}")

    if not os.path.exists('../../codebase/frontend/templates'):
        print("Error: 'templates' directory not found!")
        return

    create_directories()
    create_files()

    print("\nSetup complete! Directory structure created.")

if __name__ == "__main__":
    main()