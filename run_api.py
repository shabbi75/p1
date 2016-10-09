from api import create_app


app = create_app({
    "SECRET_KEY": "homework",
    "DEBUG": True
})

app.run(port=3000)
