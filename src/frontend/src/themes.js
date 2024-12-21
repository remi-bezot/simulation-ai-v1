import { createTheme } from "@mui/material/styles";

const theme = createTheme({
  palette: {
    primary: {
      main: "#007bff", // Couleur principale
    },
    secondary: {
      main: "#6c757d", // Couleur secondaire
    },
  },
  typography: {
    fontFamily: "Arial, sans-serif",
    h4: {
      fontWeight: 700,
    },
  },
});

export default theme;
