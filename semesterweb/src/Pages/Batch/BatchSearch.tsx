import * as React from "react";
import { makeStyles, Theme } from "@material-ui/core";
import Paper from "@material-ui/core/Paper";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";

const useStyles = makeStyles((theme: Theme) => ({
  root: {
    flex: 1,
    display: "flex",
    flexDirection: "column",
  },
  card: {
    display: "flex",
    flexDirection: "column",
    margin: theme.spacing(3),
    padding: theme.spacing(2),
  },
  textHolder: {
    display: "flex",
    justifyContent: "space-evenly",
    margin: theme.spacing(1),
    padding: theme.spacing(2),
  },
  buttonHolder: {
    display: "flex",
    justifyContent: "space-evenly",
  },
}));

function BatchSearch(): JSX.Element {
  const classes = useStyles();
  return (
    <div className={classes.root}>
      <Paper className={classes.card}>
        <div className={classes.textHolder}>
          <TextField
            color="primary"
            variant="outlined"
            label="Batch"
            placeholder="2016"
          />
        </div>
        <div className={classes.buttonHolder}>
          <Button variant="contained" color="secondary">
            Go To Scores
          </Button>
          <Button variant="contained" color="secondary">
            Go To Backlogs
          </Button>
          <Button variant="contained" color="secondary">
            Go To Detained
          </Button>
          <Button variant="contained" color="secondary">
            Go To Aggregate
          </Button>
          <Button variant="contained" color="secondary">
            Go To Summary
          </Button>
        </div>
      </Paper>
    </div>
  );
}

export default BatchSearch;
