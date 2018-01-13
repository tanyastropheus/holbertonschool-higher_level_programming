const endPoint = 'https://swapi.co/api/people/5/?format=json';
$.get(endPoint, function (data) {
  // how to check if request is successful?
  $('#character').text(data['name']);
}, 'json');
