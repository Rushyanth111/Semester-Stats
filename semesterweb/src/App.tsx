import * as React from "react";
import { connect, ConnectedProps } from "react-redux";

import {
  makeStyles,
  MuiThemeProvider,
  Theme,
  createStyles,
} from "@material-ui/core/styles";

import { CssBaseline } from "@material-ui/core";
import SemesterAppBar from "./Components/AppBar";
import SemesterDrawer from "./Components/Drawer";
import RootGlobalTheme from "./Global/Theme";
import Routes from "./Routes";
import { RootState } from "./Store";

function mapStateToProps(state: RootState) {
  return {
    darkMode: state.systemReducer.darkMode,
  };
}

const connector = connect(mapStateToProps, null);
type PropsFromRedux = ConnectedProps<typeof connector>;

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    root: {
      display: "flex",
    },
    toolbar: {
      display: "flex",
      alignItems: "center",
      justifyContent: "flex-end",
      padding: theme.spacing(0, 1),
      ...theme.mixins.toolbar,
    },
    content: {
      flex: 1,
      padding: theme.spacing(3),
      zIndex: theme.zIndex.drawer,
    },
  })
);

const App = ({ darkMode }: PropsFromRedux): JSX.Element => {
  const styles = useStyles();
  return (
    <MuiThemeProvider theme={RootGlobalTheme(darkMode)}>
      <CssBaseline />
      <div className={styles.root}>
        <SemesterAppBar />
        <div
          style={{
            display: "flex",
            flexDirection: "row",
          }}
        >
          <SemesterDrawer />
          <main className={styles.content}>
            <div className={styles.toolbar} />
            <Routes />
          </main>
        </div>
      </div>
    </MuiThemeProvider>
  );
};

export default connector(App);
