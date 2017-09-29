$.get('http://swapi.co/api/films?format=json', function () {
  $('#character').text(data.name);
});
