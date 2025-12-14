#!/usr/bin/env python3
"""
Python script to create the MySQL database 'alx_book_store'.
If the database already exists, the script will not fail.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    """
    Creates the MySQL database 'alx_book_store'.
    Handles connection errors and database creation.
    """
    connection = None
    
    try:
        # Connect to MySQL server (without specifying a database)
        # Update these connection parameters as needed
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''  # Update with your MySQL password if required
        )
        
        if connection.is_connected():
            # Create cursor to execute SQL commands
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            # Using IF NOT EXISTS ensures the script won't fail if database already exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            # Print success message
            print("Database 'alx_book_store' created successfully!")
            
            # Close cursor
            cursor.close()
            
    except Error as e:
        # Handle connection and other database errors
        print(f"Error connecting to MySQL: {e}")
        
    finally:
        # Close database connection
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()

