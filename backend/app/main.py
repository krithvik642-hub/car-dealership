from .routers import auth, cars

# After the app has been created:
app.include_router(auth.router)
app.include_router(cars.router)