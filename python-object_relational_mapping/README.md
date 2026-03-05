# Python Object Relational Mapping

This project introduces connecting Python applications to MySQL databases through two different methods: using MySQLdb for direct SQL queries and SQLAlchemy ORM for object-relational mapping. The project demonstrates database connectivity, query execution, data manipulation, and security practices including SQL injection prevention.

## Project Structure

### Part 1: MySQLdb - Direct SQL Queries

Direct connection and query execution to MySQL databases.

- `0-select_states.py` - Script that lists all states from database
- `1-filter_states.py` - Script that lists states starting with N
- `2-my_filter_states.py` - Script that filters states by user input
- `3-my_safe_filter_states.py` - Script that safely filters states
- `4-cities_by_state.py` - Script that lists all cities with state
- `5-filter_cities.py` - Script that filters cities by state name

### Part 2: SQLAlchemy ORM - Object Relational Mapping

Object-oriented approach to database management without SQL queries.

#### Models
- `model_state.py` - Module containing State class
- `model_city.py` - Module containing City class

#### Scripts
- `6-model_state.py` - Script that creates State table
- `7-model_state_fetch_all.py` - Script that lists all State objects
- `8-model_state_fetch_first.py` - Script that prints first State object
- `9-model_state_filter_a.py` - Script that lists State objects with letter a
- `10-model_state_my_get.py` - Script that gets State by name
- `11-model_state_insert.py` - Script that adds Louisiana state
- `12-model_state_update_id_2.py` - Script that updates state id 2
- `13-model_state_delete_a.py` - Script that deletes states with letter a
- `14-model_city_fetch_by_state.py` - Script that displays cities with states

## Installation Requirements

```bash
sudo pip3 install mysqlclient==2.0.3
sudo pip3 install SQLAlchemy==1.4.22
```

## Usage Examples

```bash
./0-select_states.py root root hbtn_0e_0_usa
./3-my_safe_filter_states.py root root hbtn_0e_0_usa Arizona
./7-model_state_fetch_all.py root root hbtn_0e_6_usa
./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa
```

## Key Concepts

- MySQLdb Module for direct database connections
- SQLAlchemy ORM for object-oriented database access
- SQL Injection Prevention using parameterized queries
- Model Definition as Python classes
- Database Sessions and transactions
- Query Filtering and joins
- CRUD Operations

## Requirements

- Python 3.8.5
- MySQLdb 2.0.x
- SQLAlchemy 1.4.x
- Ubuntu 20.04 LTS
- All files executable and PEP8 compliant
- Complete documentation on all modules and functions

