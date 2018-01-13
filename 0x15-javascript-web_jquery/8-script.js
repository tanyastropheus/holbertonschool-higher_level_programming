const endPoint = 'https://swapi.co/api/films/?format=json';
$.get(endPoint, function (data) {
  // how to check if request is successful?
  for (let ep = 0; ep < data['results'].length; ep++) {
    $('#list_movies').append('<li>' + data['results'][ep]['title'] + '</li>');
  }
});
