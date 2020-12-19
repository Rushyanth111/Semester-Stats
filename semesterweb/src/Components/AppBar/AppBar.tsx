import * as React from "react";
import { connect, ConnectedProps } from "react-redux";

import AppBar from "@material-ui/core/AppBar";
import IconButton from "@material-ui/core/IconButton";
import { makeStyles } from "@material-ui/core/styles";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import AccountCircle from "@material-ui/icons/AccountCircle";
import InvertColors from "@material-ui/icons/InvertColors";
import MenuIcon from "@material-ui/icons/Menu";

import { Dispatch } from "redux";
import LinearProgress from "@material-ui/core/LinearProgress";
import { toggleDarkMode, openSideBar } from "../../Store/System";
import { SystemState } from "../../Store/System/Reducers";

function mapStateToDispatch(dispatch: Dispatch) {
  return {
    setDarkMode: () => {
      dispatch(toggleDarkMode());
    },
    setSideBar: () => {
      dispatch(openSideBar());
    },
  };
}

function mapStateToProps(state: SystemState) {
  return {
    isloading: state.loadingToggle,
  };
}

const connector = connect(mapStateToProps, mapStateToDispatch);
type PropsFromRedux = ConnectedProps<typeof connector>;

const useStyles = makeStyles((theme) => ({
  appbar: {
    zIndex: theme.zIndex.drawer + 1,
  },
  toolbar: {
    justifyContent: "space-between",
  },
}));

function SemesterAppBar({
  setDarkMode,
  setSideBar,
  isloading,
}: PropsFromRedux): JSX.Element {
  const styles = useStyles();

  const onColorHandleClick = () => {
    setDarkMode();
  };

  const onSideBarHandleClick = () => {
    setSideBar();
  };

  return (
    <AppBar position="fixed" className={styles.appbar}>
      <Toolbar className={styles.toolbar}>
        <IconButton edge="start" onClick={onSideBarHandleClick}>
          <MenuIcon />
        </IconButton>
        <Typography variant="h5">Semester Statistics</Typography>
        <div>
          <IconButton onClick={onColorHandleClick}>
            <InvertColors />
          </IconButton>
          <IconButton edge="end">
            <AccountCircle />
          </IconButton>
        </div>
      </Toolbar>
      {isloading && <LinearProgress />}
    </AppBar>
  );
}

export default connector(SemesterAppBar);
