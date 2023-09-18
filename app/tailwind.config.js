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
    extend: {},
  },
  plugins: [require("tw-elements/dist/plugin.cjs")],
  darkMode: "class",
};
