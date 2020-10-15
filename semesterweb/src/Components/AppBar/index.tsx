import PropTypes from "prop-types";
import * as React from "react";
import { connect } from "react-redux";

import AppBar from "@material-ui/core/AppBar";
import IconButton from "@material-ui/core/IconButton";
import { makeStyles } from "@material-ui/core/styles";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import AccountCircle from "@material-ui/icons/AccountCircle";
import InvertColors from "@material-ui/icons/InvertColors";
import MenuIcon from "@material-ui/icons/Menu";

import { toggleDarkMode } from "../../Store";

const useStyles = makeStyles({
  root: {},
  appbar: {
    padding: 0,
  },
  toolbar: {
    display: "flex",
    justifyContent: "space-between",
  },
});

function SemesterAppBar({ setDarkMode }): JSX.Element {
  const styles = useStyles();

  const onColorHandle = () => {
    setDarkMode();
  };

  return (
    <AppBar position="static" className={styles.appbar}>
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

SemesterAppBar.propTypes = {
  setDarkMode: PropTypes.func.isRequired,
};

function mapStateToDispatch(dispatch) {
  return {
    setDarkMode: () => {
      dispatch(toggleDarkMode());
    },
  };
}

export default connect(null, mapStateToDispatch)(SemesterAppBar);
