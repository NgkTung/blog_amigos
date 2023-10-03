/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.html", "./node_modules/tw-elements/dist/js/**/*.js"],
  theme: {
    listStyleType: {
      none: "none",
      disc: "disc",
      decimal: "decimal",
      square: "square",
      roman: "upper-roman",
    },
    fontFamily: {
      playfair: ["Playfair Display", "sans-serif"],
      lato: ["Lato", "sans-serif"],
      helvetica: ["Helvetica", "sans-serif"],
      "open-sans": ["Open Sans", "sans-serif"],
    },
    screens: {
      '2xl': {'max': '1536px'},
      'xl': {'max': '1280px'},
      'lg': {'max': '1024px'},
      'md': {'max': '768px'},
      'sm': {'max': '640px'},
    },
    extend: {
      colors:{
        'dark': '#1a1a1a',
      }
    },
  },
  plugins: [require("tw-elements/dist/plugin.cjs")],
  darkMode: "class",
};
