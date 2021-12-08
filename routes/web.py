"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),
    RouteGroup([
    Get("/", "ShoeController@index").name("index"),
        Get("/@id", "ShoeController@show").name("show"),
        Post("/", "ShoeController@create").name("create"),
        Put("/@id", "ShoeController@update").name("update"),
        Delete("/@id", "ShoeController@destroy").name("destroy"),
    ], prefix="/shoe", name="shoe")
]
