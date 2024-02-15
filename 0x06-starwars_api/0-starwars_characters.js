#!/usr/bin/node
const request = require('request');

const API_URL = 'https://swapi-api.hbtn.io/api/films';

if (process.argv.length > 2) {
    request(`${API_URL}/${process.argv[2]}`, (err, res, body) => {
        if (err) {
            console.log(err);
        } else {
            const data = JSON.parse(body).characters;
            if (data) {
                for (const url of data) {
                    request(url, (err, res, body) => {
                        if (err) {
                            console.log(err);
                        } else {
                            console.log(JSON.parse(body).name);
                        }
                    });
                }
            }
        }
    });
}
