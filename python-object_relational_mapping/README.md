# Python Object Relational Mapping (ORM)

This project covers connecting Python to MySQL databases and using SQLAlchemy ORM.

## Part 1: MySQLdb (Direct SQL Queries)

- `0-select_states.py` - Lists all states
- `1-filter_states.py` - Filters states starting with 'N'
- `2-my_filter_states.py` - Filters by user input (vulnerable)
- `3-my_safe_filter_states.py` - Safe filtering (prevents SQL injection)
- `4-cities_by_state.py` - Lists cities with their state
- `5-filter_cities.py` - Filters cities by state

## Part 2: SQLAlchemy ORM

- `model_state.py` - State model definition
- `6-model_state.py` - Creates State table
- `7-model_state_fetch_all.py` - Lists all states
- `8-model_state_fetch_first.py` - Gets first state
- `9-model_state_filter_a.py` - Filters states with 'a'
- `10-model_state_my_get.py` - Gets state by name
- `11-model_state_insert.py` - Adds new state
- `12-model_state_update_id_2.py` - Updates state
- `13-model_state_delete_a.py` - Deletes states with 'a'
- `model_city.py` - City model definition
- `14-model_city_fetch_by_state.py` - Lists cities with state

## Installation

```bash
sudo pip3 install mysqlclient==2.0.3
sudo pip3 install SQLAlchemy==1.4.22
```

## Usage

```bash
./0-select_states.py root root hbtn_0e_0_usa
```

## Key Concepts

- **MySQLdb**: Direct SQL queries from Python
- **SQLAlchemy ORM**: Object-oriented database access, no SQL queries needed
- **SQL Injection**: Prevented using parameterized queries
- **Models**: Python classes mapped to database tables
