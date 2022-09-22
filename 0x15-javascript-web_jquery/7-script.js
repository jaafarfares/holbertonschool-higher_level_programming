const namee = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.getJSON(namee, function (data) {
  $('DIV#character').text(data.name);
});
