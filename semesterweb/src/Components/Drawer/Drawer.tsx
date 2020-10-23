import * as React from "react";
import clsx from "clsx";
import { makeStyles } from "@material-ui/core/styles";
import Drawer from "@material-ui/core/Drawer";
import Button from "@material-ui/core/Button";
import AccountCircle from "@material-ui/icons/AccountCircle";
import { createStyles, Toolbar, Typography } from "@material-ui/core";
import Fade from "@material-ui/core/Fade";

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

function SemesterDrawer(): JSX.Element {
  const [open, setOpen] = React.useState(false);
  const classes = useStyles();

  const handleOpen = () => {
    setOpen(!open);
  };
  return (
    <Drawer
      variant="persistent"
      open
      className={clsx({ [classes.root]: !open, [classes.rootOpen]: open })}
      classes={{
        paper: clsx({
          [classes.rootPaper]: !open,
          [classes.rootOpenPaper]: open,
        }),
      }}
    >
      <Toolbar />
      <Button onClick={handleOpen}>
        <AccountCircle />
        {open && (
          <Fade in={open}>
            <Typography variant="body1">Something Something</Typography>
          </Fade>
        )}
      </Button>
    </Drawer>
  );
}

export default SemesterDrawer;
