import * as React from "react";
import { connect, ConnectedProps } from "react-redux";
import CssBaseLine from "@material-ui/core/CssBaseline";
import { MuiThemeProvider } from "@material-ui/core/styles";

import SemesterAppBar from "./Components/AppBar";
import theme from "./Global/Theme";
import { RootState } from "./Store";

function mapStateToProps(state: RootState) {
  return {
    darkMode: state.systemReducer.darkMode,
  };
}

const connector = connect(mapStateToProps, null);
type PropsFromRedux = ConnectedProps<typeof connector>;

const App = ({ darkMode }: PropsFromRedux): JSX.Element => {
  return (
    <MuiThemeProvider theme={theme(darkMode)}>
      <CssBaseLine />
      <SemesterAppBar />
    </MuiThemeProvider>
  );
};

export default connector(App);
