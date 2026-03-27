# Python Server-Side Rendering

This project covers server-side rendering concepts using Python and Flask. Learn how to use Jinja templating, work with multiple data sources (JSON, CSV, SQLite), and build dynamic web applications.

## Learning Objectives

At the end of this project, you should be able to:

- Create Python functions to manipulate template strings and generate files
- Set up a basic Flask application with template rendering
- Use Jinja templates for dynamic content generation
- Implement loops and conditional statements in Jinja
- Read and parse data from different file formats (JSON, CSV)
- Interact with SQLite databases in Flask
- Handle multiple data sources in a single application
- Implement error handling for file and database operations
- Create reusable template components

## General Requirements

- All files must be compatible with Python 3
- All Python files must start with `#!/usr/bin/python3`
- All Python files must end with a new line
- Allowed editors: Any editor of your choice
- Flask application runs on port 5000 by default
- All code should follow PEP 8 style guidelines
- Use meaningful variable names and comments where necessary

## Project Structure

```
python-server_side_rendering/
├── task_00_intro.py          # Template generation with file output
├── task_01_jinja.py          # Basic Flask app with Jinja templates
├── task_02_logic.py          # Dynamic templates with loops and conditions
├── task_03_files.py          # JSON and CSV data source handling
├── task_04_db.py             # SQLite database integration
├── create_db.py              # Database creation script
├── template.txt              # Email invitation template
├── items.json                # Sample items data
├── products.json             # Products data (JSON format)
├── products.csv              # Products data (CSV format)
├── products.db               # SQLite database (created by create_db.py)
├── templates/
│   ├── header.html           # Reusable header component
│   ├── footer.html           # Reusable footer component
│   ├── index.html            # Home page
│   ├── about.html            # About page
│   ├── contact.html          # Contact page
│   ├── items.html            # Items list page with dynamic loops
│   └── product_display.html  # Product display with table formatting
└── README.md                 # This file
```

## Tasks

### Task 0: Creating a Simple Templating Program
**File:** `task_00_intro.py`

Create a Python function that generates personalized invitation files from a template with placeholders.

**Function:** `generate_invitations(template, attendees)`

**Features:**
- Validates input types (template must be string, attendees must be list of dicts)
- Handles empty inputs with appropriate error messages
- Replaces placeholders: `{name}`, `{event_title}`, `{event_date}`, `{event_location}`
- Replaces missing values with "N/A"
- Generates sequentially numbered output files: `output_1.txt`, `output_2.txt`, etc.

**Error Handling:**
- Empty template → "Template is empty, no output files generated."
- Empty attendees list → "No data provided, no output files generated."
- Invalid template type → "Error: template is not a string"
- Invalid attendees type → "Error: attendees is not a list of dictionaries"

**Test Data:**
```python
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]
```

---

### Task 1: Creating a Basic HTML Template in Flask
**File:** `task_01_jinja.py`

Build a basic Flask application that serves web pages using Jinja templates.

**Routes:**
- `/` - Home page
- `/about` - About page
- `/contact` - Contact page

**Features:**
- Uses `render_template()` to render HTML pages
- Implements reusable header and footer components
- All pages include navigation menu with links to Home, About, and Contact
- Demonstrates template inclusion with `{% include %}`

**Template Files:**
- `header.html` - Site header with navigation
- `footer.html` - Site footer with copyright info
- `index.html` - Home page content
- `about.html` - About page with description
- `contact.html` - Contact page with contact information

**How to Run:**
```bash
python3 task_01_jinja.py
# Visit http://localhost:5000
```

---

### Task 2: Creating a Dynamic Template with Loops and Conditions in Flask
**File:** `task_02_logic.py`

Enhance the Flask application with dynamic content using Jinja loops and conditionals.

**Additional Route:**
- `/items` - Displays a list of items from JSON file

**Features:**
- Reads data from `items.json`
- Uses `{% for %}` loops to iterate over items
- Uses `{% if %}` conditionals to handle empty lists
- Displays "No items found" message when list is empty

**Jinja Concepts Used:**
- `{% for item in items %}` - Iteration
- `{% if condition %}` - Conditional rendering
- `{{ variable }}` - Variable interpolation

**Data Source:** `items.json`
```json
{
    "items": ["Python Book", "Flask Mug", "Jinja Sticker"]
}
```

**How to Run:**
```bash
python3 task_02_logic.py
# Visit http://localhost:5000/items
```

---

### Task 3: Displaying Data from JSON or CSV Files in Flask
**File:** `task_03_files.py`

Build a feature to read and display product data from multiple formats.

**Route:**
- `/products` - Displays products with query parameters

**Query Parameters:**
- `source` - Required: `json` or `csv`
- `id` - Optional: Filter by product ID

**Features:**
- Reads products from JSON or CSV files
- Filters by ID when provided
- Handles missing product IDs gracefully
- Displays error messages for invalid sources
- Uses HTML table for data display

**Error Handling:**
- Invalid source → "Wrong source"
- Product ID not found → "Product not found"
- Missing files → Empty list

**File Reading Functions:**
- `read_json(product_id=None)` - Reads from JSON file
- `read_csv(product_id=None)` - Reads from CSV file

**Test URLs:**
```
http://localhost:5000/products?source=json
http://localhost:5000/products?source=csv
http://localhost:5000/products?source=json&id=1
http://localhost:5000/products?source=xml  # Error
```

**Data Sources:**
- `products.json` - JSON format products
- `products.csv` - CSV format products

**How to Run:**
```bash
python3 task_03_files.py
# Visit http://localhost:5000/products?source=json
```

---

### Task 4: Extending Dynamic Data Display to Include SQLite in Flask
**File:** `task_04_db.py`

