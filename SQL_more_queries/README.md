# SQL More Queries

This project covers advanced SQL topics including users, privileges, constraints, and complex queries.

## Learning Objectives

- Create MySQL users and manage privileges
- Use constraints: NOT NULL, UNIQUE, PRIMARY KEY, FOREIGN KEY
- Write SELECT statements with multiple tables
- Use JOIN (INNER, LEFT, RIGHT)
- Use subqueries
- Use GROUP BY and aggregate functions

## Files

- `0-privileges.sql` - Show user privileges
- `1-create_user.sql` - Create user with all privileges
- `2-create_read_user.sql` - Create user with SELECT only
- `3-force_name.sql` - Table with NOT NULL
- `4-never_empty.sql` - Table with DEFAULT value
- `5-unique_id.sql` - Table with UNIQUE constraint
- `6-states.sql` - Create states table with PRIMARY KEY
- `7-cities.sql` - Create cities table with FOREIGN KEY
- `8-cities_of_california_subquery.sql` - Subquery example
- `9-cities_by_state_join.sql` - INNER JOIN example
- `10-genre_id_by_show.sql` - JOIN with WHERE
- `11-genre_id_all_shows.sql` - LEFT JOIN
- `12-no_genre.sql` - WHERE IS NULL
- `13-count_shows_by_genre.sql` - GROUP BY and COUNT
- `14-my_genres.sql` - Multiple JOINs
- `15-comedy_only.sql` - Multiple JOINs with WHERE
- `16-shows_by_genre.sql` - LEFT JOIN with multiple tables

## Usage

```bash
cat 0-privileges.sql | mysql -uroot -p
```

## Note

For exercises 10-16, you need to import the database dump:
```bash
curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
```
