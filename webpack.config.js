const path = require('path');

module.exports = {
  mode: 'development', // или 'production'
  entry: 'src/index.js', // Входной файл
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist'),
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader', // Для трансформации JS
        },
      },
    ],
  },
};