import clsx from "clsx";
import * as React from "react";
import { connect, ConnectedProps } from "react-redux";

import Drawer from "@material-ui/core/Drawer";
import Fade from "@material-ui/core/Fade";
import ListItem from "@material-ui/core/ListItem";
import ListItemIcon from "@material-ui/core/ListItemIcon";
import ListItemText from "@material-ui/core/ListItemText";
import { createStyles, makeStyles } from "@material-ui/core/styles";
import Toolbar from "@material-ui/core/Toolbar";
import Subject from "@material-ui/icons/Book";
import Home from "@material-ui/icons/Home";
import Summary from "@material-ui/icons/Pages";
import Batch from "@material-ui/icons/People";
import Student from "@material-ui/icons/Person";

import { Link as RouterLink } from "react-router-dom";
import { RootState } from "../../Store";

function mapStateToProps(state: RootState) {
  return {
    sideBarOpen: state.systemReducer.sideBarOpen,
  };
}

const connector = connect(mapStateToProps, null);
type PropsFromRedux = ConnectedProps<typeof connector>;

const useStyles = makeStyles((theme) =>
  createStyles({
    root: {
      width: theme.spacing(7),
    },
    rootOpen: {
      width: theme.spacing(20),
    },
    rootPaper: {
      width: theme.spacing(7),
      overflowX: "hidden",
      transition: theme.transitions.create(["all"], {
        duration: 600,
        delay: 0,
      }),
    },
    rootOpenPaper: {
      width: theme.spacing(20),
      overflowX: "hidden",
      transition: theme.transitions.create(["all"], {
        duration: 600,
        delay: 0,
      }),
    },
    buttonspacer: {
      display: "flex",
      flexDirection: "row",
      justifyContent: "space-around",
    },
  })
);

function SemesterDrawer({ sideBarOpen }: PropsFromRedux): JSX.Element {
  const classes = useStyles();

  return (
    <Drawer
      variant="persistent"
      open
      className={clsx({
        [classes.root]: !sideBarOpen,
        [classes.rootOpen]: sideBarOpen,
      })}
      classes={{
        paper: clsx({
          [classes.rootPaper]: !sideBarOpen,
          [classes.rootOpenPaper]: sideBarOpen,
        }),
      }}
    >
      <Toolbar />
      <ListItem button component={RouterLink} to="/">
        <ListItemIcon>
          <Home />
        </ListItemIcon>
        <Fade in={sideBarOpen} timeout={1200}>
          <ListItemText primary="Home" />
        </Fade>
      </ListItem>
      <ListItem button component={RouterLink} to="/Batch">
        <ListItemIcon>
          <Batch />
        </ListItemIcon>
        <Fade in={sideBarOpen} timeout={1200}>
          <ListItemText primary="Batch" />
        </Fade>
      </ListItem>
      <ListItem button component={RouterLink} to="/Student">
        <ListItemIcon>
          <Student />
        </ListItemIcon>
        <Fade in={sideBarOpen} timeout={1200}>
          <ListItemText primary="Student" />
        </Fade>
      </ListItem>
      <ListItem button component={RouterLink} to="/Subject">
        <ListItemIcon>
          <Subject />
        </ListItemIcon>
        <Fade in={sideBarOpen} timeout={1200}>
          <ListItemText primary="Subject" />
        </Fade>
      </ListItem>
      <ListItem button component={RouterLink} to="/Summary">
        <ListItemIcon>
          <Summary />
        </ListItemIcon>
        <Fade in={sideBarOpen} timeout={1200}>
          <ListItemText primary="Summary" />
        </Fade>
      </ListItem>
    </Drawer>
  );
}

export default connector(SemesterDrawer);
