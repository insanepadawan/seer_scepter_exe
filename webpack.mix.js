let mix = require('laravel-mix');

mix
    .js('src/js/app.js', 'dist')
    .sass('src/scss/theme.scss', 'dist');