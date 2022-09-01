from flask import Flask

from .views import statistic_views

def create_app(): # application factory. create_app은 플라스크 내부에서 정의된 함수명
    app = Flask(__name__) # 플라스크 애플리케이션을 생성

    if app.config['DEBUG']: # 디버그 모드일 때
        app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1 # 캐쉬 업데이트 1초 단위로 하기

    from .views import main_views
    app.register_blueprint(main_views.bp) # 블루프린트 객체 bp 등록
    app.register_blueprint(statistic_views.bp)

    return app