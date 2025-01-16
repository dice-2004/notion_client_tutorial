from flask import Flask,render_template
import os
from api import operate_notion

app = Flask(__name__)

TOKEN = os.environ.get("TOKEN") # Dockerではない場合は、直書きでお願いします
DATABASE_ID = os.environ.get("DATABASE_ID") # Dockerではない場合は、直書きでお願いします
notion =operate_notion.Notion(TOKEN)

print(TOKEN)
print(DATABASE_ID)
@app.route("/")
def home():
    # contents= notion.fetch_database(DATABASE_ID)
    # return render_template("home.html")
    return "Hello World"
@app.route("/<int:id>")
def detail(id):
    # page_id=
    content = notion.fetch_page_content(id)
    return render_template("detail.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
