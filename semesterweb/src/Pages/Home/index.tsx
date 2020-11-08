import * as React from "react";

import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import { makeStyles, Theme } from "@material-ui/core/styles";
import Typography from "@material-ui/core/Typography";

const useStyles = makeStyles((theme: Theme) => ({
  rootComponent: {
    margin: theme.spacing(2),
    padding: theme.spacing(1),
    display: "flex",
    flexDirection: "row",
    justifyContent: "space-around",
  },
  cardComponent: {
    margin: theme.spacing(1),
  },
}));

function Home(): JSX.Element {
  const classes = useStyles();
  return (
    <div className={classes.rootComponent}>
      <Card variant="elevation" className={classes.cardComponent}>
        <CardContent>
          <Typography>This is a Card!</Typography>
        </CardContent>
      </Card>
      <Card variant="elevation" className={classes.cardComponent}>
        <CardContent>
          <Typography>This is a Card!</Typography>
        </CardContent>
      </Card>
    </div>
  );
}

export default Home;
