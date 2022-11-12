/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: "jit",
  content: ["./templates/**/*.html"],
  theme: {
    extend: {},
  },
  plugins: [],
}

// npx tailwindcss -i static/src/input.css -o static/css/main.css --watch
