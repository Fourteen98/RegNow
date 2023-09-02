# RegNow

This is a FastAPI project that showcases a student registration system api for Koforidua Technical University CSC BTECH(weekends) 23/24 Software Engineering Course.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Linters](#linters)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

- Python 3.x (Recommended: Python 3.8 or later)
- pip (Python package manager)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Fourteen98/RegNow.git
```
2. Navigate to project directory
```bash
cd RegNow
```
3. Create a virtual environment
- On macOs/Linux
```bash
python3 -m venv venv
```
- On Windows
```powershell
python -m venv venv
```
4. Activate the virtual environment
- On macOs/Linux
```bash
source venv/bin/activate
```
- On Windows
```powershell
venv\Scripts\Activate
```
5. Install project dependencies
```bash
pip install -r requirement.txt
```
## Usage
Run the development server
```bash
hypercorn app.main:app --bind 0.0.0.0:80 --reload
```
Open your browser and navigate to http://127.0.0.1:8000 to access the API.

## Linters
- Check for flake8 linter
```
flake8 .
```
- Or auto fix flake8 linter
```bash
autopep8 --in-place --recursive . && isort -rc .
```
## API Documentation
The API documentation is automatically generated using Swagger UI. You can access the documentation by visiting http://127.0.0.1:8000/docs or http://127.0.0.1:8000/redoc after starting the development server.

## Contributing
Contributions are welcome! If you have any bug fixes, improvements, or new features, please open an issue or a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

## Authors
👤 Muhyideen Elias
GitHub: @fourteen98

