const path = require('path');

module.exports = {
  entry: {
    app: ['./assets/js/index.js'],
  },
  output: {
    path: path.resolve(__dirname, 'assets', 'bundles'),
    publicPath: '/assets/',
    filename: 'bundle.js',
  },
  module: {
    loaders: [
      {
        test: /.jsx?$/,
        loader: 'babel-loader',
        exclude: /node_modules/,
        query: {
          presets: ['es2015', 'react'],
        },
      },
    ],
  },
};
