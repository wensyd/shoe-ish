# Shoe-ish - Project 4
#### By Wensy DeSousa

## Project Summary

Shoe-ish is a full-stack application created using a masonite backend and react frontend. Shoe-ish will allow a user to find their most favorite shoes and add them to a collection which can be marked off as purchased making this the ultimate shoe wish app. 

## Models/ Schema


{
    table.increments("id")
    table.timestamps()
    table.string("title")
    table.string("image")
    table.string("description")
    table.Boolean("purchased")
}

## Route Table

List your routes in a table

| url | method | action |
|-----|--------|--------|
| /shoes | get | get all shoes (index)|
| /shoes/:id | get | get a particular shoe (show)|
| /shoes/new | get | return form to create a new shoe (new)|
| / | post | get post request to /shoes, create new and redirect to index (create)|
| /shoes/:id/edit | get | edit a particular shoe (edit)|
| /shoes/:id | put | put request to /shoes/:id (update)|
| /shoes/:id | delete | deletes a particular shoe (destroy)|

## User Stories

-user can view all pictures on main page (index).
-user can select picture and it redirects to show page for that particular picture. 
-user can edit picture, title, description of each shoe.
-user can delete picture.
-user can update picture.
-user can go back to main page from show page.
-user can create new picture/file/shoe. 
-user can mark the shoe complete with checkbox.

## List of Technologies

-html
-css
-Bootstrap or Milligram
-Python 
-Masonite
-React
-JS
-Postgres


## Wireframes

coming soon...


## Challenges

- no challenges anticipated yet. Will update as I build. 
