from flask import Flask
from app import stores, models

app = Flask(__name__)

member_store = stores.MemberStore()
post_store = stores.PostsStore()

from app import views
