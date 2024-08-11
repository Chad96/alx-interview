#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      request(character, (err, res, charBody) => {
        if (!err && res.statusCode === 200) {
          console.log(JSON.parse(charBody).name);
        }
      });
    });
  }
});

