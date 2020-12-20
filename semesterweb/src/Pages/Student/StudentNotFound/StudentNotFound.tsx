import { makeStyles, Theme } from "@material-ui/core";
import * as React from "react";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import CardActions from "@material-ui/core/CardActions";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";
import Fade from "@material-ui/core/Fade";
import { useHistory } from "react-router";

const useStyles = makeStyles((theme: Theme) => ({
  root: {
    flex: 1,
    display: "flex",
    padding: theme.spacing(3),
    flexDirection: "column",
  },
}));

function StudentNotFound(): JSX.Element {
  const classes = useStyles();
  const history = useHistory();
  const handleOnClickBack = (): void => {
    history.push("/Student");
  };

  return (
    <div className={classes.root}>
      <Fade in timeout={1500}>
        <Card
          style={{
            display: "flex",
            justifyContent: "center",
            flexDirection: "column",
            alignItems: "center",
          }}
        >
          <CardContent>
            <Typography variant="h4">
              The Data Requested Does not Exist. Or No Active Records Exist.
            </Typography>
          </CardContent>
          <CardActions>
            <Button
              color="secondary"
              variant="outlined"
              onClick={handleOnClickBack}
            >
              Go Back to Search Page?
            </Button>
          </CardActions>
        </Card>
      </Fade>
    </div>
  );
}

export default StudentNotFound;
