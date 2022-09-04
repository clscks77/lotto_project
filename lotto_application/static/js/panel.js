// 숫자 패널
const numPanelEl = document.querySelector('.panel');
const panelBtn = document.querySelector('.panel-btn');
let isShowPanel = false;
panelBtn.addEventListener('click', function () {
    isShowPanel = !isShowPanel
    console.log(isShowPanel)
    if (isShowPanel) {
        // 보임 처리!
        gsap.to(numPanelEl, .2, {
            x: -60
        });
    } else {
        // 숨김 처리!
        gsap.to(numPanelEl, .2, {
            x: 0
        });
    }
});