# Clora: CLOra Rotational Application
## Description
This application stores the clothes you have based on categorie, name and description
Data is stored in a text file that can easily be manipulated with either clora itself or an external editor.

## Purpose
The goal of this application is to keep a record of when you need to buy new clothes, so you always know when and what to buy.

## Database
The database is a textfile. I have chosen the .md-extension to allow for markdown to be used.  

The format is as followed:  
    # categories;max  
    category_name_1;max_number_of_items  
    category_name_2;max_number_of_items  
    ...  
    # category_name_1  
    item_of_cat_1_description1;state_of_item_as_int;comment  
    item_of_cat_1_description2;state_of_item_as_int;comment  
    # category_name_2  
    item_of_cat_2_description1;state_of_item_as_int;comment  
    ...  

## Updating
Updating the database can be done via a regular text-editor (as long as you maintain the above convention).
The application itself also contains several options for updating:  
- -a or --add to add a new item  
- -d or --delete to delete an item  
- -u or --update to update an item
