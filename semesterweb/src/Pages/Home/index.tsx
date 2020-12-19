import * as React from "react";

import { Theme, makeStyles } from "@material-ui/core/styles";

import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import Typography from "@material-ui/core/Typography";

const useStyles = makeStyles((theme: Theme) => ({
  rootComponent: {
    margin: theme.spacing(2),
    padding: theme.spacing(1),
    display: "flex",
    flexDirection: "row",
    justifyContent: "center",
    alignItems: "strech",
    flex: 1,
  },
  cardComponent: {
    flex: 1,
    margin: theme.spacing(1),
  },
}));

function Home(): JSX.Element {
  const classes = useStyles();
  return (
    <div className={classes.rootComponent}>
      <Card variant="elevation" className={classes.cardComponent}>
        <CardContent>
          <Typography variant="h3">Welcome to Semester Statistics</Typography>
          <Typography variant="body1">
            This is a Project Created By Rushyanth S (1CR17CS117), As a
            FullStack Web Application.
          </Typography>
        </CardContent>
      </Card>
    </div>
  );
}

export default Home;
