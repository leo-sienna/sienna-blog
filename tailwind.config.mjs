/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        // Apple-inspired grays
        'apple-gray-50': '#fbfbfd',
        'apple-gray-100': '#f5f5f7',
        'apple-gray-200': '#e8e8ed',
        'apple-gray-300': '#d2d2d7',
        'apple-gray-400': '#86868b',
        'apple-gray-500': '#6e6e73',
        'apple-gray-600': '#515154',
        'apple-gray-700': '#323235',
        'apple-gray-800': '#1c1c1e',
        'apple-gray-900': '#000000',
        // Accent color (subtle blue like Apple)
        'apple-blue': '#0066cc',
        'apple-blue-light': '#2997ff',
      },
      fontFamily: {
        sans: [
          '-apple-system',
          'BlinkMacSystemFont',
          'SF Pro Display',
          'SF Pro Text',
          'Helvetica Neue',
          'Helvetica',
          'Arial',
          'sans-serif',
        ],
      },
      typography: {
        DEFAULT: {
          css: {
            maxWidth: 'none',
            color: '#1d1d1f',
            a: {
              color: '#0066cc',
              '&:hover': {
                color: '#2997ff',
              },
            },
          },
        },
      },
    },
  },
  plugins: [],
};
