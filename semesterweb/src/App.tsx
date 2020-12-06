import * as React from "react";

import { ConnectedProps, connect } from "react-redux";
import {
  MuiThemeProvider,
  Theme,
  createStyles,
  makeStyles,
} from "@material-ui/core/styles";

import Container from "@material-ui/core/Container";
import { CssBaseline } from "@material-ui/core";
import Grid from "@material-ui/core/Grid";
import RootGlobalTheme from "./Global/Theme";
import { RootState } from "./Store";
import Routes from "./Routes";
import SemesterAppBar from "./Components/AppBar";
import SemesterDrawer from "./Components/Drawer";
import clsx from "clsx";

function mapStateToProps(state: RootState) {
  return {
    darkMode: state.systemReducer.darkMode,
    sideBarOpen: state.systemReducer.sideBarOpen,
  };
}

const connector = connect(mapStateToProps, null);
type PropsFromRedux = ConnectedProps<typeof connector>;

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    root: {
      display: "flex",
      width: "100%",
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
      marginLeft: theme.spacing(7),
      transition: theme.transitions.create(["all"], {
        duration: 600,
        delay: 0,
      }),
    },
    contentMoving: {
      flex: 1,
      marginLeft: theme.spacing(20),
      transition: theme.transitions.create(["all"], {
        duration: 600,
        delay: 0,
      }),
    },
  })
);

const App = ({ darkMode, sideBarOpen }: PropsFromRedux): JSX.Element => {
  const styles = useStyles();
  return (
    <MuiThemeProvider theme={RootGlobalTheme(darkMode)}>
      <CssBaseline />
      <Grid className={styles.root}>
        <SemesterAppBar />
        <div
          style={{
            display: "flex",
            flex: 1,
            flexDirection: "row",
          }}
        >
          <div
            className={clsx({
              [styles.content]: !sideBarOpen,
              [styles.contentMoving]: sideBarOpen,
            })}
          >
            <div className={styles.toolbar} />
            <SemesterDrawer />
            <Container
              style={{
                display: "flex",
              }}
            >
              <Routes />
            </Container>
          </div>
        </div>
      </Grid>
    </MuiThemeProvider>
  );
};

export default connector(App);
