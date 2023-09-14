// theme.js

import { createTheme } from '@mui/material/styles';

// Tema padrão
const lightTheme = createTheme({
  palette: {
    mode: 'light',
  },
});

// Tema escuro
const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

export { lightTheme, darkTheme };
