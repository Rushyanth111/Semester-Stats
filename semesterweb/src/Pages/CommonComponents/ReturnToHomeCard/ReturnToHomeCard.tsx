import * as React from "react";
import { useHistory } from "react-router";

import { makeStyles, Theme } from "@material-ui/core";
import Fade from "@material-ui/core/Fade";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import Button from "@material-ui/core/Button";

interface Props {
  content: string;
  location?: string;
}

const useStyles = makeStyles((theme: Theme) => ({
  buttonCard: {
    flex: 1,
    display: "flex",
    justifyContent: "space-evenly",
    padding: theme.spacing(1),
  },
}));

function ReturnToHomeCard({ content, location }: Props): JSX.Element {
  const classes = useStyles();
  const history = useHistory();
  const handleOnClickBack = () => {
    if (!location) history.goBack();
    else history.push(location);
  };

  return (
    <Fade in timeout={1500}>
      <Card className={classes.buttonCard} elevation={5}>
        <CardContent>
          <Button
            variant="outlined"
            color="secondary"
            onClick={handleOnClickBack}
          >
            {content}
          </Button>
        </CardContent>
      </Card>
    </Fade>
  );
}

export default ReturnToHomeCard;
