const path = require('path');

module.exports = {
  mode: 'production',
  entry: './src/server.js',
  target: 'node',
  output: {
    filename: 'server.bundle.js',
    path: path.resolve(__dirname, 'dist'),
  },
};