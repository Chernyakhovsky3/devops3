const path = require('path');

module.exports = {
  mode: 'development', // или 'production'
  entry: './src/index.js', // Путь к вашему исходному файлу
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist'),
  },
  module: {
    rules: [
      {
        test: /\.js$/, // Применяется ко всем .js файлам
        exclude: /node_modules/, // Исключает папку node_modules
        use: {
          loader: 'babel-loader', // Использование babel-loader
          options: {
            presets: ['@babel/preset-env'], // Использование пресета для современных возможностей JS
          },
        },
      },
    ],
  },
};
