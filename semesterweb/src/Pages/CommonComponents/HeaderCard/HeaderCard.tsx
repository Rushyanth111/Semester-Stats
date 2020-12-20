import * as React from "react";
import Fade from "@material-ui/core/Fade";
import Typography from "@material-ui/core/Typography";
import Paper from "@material-ui/core/Paper";
import { makeStyles, Theme } from "@material-ui/core";

const useStyles = makeStyles((theme: Theme) => ({
  titleCard: {
    flex: 1,
    display: "flex",
    justifyContent: "center",
    marginBottom: theme.spacing(3),
    padding: theme.spacing(2),
  },
}));

interface Props {
  content: string;
}

function HeaderCard({ content }: Props): JSX.Element {
  const classes = useStyles();
  return (
    <Fade in timeout={1000}>
      <Paper className={classes.titleCard} elevation={5}>
        <Typography variant="h3">{content}</Typography>
      </Paper>
    </Fade>
  );
}

export default HeaderCard;
