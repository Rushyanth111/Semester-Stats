import { lightBlue, red } from "@material-ui/core/colors";
import { createMuiTheme, Theme } from "@material-ui/core/styles";

const theme = (darkMode: boolean): Theme => {
  const type = darkMode ? "dark" : "light";
  return createMuiTheme({
    palette: {
      primary: {
        main: red[400],
      },
      secondary: {
        main: lightBlue[500],
      },
      type,
    },
  });
};

export default theme;
