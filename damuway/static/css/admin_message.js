window.addEventListener('load', function () {
    const banner = document.createElement('div');
    banner.innerHTML = '✨ Ты в админке DamuWay. Проверяй отзывы, модерируй школы, делай этот мир лучше! 🌍';
    banner.style.background = '#714EFF';
    banner.style.color = 'white';
    banner.style.padding = '12px';
    banner.style.textAlign = 'center';
    banner.style.fontSize = '16px';
    document.body.insertBefore(banner, document.body.firstChild);
});