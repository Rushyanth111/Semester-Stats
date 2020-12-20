import * as React from "react";
import Paper from "@material-ui/core/Paper";
import TextField from "@material-ui/core/TextField";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";
import { makeStyles, Theme } from "@material-ui/core/styles";
import { useHistory } from "react-router";
import Snackbar from "@material-ui/core/Snackbar";
import { isSubjectValid, isUsnValid } from "../../../../Helpers";

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
    flex: 1,
    display: "flex",
    justifyContent: "space-evenly",
    padding: theme.spacing(2),
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

function StudentScoreSearch(): JSX.Element {
  // Hooks.
  const classes = useStyles();
  const history = useHistory();

  // Input Feilds
  const [usn, setUsn] = React.useState("");
  const [subjectCode, setSubjectCode] = React.useState("");

  // Snack Bars
  const [isUsnSnackbarOpen, setUsnSnackbarOpen] = React.useState(false);
  const [isSubjectSnackbarOpen, setSubjectSnackbarOpen] = React.useState(false);
  const [isBothSnackbarOpen, setBothSnackbarOpen] = React.useState(false);
  const [snackbarCount, setSnackbarCount] = React.useState(0);

  // Handle SnackBars.
  const handleUsnSnackbarClose = (): void => {
    setUsnSnackbarOpen(false);
  };

  const handleSubjectSnackbarClose = (): void => {
    setSubjectSnackbarOpen(false);
  };

  const handleBothSnackbarClose = (): void => {
    setBothSnackbarOpen(false);
  };

  const multipleSnackbarHandle = (fn: (val: boolean) => void): void => {
    setSnackbarCount(snackbarCount + 1);
    fn(true);
  };

  const handleOnClickStudent = () => {
    console.log(subjectCode);
    if (!isUsnValid(usn) && !isSubjectValid(subjectCode)) {
      multipleSnackbarHandle(setBothSnackbarOpen);
    } else if (!isUsnValid(usn)) {
      multipleSnackbarHandle(setUsnSnackbarOpen);
    } else if (!isSubjectValid(subjectCode)) {
      multipleSnackbarHandle(setSubjectSnackbarOpen);
    } else history.push(`/Student/Score/${usn}/${subjectCode}`);
  };

  // Handle Text Feild Changes.
  const handleOnChangeUsnTextField = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    setUsn(event.target.value);
  };

  const handleOnChangeSubjectTextFeild = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    setSubjectCode(event.target.value);
  };

  return (
    <Paper className={classes.searchRoot} elevation={10}>
      <Snackbar
        open={isUsnSnackbarOpen}
        onClose={handleUsnSnackbarClose}
        autoHideDuration={3000}
        message={"Hey, That's not a Valid USN."}
        key={`StudentScoreSearchSnackBarUsn${snackbarCount}`}
        anchorOrigin={{
          horizontal: "center",
          vertical: "top",
        }}
      />
      <Snackbar
        open={isSubjectSnackbarOpen}
        onClose={handleSubjectSnackbarClose}
        autoHideDuration={3000}
        message={"Hey, That's not a Valid Subject Code."}
        key={`StudentScoreSearchSnackBarSubject${snackbarCount}`}
        anchorOrigin={{
          horizontal: "center",
          vertical: "top",
        }}
      />
      <Snackbar
        open={isBothSnackbarOpen}
        onClose={handleBothSnackbarClose}
        autoHideDuration={3000}
        message={"Hey, That's not a Valid USN And a Valid Subject Code."}
        key={`StudentScoreSearchSnackBarBoth${snackbarCount}`}
        anchorOrigin={{
          horizontal: "center",
          vertical: "top",
        }}
      />
      <Typography variant="h4" className={classes.title}>
        Specific Score For Student Search
      </Typography>
      <div className={classes.textFeild}>
        <TextField
          id="StudentScoreSearchUsn"
          variant="outlined"
          label="Student USN"
          placeholder="1CR17CS001"
          onChange={handleOnChangeUsnTextField}
        />
        <TextField
          id="StudentScoreSearchSubject"
          variant="outlined"
          label="Subject Code"
          placeholder="15CS51"
          onChange={handleOnChangeSubjectTextFeild}
        />
      </div>
      <div className={classes.searchButtonContainer}>
        <Button
          variant="contained"
          color="secondary"
          className={classes.searchButton}
          onClick={handleOnClickStudent}
        >
          Go To Score
        </Button>
      </div>
    </Paper>
  );
}

export default StudentScoreSearch;
