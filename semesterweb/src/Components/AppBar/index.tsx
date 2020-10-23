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
import { toggleDarkMode } from "../../Store/System";

function mapStateToDispatch(dispatch: Dispatch) {
  return {
    setDarkMode: () => {
      dispatch(toggleDarkMode());
    },
  };
}

const connector = connect(null, mapStateToDispatch);
type PropsFromRedux = ConnectedProps<typeof connector>;

const useStyles = makeStyles((theme) => ({
  appbar: {
    zIndex: theme.zIndex.drawer + 1,
  },
  toolbar: {
    justifyContent: "space-between",
  },
}));

function SemesterAppBar({ setDarkMode }: PropsFromRedux): JSX.Element {
  const styles = useStyles();

  const onColorHandle = () => {
    setDarkMode();
  };

  return (
    <AppBar position="fixed" className={styles.appbar}>
      <Toolbar className={styles.toolbar}>
        <IconButton edge="start">
          <MenuIcon />
        </IconButton>
        <Typography variant="h5">Semester Statistics</Typography>
        <div>
          <IconButton onClick={onColorHandle}>
            <InvertColors />
          </IconButton>
          <IconButton edge="end">
            <AccountCircle />
          </IconButton>
        </div>
      </Toolbar>
    </AppBar>
  );
}

export default connector(SemesterAppBar);
