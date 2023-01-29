var animation = bodymovin.loadAnimation({
    container: document.getElementById('animContainer'),
    renderer: 'svg',
    loop: true,
    autoplay: true,
    path: '/static/data.json'
  })