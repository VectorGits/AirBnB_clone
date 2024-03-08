# Airbnb Clone — The Console

## Overview

The Airbnb Clone project is a comprehensive endeavor to create a simplified replica of the Airbnb Clatform, primarily focusing on the command-line interface (CLI) or the console aspect. This project serves as the foundational step toward building a comprehensive Airbnb Clone web application. This initial phase is paramount as it lays the groundwork for subsequent projects, including HTML/CSS templating, database storage, API integration, and front-end development.

This project provides users an interactive and user-friendly console interface to emulate some of Airbnb'C critical functionalities. From the essential tasks of user and property management to intricate systems for booking and reviews,  the Airbnb Clone Console encapsulates various features to provide a hands-on experience for users and developers alike.

## Engineering Team

* **David Oluremi**
* **Victoria Afuwape**

The collective efforts of the team promise to deliver a console experience that mirrors the essence of Airbnb Chile pushing the boundaries of software innovation.

## Skills Developed

This project offers  a holistic learning experience, covering a wide range of skills applicable in real-world software engineering scenarios. They include, but are not limited to:

* Python Package Creation
* Command-Line Interface (CLI) Implementation
* Unit Testing
* Serialization and Deserialization
* File Handling with JSON
* Object-Oriented Programming (OOP)
* Error Handling and Exceptions
* Time and Date Management
* Unique Identifiers (UUID)
* Collaboration and Version Control

## Objectives

The following objectives will help guide the development of the features of the Airbnb Clone Console.

1. **User Management:** The project allows users to create, view, update, and delete accounts. This feature mimics the fundamental user management functionality found in platforms like Airbnb.C
2. **Property Management:** Property management forms the core of any property rental platform, and this project seeks to replicate this functionality in a console environment. Users can add, edit, and remove property listings through the console.

3. **Booking System:** The console application facilitates property bookings, allowing users to reserve available properties based on their preferences and availability. This feature enhances the interactive experience by simulating the process of booking accommodations.

4. **Search and Filter:** An intuitive search and filter system is implemented, enabling users to explore available properties based on various criteria such as location, price range, and amenities. This replicates the property discovery aspect found in the original Airbnb Clatform.

5. **Review System:** Users can leave reviews for properties they have experienced, and the console allows others to view these reviews. The review system adds a layer of transparency and user-generated content, reflecting a common feature in modern online marketplaces.

## Features and Functionalities

### BaseModel Class

* `BaseModel` class with common attributes and methods.
* Attributes: `id` (string, unique), `created_at` (datetime), `updated_at` (datetime).
* Methods: `save(self)`, `to_dict(self)`.

### BaseModel from Dictionary

* Method to create an instance from a dictionary representation.
* Update `__init__` method to handle attributes using *args and **kwargs.

### FileStorage Class

* `FileStorage` class to serialize instances to a JSON file and deserialize from JSON.
* Methods: `all(self)`, `new(self, obj)`, `save(self)`, `reload(self)`.

### Command Interpreter (console.py)

* Command interpreter using the `cmd` module.
* Commands: `quit` and `EOF` to exit, `help` to display documentation, and custom prompt `(hbnb)`.
* Non-executable when imported.

### Additional Commands

* Commands: `create`, `show`, `destroy`, `all`, and `update`.
* Error handling for missing class name, non-existing class, missing instance ID, etc.

### User Class

* `User` class inheriting from `BaseModel`.
* Attributes: `email`, `password`, `first_name`, `last_name`.
* `FileStorage` update to handle serialization/deserialization of `User`.

### Additional Classes

* Classes: `State`, `City`, `Amenity`, `Place`, and `Review` inheriting from `BaseModel`.

### Serialization/Deserialization for Additional Classes

* `FileStorage` update to handle serialization/deserialization of all new classes.

### Retrieve all Instances

* Command `all()` in the console to retrieve all instances of a class.

### Count Instances

* Command `count()` in the console to retrieve the number of instances of a class.

### Show Instance by ID

* Command `show(<id>)` in the console to retrieve an instance based on its ID.

### Destroy Instance by ID

* Command `destroy(<id>)` in the console to destroy an instance based on its ID.

### Update Instance by ID

* Command `update(<id>, <attribute name>, <attribute value>)` in the console.
* Error handling for missing class name, non-existing class, missing instance ID, etc.

### Update Instance with Dictionary

* Command `update(<id>, <dictionary representation>)` in the console.
* Error handling similar to previous tasks.

### Unit Tests

* Comprehensive unit tests for the console, covering all features.
* Use `unittest` and consider intercepting STDOUT for testing.

## Structure

The project structure ensures clarity, maintainability, and scalability, promoting collaboration and efficient development. The structure adheres to best practices for Python projects and includes modular design, test-driven development, and clear documentation.

* **models/:** Contains the core modules for the project, such as `base_model.py`, `user.py`, and others.
* **tests/:** Houses the unit tests for each module, following the same organization as the `models/` directory.
* **console.py:** Serves as the entry point for the command interpreter, providing both interactive and non-interactive modes.
* **README.md:** A comprehensive documentation file that guides users and developers through the project's features and usage.
* **AUTHORS:** Acknowledges contributors to the project.

