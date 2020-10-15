import * as React from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import CssBaseLine from "@material-ui/core/CssBaseline";
import { MuiThemeProvider } from "@material-ui/core/styles";

import SemesterAppBar from "./Components/AppBar";
import theme from "./Global/Theme";
import { GlobalState } from "./Store/Reducers";

const App = ({ darkMode }): JSX.Element => {
  return (
    <MuiThemeProvider theme={theme(darkMode)}>
      <CssBaseLine />
      <SemesterAppBar />
    </MuiThemeProvider>
  );
};

App.propTypes = {
  darkMode: PropTypes.bool.isRequired,
};

function mapStateToProps(state: GlobalState) {
  return {
    darkMode: state.darkMode,
  };
}

export default connect(mapStateToProps)(App);
