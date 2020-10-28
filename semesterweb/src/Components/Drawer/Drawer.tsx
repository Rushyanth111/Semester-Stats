import clsx from "clsx";
import * as React from "react";
import { ConnectedProps, connect } from "react-redux";

import { createStyles, Toolbar, Typography } from "@material-ui/core";
import Button from "@material-ui/core/Button";
import Drawer from "@material-ui/core/Drawer";
import Fade from "@material-ui/core/Fade";
import { makeStyles } from "@material-ui/core/styles";
import AccountCircle from "@material-ui/icons/AccountCircle";

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
      width: theme.spacing(10),
    },
    rootOpen: {
      width: theme.spacing(20),
    },
    rootPaper: {
      width: theme.spacing(10),
      transition: theme.transitions.create(["all"], {
        duration: 400,
        delay: 0,
      }),
    },
    rootOpenPaper: {
      width: theme.spacing(20),
      transition: theme.transitions.create(["all"], {
        duration: 400,
        delay: 0,
      }),
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
      <Button>
        <AccountCircle />
        {sideBarOpen && (
          <Fade in={sideBarOpen}>
            <Typography variant="body1">Something Something</Typography>
          </Fade>
        )}
      </Button>
    </Drawer>
  );
}

export default connector(SemesterDrawer);
