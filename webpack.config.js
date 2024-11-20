const path = require('path');

module.exports = {
  entry: './src/index.js', // Входной файл
  output: {
    filename: 'bundle.js', // Имя выходного файла
    path: path.resolve(__dirname, 'dist'), // Путь к директории для сохранения результата
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader', // Если используете Babel для JS
        },
      },
    ],
  },
  resolve: {
    extensions: ['.js', '.json'], // Расширения файлов, которые Webpack будет обрабатывать
  },
};