import * as React from "react";
import Paper from "@material-ui/core/Paper";
import Typography from "@material-ui/core/Typography";
import { makeStyles, Theme } from "@material-ui/core";
import Fade from "@material-ui/core/Fade";

const useStyles = makeStyles((theme: Theme) => ({
  root: {
    flex: 1,
    display: "flex",
    flexDirection: "column",
    margin: theme.spacing(1),
  },
  card: {
    flex: 1,
    display: "flex",
    justifyContent: "center",
    margin: theme.spacing(2),
    padding: theme.spacing(2),
  },
}));

function LoadingCard(): JSX.Element {
  const classes = useStyles();
  return (
    <Fade in timeout={1000}>
      <div className={classes.root}>
        <Paper className={classes.card}>
          <Typography variant="h3">Loading...</Typography>
        </Paper>
      </div>
    </Fade>
  );
}

export default LoadingCard;
