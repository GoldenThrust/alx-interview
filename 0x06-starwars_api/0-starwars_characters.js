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
                const promiseData = data.map((url) =>
                    new Promise((resolve, reject) => {
                        request(url, (err, res, body) => {
                            if (err) {
                                reject(err);
                            } else {
                                resolve(JSON.parse(body).name);
                            }
                        });
                    })
                );

                Promise.all(promiseData).then((values) => {
                    console.log(values.join('\n'));
                }).catch((err) => console.log(err));
            } else {
                console.log('No result');
            }
        }
    });
} else {
    console.log('Usage: ./0-starwars_characters.js <film_id>');
}