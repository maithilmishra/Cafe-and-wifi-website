# Cafe List Website

## Overview
This project is a dynamic web application that interacts with an SQLite database (`cafes.db`) to manage a list of cafes. The application allows users to:

- View a list of cafes with their details.
- Add new cafes to the database.
- Delete existing cafes from the database.

The project is built using **Flask** for the backend and **HTML/CSS** for the frontend.

## Features

- **Dynamic Cafe Management**: Add and delete cafes in real-time.
- **Responsive Design**: Optimized for both desktop and mobile devices.
- **Simple UI**: User-friendly interface with clear navigation.

## Project Structure
```
/project-root
├── app.py                 # Main application file
├── cafes.db               # SQLite database
├── templates              # HTML templates
│   ├── base.html          # Base layout
│   ├── index.html         # Home page to display cafes
│   └── add_cafe.html      # Page to add new cafes
├── static
│   └── styles.css         # CSS styles
└── README.md              # Project documentation
```

## Requirements

- **Python 3.7+**
- **Flask**

To install Flask, run:
```bash
pip install flask
```

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/maithilmishra/Cafe-and-wifi-website.git
   cd Cafe-and-wifi-website
   ```

2. Ensure `cafes.db` is in the project directory.

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## Usage

### Viewing Cafes
- The homepage displays a list of all cafes in the database.

### Adding a New Cafe
1. Click on "Add Cafe" in the navigation menu.
2. Fill out the form with the cafe name and location.
3. Submit the form to add the cafe to the list.

### Deleting a Cafe
- Click the "Delete" link next to a cafe to remove it from the database.

## Technologies Used

- **Flask**: Backend framework.
- **SQLite**: Lightweight database.
- **HTML5 & CSS3**: Frontend design and structure.

## Future Enhancements

- **Search Functionality**: Allow users to search for cafes by name or location.
- **Edit Cafe**: Add the ability to update existing cafe details.
- **User Authentication**: Restrict add/delete actions to authenticated users.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Inspired by the [LaptopFriendly.co](https://laptopfriendly.co/london) project.
- Thanks to the open-source community for tutorials and guidance.

## Contact

For any questions or feedback, please reach out to:

- **Your Name**: work.maithil@gmail.com
- **GitHub**: [maithilmishra](https://github.com/maithilmishra)

---

**Happy Coding!**

