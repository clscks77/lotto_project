
// statistic data 가져오기
const data = document.querySelector("#statistics_json");
const json = data.dataset.statistics;
const statistics = JSON.parse(json);

const checks = statistics.checks_per_round;
const counts = statistics.desc_count;
const count_per_num = statistics.count_per_num;

const round_cnt = checks.length+1;

// table 채우기
th_cnt = 0
tr_cnt = 0
for (i = 0; i < counts.length; i++){ // 45
    th_cnt = i;
    header = i + 1;
    $("th:eq(" + header + ")").html(counts[i]); // header
    for (j = 1; j < round_cnt; j++) { // round 만큼 반복
        tr_cnt = j;
        $("tr:eq(" + j + ") td:eq(" + i + ")").html(checks[j-1][counts[i]]);
    }
}

// origin table 채우기
th_cnt = th_cnt + round_cnt + 2;
tr_cnt = tr_cnt + 2;
td_cnt = 0;
console.log(th_cnt)
for (i = th_cnt; i < th_cnt + counts.length; i++){
    $("th:eq(" + i + ")").html(i - th_cnt + 1); // header
    for (j = tr_cnt; j < tr_cnt + round_cnt -1; j++) { // round 만큼 반복 
        $("tr:eq(" + j + ") td:eq(" + td_cnt + ")").html(checks[j - tr_cnt][i - th_cnt + 1]);
    }
    td_cnt = td_cnt + 1;
}

// chart 만들기
var data_for_chart = [];
for (i = 0; i < 45; i++){
    data_for_chart.push(count_per_num[counts[i]]);
}
var label_for_chart = [];
for (i = 0; i < 45; i++){
    label_for_chart.push(String(counts[i]));
}

var ctx = document.getElementById("myChart").getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: label_for_chart,
        datasets: [{
            label: '추첨된 회수',
            data: data_for_chart,
            backgroundColor: [
                'rgba(13, 110, 253, 1)',
                'rgba(13, 110, 253, 0.9)',
                'rgba(13, 110, 253, 0.7)',
                'rgba(13, 110, 253, 0.5)',
                'rgba(13, 110, 253, 0.3)',
                'rgba(13, 110, 253, 0.2)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});

//var table = jQuery("table").width();
//("canvas").width(table - 15)