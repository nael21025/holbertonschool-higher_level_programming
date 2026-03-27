# JavaScript - DOM Manipulation

This project covers DOM manipulation using vanilla JavaScript. Learn how to select elements, modify their properties, handle events, and work with the Fetch API.

## Learning Objectives

At the end of this project, you should be able to:

- Select HTML elements using `document.querySelector()` and `document.getElementById()`
- Modify element styles, classes, and content
- Add event listeners to respond to user interactions
- Create and append new elements to the DOM
- Work with the Fetch API to retrieve data from external APIs
- Use Promises with `.then()` to handle asynchronous operations
- Handle DOM events without page reload

## General Requirements

- Allowed editors: Any editor of your choice
- All files will be interpreted on Chrome browser (version 57.0 or later)
- All files should end with a new line
- Files must be semistandard compliant
- Cannot use `var` keyword (use `const` or `let` instead)
- HTML pages should not reload for each action (DOM manipulation only)

## Tasks

### Task 0: Color Me
**File:** `0-script.js`

Updates the text color of the header element to red (#FF0000).

**Method Used:** `document.querySelector()` with inline style modification

**Test File:** `0-main.html`

---

### Task 1: Click and turn red
**File:** `1-script.js`

Updates the header text color to red (#FF0000) when the user clicks on the element with id `red_header`.

**Methods Used:**
- `document.getElementById()` to select the clickable element
- `addEventListener()` to handle click events
- `document.querySelector()` to select the header

**Test File:** `1-main.html`

---

### Task 2: Add `.red` class
**File:** `2-script.js`

Adds the class `red` to the header element when the user clicks on the element with id `red_header`.

**Methods Used:**
- `classList.add()` to add a CSS class
- CSS classes for separation of concerns (style in CSS, logic in JS)

**Test File:** `2-main.html`

**CSS Styles Defined:**
```css
.red {
  color: #FF0000;
}
```

---

### Task 3: Toggle classes
**File:** `3-script.js`

Toggles between `red` and `green` classes on the header when the user clicks on the element with id `toggle_header`.

**Requirements:**
- Header always has exactly one class: either `red` or `green`, never both
- Class never empty
- Initial class: `green`
- Toggles to opposite color on each click

**Methods Used:**
- `classList.contains()` to check if class exists
- `classList.remove()` to remove a class
- `classList.add()` to add a class

**Test File:** `3-main.html`

**CSS Styles Defined:**
```css
.red {
  color: #FF0000;
}
.green {
  color: #00FF00;
}
```

---

### Task 4: List of elements
**File:** `4-script.js`

Adds a new `<li>Item</li>` element to the unordered list when the user clicks on the element with id `add_item`.

**Methods Used:**
- `document.createElement()` to create new elements
- `textContent` to set element text
- `appendChild()` to add element to the DOM
- `document.querySelector()` to select the list by class

**Requirements:**
- New element must be: `<li>Item</li>`
- Element added to `ul` with class `my_list`

**Test File:** `4-main.html`

---

### Task 5: Change the text
**File:** `5-script.js`

Updates the header text to "New Header!!!" when the user clicks on the element with id `update_header`.

**Methods Used:**
- `textContent` to update element text content

**Test File:** `5-main.html`

---

### Task 6: Star wars character
**File:** `6-script.js`

Fetches the character name from the Star Wars API and displays it in the element with id `character`.

**API:** `https://swapi-api.hbtn.io/api/people/5/?format=json`

**Methods Used:**
- `fetch()` to make HTTP requests
- `.then()` to handle Promise responses
- `response.json()` to parse JSON data
- `textContent` to display the fetched name

**Requirements:**
- Uses Fetch API
- Handles Promise with `.then()`
- Character 5 returns: Luke Skywalker

**Test File:** `6-main.html`

---

### Task 7: Star Wars movies
**File:** `7-script.js`

Fetches all Star Wars movie titles from the API and lists them in the `ul` element with id `list_movies`.

**API:** `https://swapi-api.hbtn.io/api/films/?format=json`

**Methods Used:**
- `fetch()` to retrieve data
- `.then()` for Promise chaining
- `forEach()` to iterate through results array
- `document.createElement()` and `appendChild()` to build the list

**Requirements:**
- Lists all movie titles dynamically
- Each title in its own `<li>` element

**Test File:** `7-main.html`

---

### Task 8: Say Hello!
**File:** `8-script.js`

Fetches the translation of "hello" in French and displays it in the element with id `hello`.

**API:** `https://hellosalut.stefanbohacek.com/?lang=fr`

**Special Requirement:** Script must work when imported from the `<head>` tag (not at end of body)

**Methods Used:**
- `DOMContentLoaded` event to wait for DOM to be ready
- `fetch()` to retrieve data
- Promise chaining with `.then()`
- `textContent` to display result

**Important:** The `DOMContentLoaded` event listener ensures the script runs after the DOM is fully loaded, even when placed in the `<head>`.

**Test File:** `8-main.html`

---

## How to Test

1. Open any `-main.html` file in Chrome browser (version 57.0 or later)
2. Test the interactive features:
   - **0-main.html:** Header text should appear in red
   - **1-main.html:** Click "Red header" to change header color to red
   - **2-main.html:** Click "Red header" to apply red class
   - **3-main.html:** Click "Toggle header" to switch between red and green
   - **4-main.html:** Click "Add item" repeatedly to add items to the list
   - **5-main.html:** Click "Update the header" to change header text
   - **6-main.html:** Character name "Luke Skywalker" should load from API
   - **7-main.html:** List of all Star Wars movies should appear
   - **8-main.html:** French translation "Bonjour" should appear

## Key Concepts

### DOM Selection
- `document.querySelector(selector)` - CSS selector (flexible, returns first match)
- `document.getElementById(id)` - Direct ID selection (fastest)
- `document.querySelectorAll(selector)` - Multiple elements

### DOM Manipulation
- `element.style.property` - Inline styles
- `element.classList` - Class manipulation
- `element.textContent` - Text content
- `element.createElement()` - Create new elements
- `element.appendChild()` - Add child elements

### Event Handling
- `addEventListener(event, callback)` - Attach event listeners
- `DOMContentLoaded` - Document ready event
- `click` - Click event

### Fetch API
```javascript
fetch(url)
  .then(response => response.json())
  .then(data => {
    // Process data
  });
```

### Code Quality
- No `var` keyword (use `const` and `let`)
- Semistandard compliant code
- Clear, meaningful variable names
- Proper indentation and formatting

## Author

Holberton School - JavaScript Curriculum

## License

Copyright © 2022 Holberton School - All rights reserved
