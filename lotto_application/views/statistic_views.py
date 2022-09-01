from flask import Blueprint, render_template, request, json
from lotto_application import tools

bp = Blueprint('statistic', __name__, url_prefix='/statistic')
# bp 객체 생성. __name__에는 모듈명인 "main_views"가 인수로 전달

@bp.route('/', methods=['POST'])
def statistic():
    round_list = []
    checks_per_round = []

    recent_round = tools.get_recent_round()
    week_range = int(request.form['week_range'])
    bonus =  request.form.get('with_bonus')
    checked = ''
    if bonus == 'on':
        checked = 'checked'
    # request 객체는 플라스크에서 생성 과정 없이 사용할 수 있는 기본 객체
    # 이 객체를 이용해 브라우저에서 요청한 정보를 확인할 수 있다.
    for i in range(week_range):
        round_list.append(recent_round - i)
        checks = tools.get_checks_per_round(round_list[-1], bonus)
        checks_per_round.append(checks)
    count_per_num = tools.count_win_nums(checks_per_round)
    desc_count = tools.index_for_desc(count_per_num)

    statistics = json.dumps({
        "checks_per_round" : checks_per_round,
        "count_per_num" : count_per_num,
        "desc_count" : desc_count
    })
    
    return render_template("statistic.html", round_list=round_list, statistics=statistics, checked=checked)