#!/usr/bin/node

const args = process.argv;
const request = require('request');

const urlList = [];

const url = {
  url: 'https://swapi-api.alx-tools.com/api/films/' + args[2]
};
request(url, (error, response, body) => {
  if (error) {
    return console.error(error);
  }
  const json = JSON.parse(body);
  // get character id list
  const characters = json.characters;
  characters.forEach(function (url) {
    urlList.push(url);
  });

  // define function that makes request sequential
  function sequentialReq (urlList, index = 0) {
    if (index < urlList.length) {
      request(urlList[index], (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const character = JSON.parse(body);
          // print name
          console.log(character.name);
          // next function call
          sequentialReq(urlList, index + 1);
        } else {
          return console.error(error);
        }
      });
    }
  }
  // make function call
  sequentialReq(urlList);
});
