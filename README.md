[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/TNLLzJ67)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=16819164&assignment_repo_type=AssignmentRepo)
# CensusConnect: Secure Census Data Access Platform

## Description/Motivation

CensusConnect is a secure web application designed to democratize access to American Community Survey (ACS) data while implementing robust security measures to protect user information and data access patterns. The platform features a comprehensive user authentication system that not only secures access but also enhances the user experience through personalized data management.

### Core Components:

#### Advanced Authentication System
- Multi-factor authentication
- Secure session management
- Rate limiting and brute force protection
- Admin dashboard for security monitoring
- Email verification system
- Password reset functionality with secure tokens

#### Data Access Platform
- Simplified ACS data retrieval
- Automatic variable code mapping across years
- Geographic customization options
- Interactive visualization tools
- Data export capabilities
- Collaborative features

The motivation behind this project is twofold:
1. Implement a production-grade authentication system that follows security best practices and protects sensitive data access.
2. Make Census Bureau data more accessible to researchers and analysts who may lack technical expertise in API integration and data processing.

For detailed information about the backend structure and implementation, see our [Backend Documentation](codebase/backend/backend_documentation/BACKEND_STRUCTURE.md).

### Prerequisites
This is a web application. For detailed setup instructions and requirements working with the repo, please refer to our [Setup Guide](Documentation/setupInstructions.md).

#### Quick Start Requirements:
- Python 3.10+
- PostgreSQL 12+
- Node.js 16+
- Redis (for caching)
- SendGrid API key (for email verification)

### Built With
- **Flask**: Python web framework for backend development
- **PostgreSQL**: Database for user management and data caching
- **bcrypt**: Password hashing
- **Redis**: Session management and caching
- **SendGrid**: Email service for user verification
- **D3.js**: Data visualization
- **Tailwind**: Frontend styling
- **VSCode** with Python and PostgreSQL extensions

### Author
- Nicholas Hamilton: [GitHub Profile](https://github.com/hamiltonnBC)

## Security Considerations and Acknowledgments
For a comprehensive overview of security implementations and acknowledgments, please refer to our [Security Documentation](Documentation/securityConsiderations.md).

### Key Security Features:
- OWASP compliant authentication system
- Rate limiting and request throttling
- Secure session management
- SQL injection prevention
- XSS protection
- CSRF protection
- Comprehensive security logging

This project embraces security best practices while making Census data more accessible to users of all technical backgrounds. The robust authentication system ensures that data access is both secure and user-friendly.

## For Software Requirements Specification (SRS) and Conceptual Documentation
For detailed information about the software requirements and conceptual documentation, please refer to the following files:
- [Software Requirements Specification](Documentation/requirements.md)
- [Conceptual Documentation](Documentation/concept.md)

## About the Author
Nicholas Hamilton is a software developer with a passion for data security and accessibility. With a background in computer science and cybersecurity, Nicholas has a keen interest in developing secure web applications that make complex data more accessible to users of all technical backgrounds.

## Backend Structure and Component Interaction

For detailed information about the backend structure and component interactions, please refer to the following files:
- [Backend Structure](Documentation/BACKEND_STRUCTURE.md)
- [Backend Component Interaction](codebase/backend/backend_documentation/BACKEND_COMPONENT_INTERACTION.md)

## License (not required initially)

This project is licensed under the ??? License - see the wiki page (https://en.wikipedia.org/wiki/Software_license) for details

