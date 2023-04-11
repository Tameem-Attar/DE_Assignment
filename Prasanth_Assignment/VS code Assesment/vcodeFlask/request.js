const http = require('http');

http.get('http://127.0.0.1:3500/', (response) => {
  let data = '';

  // A chunk of data has been received.
  response.on('data', (chunk) => {
    data += chunk;
  });

  // The whole response has been received.
  response.on('end', () => {
    console.log(data);
  });
}).on('error', (error) => {
  console.error(`Error: ${error.message}`);
});