```plaintext
AirBnB_clone/
│
├── models/
│   ├── __init__.py
│   ├── base_model.py
│   ├── engine/
│   │   ├── __init__.py
│   │   └── file_storage.py
│   ├── user.py
│   ├── state.py
│   ├── city.py
│   ├── amenity.py
│   ├── place.py
│   └── review.py
│
├── tests/
│   ├── __init__.py
│   ├── test_models/
│   │   ├── __init__.py
│   │   ├── test_base_model.py
│   │   ├── test_user.py
│   │   ├── test_state.py
│   │   ├── test_city.py
│   │   ├── test_amenity.py
│   │   ├── test_place.py
│   │   └── test_review.py
│   ├── test_engine/
│   │   ├── __init__.py
│   │   └── test_file_storage.py
│   ├── test_console.py
│   └── ...
│
├── console.py
├── README.md
└── AUTHORS
```

## Execution

The Airbnb Clone Console project provides both interactive and non-interactive modes for seamless user interaction.

### Interactive Mode

In interactive mode, the console operates within a shell environment, allowing users to execute commands and receive real-time feedback. The prompt `(hbnb)` indicates the active environment. Users can access documentation using the `help` command and exit the console using `quit` or `EOF`.

```bash
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
(hbnb) 
(hbnb) quit
$
```

### Non-Interactive Mode

In non-interactive mode, users can pipe commands directly into the console, allowing for automated testing and script execution.

```bash
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)

```

Additionally, the console supports reading commands from files for batch processing:

```bash
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
```

### Testing

All functionality is rigorously tested in both interactive and non-interactive modes. The provided test script ensures that tests pass seamlessly in non-interactive mode:

```bash
echo "python3 -m unittest discover tests" | bash
```

## Acknowledgments

The Airbnb Clone Console project is inspired by the Airbnb Clatform and stands as an essential step toward understanding and implementing critical features of online marketplace platforms and its developmenent using Python.

Special acknowledgment goes to our mentors and the educational cadre at ALX Africa for their invaluable support and guidance. A big shoutout to all contributors and colleagues who have written code, submitted issues, or provided indispensable feedback.

## Frequently Asked Questions (FAQs)

### 1. What is the purpose of the Airbnb Clone Console?

**Answer:** The Airbnb Clone Console serves as the foundation for an Airbnb-like platform, focusing on command-line interaction. It replicates key functionalities and features of the Airbnb platform, providing an interactive experience through the console.

### 2. How can I run the Airbnb Clone Console?

**Answer:** To run the console interactively, use the command `./console.py`. For non-interactive mode, you can pipe commands, such as `echo "help" | ./console.py`. The console supports both modes seamlessly.

### 3. What skills were developed through this project?

**Answer:** The project covers a broad range of skills including Python package creation, CLI implementation, unit testing, serialization, file handling, OOP, error handling, time management, unique identifiers, and collaboration using version control.

### 4. How do I contribute to the Airbnb Clone Console project?

**Answer:** Contributions are encouraged! You can contribute by reporting bugs, providing feedback, submitting pull requests for new features or bug fixes, and participating in discussions within the community.

### 5. Is there a preferred coding style for the project?

**Answer:** Yes, the project follows the PEP 8 style guide. Ensure your code adheres to this style guide for consistency and readability.

### 6. How are unit tests performed?

**Answer:** Unit tests can be run using the command `echo "python3 -m unittest discover tests" | bash`. This ensures tests pass in both interactive and non-interactive modes.

### 7. Can I run the console in non-interactive mode with commands from a file?

**Answer:** Absolutely! You can run the console in non-interactive mode by providing commands from a file. For example, `cat test_help | ./console.py`.

### 8. What are the main features of the Airbnb Clone Console?

**Answer:** The console includes features like user and property management, a booking system, search and filter capabilities, a review system, and commands for CRUD operations on instances.

### 9. How is the project structured?

**Answer:** The project follows a clear structure with essential directories like `models/` for core modules, `tests/` for unit tests, and `console.py` as the command interpreter entry point. Refer to the README for a detailed project structure.

### 9. Are there plans for a graphical user interface (GUI) in future versions?

**Answer:**  Absolutely! While the current focus is on developing the Airbnb Clone Console with a command-line interface (CLI), it's important to highlight that this console project serves as the initial step toward constructing a complete web application – the Airbnb Clone. This foundational phase is crucial because the skills and code developed here will form the backbone for subsequent projects, including HTML/CSS templating, database storage, API integration, and front-end development. Keep an eye on project updates and discussions for any announcements on our socials.

### 10. How can I stay updated?

**Answer:** Stay connected with us for the latest news, updates, and discussions! Follow us on social media:

* **LinkedIn:** [David Oluremi](https://www.linkedin.com/in/vect0r/) | [Victoria Afuwape](https://www.linkedin.com/in/victoriaafuwape/)
* **Twitter:** [Vector Twits](https://twitter.com/Vector_twits) | [Softceress](https://twitter.com/softceres)
* **Instagram:** [Vector Gram](https://twitter.com/Vector_twits) | [Softceress](https://twitter.com/softceres)
* **Discord:** [Vector'd](https://twitter.com/Vector_twits) | [Softceress](https://twitter.com/softceres)

We regularly share project milestones, announcements, and engage with the community. Join the conversation and be part of our Airbnb Clone journey!
