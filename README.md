# Restaurant-Management-System

## Overview
This is a simple restaurant management system implemented in Python. The system allows you to manage menu items, table bookings, order processing, income calculation, and popularity tracking of menu items for Luccio Carlo's, a small family-run Italian restaurant.

## Features

- Display menu items and their prices.
- Manage table bookings for early and late sessions.
- Process orders and calculate order fees.
- Track the popularity of menu items.
- Calculate total income and tips collected.
- Handle beverage orders separately.
- Display table status and costs.

## Class Descriptions

### `MenuItem`
The `MenuItem` class manages the menu items and their prices, as well as tracking the popularity of each item.

#### Methods
- `__init__()`: Initializes menu items and their prices, and sets the popularity of each item to zero.
- `display_menu_items()`: Displays the menu items and their prices.

### `Restaurant`
The `Restaurant` class manages the restaurant's operations, including table bookings, order processing, income calculation, and menu popularity tracking.

#### Methods
- `__init__()`: Initializes tables for early and late sessions, lists for booked tables, variables for orders, income, tips, and the menu.
- `order_manager()`: Manages the order process for early and late sessions.
- `place_order_for_session(session_tables, booked_tables, session_name, customer, diners_count)`: Places an order for a specific session.
- `process_order(table, table_number, session_name)`: Processes the order for a table and calculates the order fee.
- `handle_beverage_order(table_number, table, order_item, quantity)`: Handles beverage orders and updates the total income.
- `complete_payment(table, booked_tables, customer, diners_count, table_number, session_name, order_fee, tips)`: Completes the payment process and updates table status.
- `calculate_income()`: Calculates and displays the total income and tips collected.
- `table_status()`: Displays the status of tables for both sessions.
- `display_tables_status(tables)`: Helper method to display the status of tables.
- `popularity_items()`: Displays the popularity of menu items.
- `beverages()`: Manages beverage orders for early and late sessions.
- `handle_beverages_for_session(session_tables, session_name)`: Handles beverage orders for a specific session.
- `run()`: Main loop for the restaurant management system.

## Usage

1. **Run the Program:**
   ```sh
   python restaurant_management_system.py
   ```

2. **Menu Options:**
   - `1. BOOKING YOUR TABLE`: Book a table for early or late session and place an order.
   - `2. TABLES STATUS / COSTS`: Display the status and costs of tables.
   - `3. TOTAL INCOME / TIPS`: Calculate and display the total income and tips collected.
   - `4. MENU POPULARITY ITEMS`: Display the popularity of menu items.
   - `5. BEVERAGES`: Manage beverage orders for early and late sessions.
   - `6. EXIT`: Exit the program.

## Notes

- The system supports up to 5 tables for each session.
- Each table can accommodate up to 8 diners.
- Order items must be selected from the menu.
- Beverages are handled separately and can be added to the existing order.

## License

This project is licensed under the MIT License.

## Author

[Dileesha Sithum](https://iamdileesha.site/)
