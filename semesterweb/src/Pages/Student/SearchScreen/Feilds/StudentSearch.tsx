import * as React from "react";
import Paper from "@material-ui/core/Paper";
import TextField from "@material-ui/core/TextField";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";
import { makeStyles, Theme } from "@material-ui/core/styles";
import { useHistory } from "react-router";
import Snackbar from "@material-ui/core/Snackbar";
import { isUsnValid } from "../../../../Helpers";

const useStyles = makeStyles((theme: Theme) => ({
  searchRoot: {
    display: "flex",
    flexDirection: "column",
    margin: theme.spacing(2),
    padding: theme.spacing(1),
  },
  title: {
    alignSelf: "center",
    padding: theme.spacing(3),
  },
  textFeild: {
    display: "flex",
    padding: theme.spacing(2),
    justifyContent: "space-evenly",
  },
  searchButtonContainer: {
    flex: 1,
    display: "flex",
    flexDirection: "row",
    padding: theme.spacing(3),
    justifyContent: "space-evenly",
  },
  searchButton: {
    alignSelf: "center",
    padding: theme.spacing(1),
  },
}));

function StudentSearch(): JSX.Element {
  const classes = useStyles();
  const [usn, setUsn] = React.useState("");
  const [isSnackbarOpen, setSnackbarOpen] = React.useState(false);
  const [snackbarCount, setSnackbarCount] = React.useState(0);
  const history = useHistory();

  const handleSnackbarClose = (): void => {
    setSnackbarOpen(false);
  };

  const multipleSnackbarHandle = (): void => {
    setSnackbarCount(snackbarCount + 1);
    setSnackbarOpen(true);
  };

  const handleOnClickStudent = () => {
    if (!isUsnValid(usn)) multipleSnackbarHandle();
    else history.push(`/Student/${usn}`);
  };

  const handleOnClickStudentBacklogs = () => {
    if (!isUsnValid(usn)) multipleSnackbarHandle();
    else history.push(`/Student/Backlogs/${usn}`);
  };

  const handleOnClickStudentScores = () => {
    if (!isUsnValid(usn)) multipleSnackbarHandle();
    else history.push(`/Student/Scores/${usn}`);
  };

  const handleOnChangeTextField = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    setUsn(event.target.value);
  };

  return (
    <Paper className={classes.searchRoot} elevation={10}>
      <Snackbar
        open={isSnackbarOpen}
        onClose={handleSnackbarClose}
        autoHideDuration={3000}
        message={"Hey, That's not a Valid USN."}
        key={`StudentSearchPageSnackBar${snackbarCount}`}
        anchorOrigin={{
          horizontal: "center",
          vertical: "top",
        }}
      />
      <Typography variant="h4" className={classes.title}>
        Student Search
      </Typography>
      <div className={classes.textFeild}>
        <TextField
          id="StudentSearch"
          variant="outlined"
          label="Student USN"
          placeholder="1CR17CS001"
          onChange={handleOnChangeTextField}
        />
      </div>
      <div className={classes.searchButtonContainer}>
        <Button
          variant="contained"
          color="secondary"
          className={classes.searchButton}
          onClick={handleOnClickStudent}
        >
          Go To Student Page
        </Button>
        <Button
          variant="contained"
          color="secondary"
          className={classes.searchButton}
          onClick={handleOnClickStudentBacklogs}
        >
          Go To Student Backlogs
        </Button>
        <Button
          variant="contained"
          color="secondary"
          className={classes.searchButton}
          onClick={handleOnClickStudentScores}
        >
          Go To Student Scores
        </Button>
      </div>
    </Paper>
  );
}

export default StudentSearch;
