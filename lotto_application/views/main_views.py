### 블루프린트 : 라우팅 함수 모아둔 곳
from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='/')
# bp 객체 생성. __name__에는 모듈명인 "main_views"가 인수로 전달

@bp.route('/')
def index():
    return render_template("index.html")