Extend the previous application to include SQLite database as a data source.

**Database Setup:**
Run `create_db.py` first to set up the database:
```bash
python3 create_db.py
# This creates products.db with sample data
```

**Route:**
- `/products` - Same as Task 3, now with `sql` source option

**Query Parameters:**
- `source` - Required: `json`, `csv`, or `sql`
- `id` - Optional (not used in Task 4, but extensible)

**Features:**
- Connects to SQLite database
- Executes SELECT queries to fetch products
- Converts database rows to dictionaries
- Uses the same template as Task 3
- Graceful error handling for database issues

**File Reading Functions:**
- `read_json()` - Reads from JSON file
- `read_csv()` - Reads from CSV file
- `read_sql()` - Reads from SQLite database

**Database Schema:**
```sql
CREATE TABLE Products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL
)
```

**Test URLs:**
```
http://localhost:5000/products?source=json
http://localhost:5000/products?source=csv
http://localhost:5000/products?source=sql
```

**How to Run:**
```bash
# First, create the database
python3 create_db.py

# Then run the Flask app
python3 task_04_db.py

# Visit http://localhost:5000/products?source=sql
```

---

## Data Files

### template.txt
Email invitation template with placeholders for personalization:
```
Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team
```

### items.json
Sample items list for Task 2:
```json
{
    "items": ["Python Book", "Flask Mug", "Jinja Sticker"]
}
```

### products.json
Product data in JSON format (Tasks 3 & 4):
```json
[
  {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
  {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99}
]
```

### products.csv
Product data in CSV format (Task 3):
```
id,name,category,price
1,Laptop,Electronics,799.99
2,Coffee Mug,Home Goods,15.99
```

### products.db
SQLite database (created by `create_db.py`):
- Table: `Products`
- Columns: `id`, `name`, `category`, `price`

---

## Key Concepts

### Task 0: String Templating
- `str.replace()` method for placeholder substitution
- Type checking with `isinstance()`
- File operations with `open()` and `write()`
- Dictionary methods: `.get()` for safe key access

### Task 1: Flask & Jinja Basics
- Flask application structure and routing
- `render_template()` function
- Template inclusion with `{% include %}`
- Static HTML file organization

### Task 2: Dynamic Content
- Jinja `{% for %}` loops
- Jinja `{% if %}` conditions
- JSON parsing with `json.load()`
- Template variable passing with `render_template()`

### Task 3: Multiple Data Sources
- JSON file reading with `json.load()`
- CSV file reading with `csv.DictReader()`
- Query parameter retrieval with `request.args.get()`
- HTML table rendering
- Error handling for missing data

### Task 4: Database Integration
- SQLite3 module for database connections
- SQL SELECT queries
- Row factory for dictionary conversion
- Exception handling for database errors

---

## Running the Application

### Prerequisites
```bash
pip install Flask
```

### Running Each Task

**Task 1 - Basic Templates:**
```bash
cd python-server_side_rendering
python3 task_01_jinja.py
# Visit http://localhost:5000
```

**Task 2 - Dynamic Templates:**
```bash
python3 task_02_logic.py
# Visit http://localhost:5000/items
```

**Task 3 - Multiple Data Sources:**
```bash
python3 task_03_files.py
# Visit http://localhost:5000/products?source=json
```

**Task 4 - Database Integration:**
```bash
# First create the database
python3 create_db.py

# Run the application
python3 task_04_db.py
# Visit http://localhost:5000/products?source=sql
```

---

## Testing Checklist

### Task 0
- [ ] Test with valid template and attendees list
- [ ] Test with empty template → Error message printed
- [ ] Test with empty attendees list → Error message printed
- [ ] Test with None values in attendee data → "N/A" appears in output
- [ ] Verify output files created sequentially

### Task 1
- [ ] Access `/` shows home page
- [ ] Access `/about` shows about page
- [ ] Access `/contact` shows contact page
- [ ] All pages display header with title
- [ ] All pages display footer with copyright
- [ ] Navigation menu appears on all pages

### Task 2
- [ ] Access `/items` displays list of items
- [ ] Each item appears in separate `<li>` element
- [ ] "No items found" message appears when list is empty
- [ ] CSS styling applies correctly

### Task 3
- [ ] Access with `source=json` shows JSON products
- [ ] Access with `source=csv` shows CSV products
- [ ] Filter by `id=1` shows only that product
- [ ] Invalid `source=xml` shows "Wrong source" error
- [ ] Non-existent `id=999` shows "Product not found" error
- [ ] Table displays all product information correctly

### Task 4
- [ ] Database created successfully with `create_db.py`
- [ ] Access with `source=sql` shows products from database
- [ ] Same template displays data from json, csv, and sql sources
- [ ] Data displays correctly in table format

---

## File Positions

All files should be in the `python-server_side_rendering/` directory:
- Python scripts in root directory
- Data files (`.txt`, `.json`, `.csv`) in root directory
- HTML templates in `templates/` subdirectory
- Database file (products.db) created in root directory when `create_db.py` runs

---

## Troubleshooting

**Port 5000 already in use:**
```python
# In task file, change:
app.run(debug=True, port=5001)  # Use different port
```

**Template not found error:**
- Ensure `templates/` folder exists
- Verify HTML files are in `templates/` directory
- Flask automatically looks in `templates/` folder

**JSON/CSV file not found:**
- Ensure data files (.json, .csv) are in the same directory as Python script
- Check file permissions for read access

**Database locked error:**
- Close any other instances using the database
- Delete `products.db` and run `create_db.py` again

---

## Author

Holberton School - Python Curriculum

## License

Copyright © 2024 Holberton School - All rights reserved
