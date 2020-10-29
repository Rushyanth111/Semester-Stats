import * as React from "react";
import Paper from "@material-ui/core/Paper";
import Typography from "@material-ui/core/Typography";
import { makeStyles, Theme } from "@material-ui/core/styles";

const useStyles = makeStyles((theme: Theme) => ({
  rootComponent: {
    margin: theme.spacing(2),
    padding: theme.spacing(1),
  },
}));

function Home(): JSX.Element {
  const classes = useStyles();
  return (
    <Paper className={classes.rootComponent}>
      <Typography>Hello, Welcome to Home. Heck</Typography>
    </Paper>
  );
}

export default Home;
