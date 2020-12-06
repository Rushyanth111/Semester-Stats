import * as React from "react";
import Paper from "@material-ui/core/Paper";
import TextField from "@material-ui/core/TextField";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";

import { makeStyles, Theme } from "@material-ui/core/styles";
import { useHistory } from "react-router";

const useStyles = makeStyles((theme: Theme) => ({
  studentRootComponent: {
    flex: "1",
    display: "flex",
    flexDirection: "column",
    margin: theme.spacing(2),
    padding: theme.spacing(1),
  },
  searchTypographyTitle: {
    alignSelf: "center",
    padding: theme.spacing(2),
  },
  searchTextField: {
    margin: theme.spacing(1),
  },
  searchButton: {
    alignSelf: "center",
  },
}));

function StudentGoTo(): JSX.Element {
  const classes = useStyles();
  const [usn, setUsn] = React.useState("");
  const history = useHistory();
  const handleOnClickGoToStudent = () => {
    history.push(`/Student/${usn}`);
  };

  const handleOnChangeTextField = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    setUsn(event.target.value);
  };

  return (
    <Paper className={classes.studentRootComponent}>
      <Typography variant="h4" className={classes.searchTypographyTitle}>
        Student Search
      </Typography>
      <div className={classes.searchTextField}>
        <TextField
          id="something"
          variant="outlined"
          label="Student USN"
          placeholder="1CR17CS001"
          autoFocus
          fullWidth
          onChange={handleOnChangeTextField}
        />
      </div>
      <Button
        variant="contained"
        color="primary"
        className={classes.searchButton}
        onClick={handleOnClickGoToStudent}
      >
        Go!
      </Button>
    </Paper>
  );
}

export default StudentGoTo;
